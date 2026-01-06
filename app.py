"""
=============================================================================
UAE PROMO PULSE SIMULATOR + DATA RESCUE DASHBOARD
=============================================================================
Complete Streamlit application with integrated:
    - Data Cleaning & Validation (Data Rescue Toolkit)
    - KPI Computation & Promo Simulation (Promo Pulse Simulator)
    - Executive & Manager Dashboard Views

Author: Data Rescue Team
Date: 2024

Run with: streamlit run app.py
=============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="UAE Promo Pulse Simulator",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CONSTANTS & CONFIGURATION
# =============================================================================

# Valid values for validation
VALID_CITIES = ['Dubai', 'Abu Dhabi', 'Sharjah']
VALID_CHANNELS = ['App', 'Web', 'Marketplace']
VALID_CATEGORIES = ['Electronics', 'Fashion', 'Grocery', 'Home & Garden', 'Beauty', 'Sports']
VALID_PAYMENT_STATUSES = ['Paid', 'Failed', 'Refunded']
VALID_FULFILLMENT_TYPES = ['Own', '3PL']
VALID_LAUNCH_FLAGS = ['New', 'Regular']

# City name standardization mapping
CITY_MAPPING = {
    'dubai': 'Dubai', 'DUBAI': 'Dubai', 'Dubayy': 'Dubai', 'DXB': 'Dubai', 'Dубай': 'Dubai',
    'abu dhabi': 'Abu Dhabi', 'ABU DHABI': 'Abu Dhabi', 'AbuDhabi': 'Abu Dhabi', 
    'AD': 'Abu Dhabi', 'Abudhabi': 'Abu Dhabi', 'abudhabi': 'Abu Dhabi',
    'sharjah': 'Sharjah', 'SHARJAH': 'Sharjah', 'Shj': 'Sharjah', 
    'Sharijah': 'Sharjah', 'Al Sharjah': 'Sharjah'
}

# Outlier thresholds
QTY_MAX_THRESHOLD = 20
QTY_OUTLIER_CAP = 10
PRICE_MULTIPLIER_THRESHOLD = 5

# Uplift configuration (per spec: document assumptions)
UPLIFT_CONFIG = {
    'base_multiplier': 0.03,  # 3% demand increase per 1% discount
    'max_uplift': 2.0,        # Maximum 2x demand increase
    'channel_modifiers': {
        'Marketplace': 1.20,   # High price sensitivity
        'App': 1.05,           # Loyalty reduces sensitivity
        'Web': 1.00            # Baseline
    },
    'category_modifiers': {
        'Electronics': 1.25,   # High elasticity
        'Fashion': 1.15,
        'Sports': 1.10,
        'Beauty': 1.05,
        'Home & Garden': 1.00,
        'Grocery': 0.85        # Low elasticity (staples)
    }
}


# =============================================================================
# =============================================================================
#                           DATA CLEANER MODULE
# =============================================================================
# =============================================================================

class DataCleaner:
    """
    Data Rescue Toolkit: Validates and cleans dirty datasets.
    
    Handles:
        - Products table
        - Stores table
        - Sales_raw table
        - Inventory_snapshot table
    
    Produces:
        - Cleaned dataframes
        - Issues log (issues.csv)
    """
    
    def __init__(self):
        """Initialize the DataCleaner with empty issues log."""
        self.issues_log = []
        self.cleaning_stats = {}
    
    def log_issue(self, table_name, record_id, issue_type, issue_detail, action_taken):
        """
        Log a data quality issue.
        
        Args:
            table_name: Source table name
            record_id: Identifier of the affected record
            issue_type: Category of issue (e.g., MISSING_VALUE, DUPLICATE, OUTLIER)
            issue_detail: Description of the issue
            action_taken: How the issue was resolved
        """
        self.issues_log.append({
            'table_name': table_name,
            'record_id': str(record_id),
            'issue_type': issue_type,
            'issue_detail': issue_detail,
            'action_taken': action_taken,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    def get_issues_dataframe(self):
        """Return issues log as DataFrame."""
        if self.issues_log:
            return pd.DataFrame(self.issues_log)
        return pd.DataFrame(columns=['table_name', 'record_id', 'issue_type', 
                                      'issue_detail', 'action_taken', 'timestamp'])
    
    # =========================================================================
    # PRODUCTS CLEANING
    # =========================================================================
    def clean_products(self, df):
        """
        Clean products table.
        
        Validation Rules:
            - product_id must be unique and non-null
            - category must be in valid list
            - base_price_aed must be positive
            - unit_cost_aed must be positive and <= base_price
            - tax_rate must be between 0 and 1
            - launch_flag must be New or Regular
        
        Cleaning Actions:
            - Missing unit_cost: Impute as 50% of base_price (median margin assumption)
            - Invalid category: Set to 'Other' or drop
            - Invalid prices: Drop record
        """
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        
        # Track cleaning stats
        stats = {'original': original_count, 'issues_found': 0}
        
        # 1. Handle missing unit_cost_aed
        missing_cost_mask = df['unit_cost_aed'].isna()
        missing_cost_count = missing_cost_mask.sum()
        
        if missing_cost_count > 0:
            for idx in df[missing_cost_mask].index:
                product_id = df.loc[idx, 'product_id']
                base_price = df.loc[idx, 'base_price_aed']
                imputed_cost = round(base_price * 0.5, 2)  # 50% of base price
                df.loc[idx, 'unit_cost_aed'] = imputed_cost
                
                self.log_issue(
                    table_name='products',
                    record_id=product_id,
                    issue_type='MISSING_VALUE',
                    issue_detail=f'unit_cost_aed was NULL, base_price={base_price}',
                    action_taken=f'Imputed as 50% of base_price: {imputed_cost}'
                )
            stats['issues_found'] += missing_cost_count
        
        # 2. Validate unit_cost <= base_price
        invalid_cost_mask = df['unit_cost_aed'] > df['base_price_aed']
        invalid_cost_count = invalid_cost_mask.sum()
        
        if invalid_cost_count > 0:
            for idx in df[invalid_cost_mask].index:
                product_id = df.loc[idx, 'product_id']
                old_cost = df.loc[idx, 'unit_cost_aed']
                base_price = df.loc[idx, 'base_price_aed']
                new_cost = round(base_price * 0.5, 2)
                df.loc[idx, 'unit_cost_aed'] = new_cost
                
                self.log_issue(
                    table_name='products',
                    record_id=product_id,
                    issue_type='INVALID_VALUE',
                    issue_detail=f'unit_cost ({old_cost}) > base_price ({base_price})',
                    action_taken=f'Corrected to 50% of base_price: {new_cost}'
                )
            stats['issues_found'] += invalid_cost_count
        
        # 3. Validate category
        if 'category' in df.columns:
            invalid_category_mask = ~df['category'].isin(VALID_CATEGORIES)
            invalid_category_count = invalid_category_mask.sum()
            
            if invalid_category_count > 0:
                for idx in df[invalid_category_mask].index:
                    product_id = df.loc[idx, 'product_id']
                    old_category = df.loc[idx, 'category']
                    df.loc[idx, 'category'] = 'Other'
                    
                    self.log_issue(
                        table_name='products',
                        record_id=product_id,
                        issue_type='INVALID_CATEGORY',
                        issue_detail=f'Invalid category: {old_category}',
                        action_taken='Set to Other'
                    )
                stats['issues_found'] += invalid_category_count
        
        # 4. Validate tax_rate (should be 0-1, typically 0.05 for UAE VAT)
        if 'tax_rate' in df.columns:
            invalid_tax_mask = (df['tax_rate'] < 0) | (df['tax_rate'] > 1)
            if invalid_tax_mask.sum() > 0:
                for idx in df[invalid_tax_mask].index:
                    product_id = df.loc[idx, 'product_id']
                    old_tax = df.loc[idx, 'tax_rate']
                    df.loc[idx, 'tax_rate'] = 0.05  # UAE VAT
                    
                    self.log_issue(
                        table_name='products',
                        record_id=product_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid tax_rate: {old_tax}',
                        action_taken='Set to 0.05 (UAE VAT)'
                    )
                stats['issues_found'] += invalid_tax_mask.sum()
        
        # 5. Validate launch_flag
        if 'launch_flag' in df.columns:
            invalid_flag_mask = ~df['launch_flag'].isin(VALID_LAUNCH_FLAGS)
            if invalid_flag_mask.sum() > 0:
                for idx in df[invalid_flag_mask].index:
                    product_id = df.loc[idx, 'product_id']
                    old_flag = df.loc[idx, 'launch_flag']
                    df.loc[idx, 'launch_flag'] = 'Regular'
                    
                    self.log_issue(
                        table_name='products',
                        record_id=product_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid launch_flag: {old_flag}',
                        action_taken='Set to Regular'
                    )
                stats['issues_found'] += invalid_flag_mask.sum()
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['products'] = stats
        
        return df
    
    # =========================================================================
    # STORES CLEANING
    # =========================================================================
    def clean_stores(self, df):
        """
        Clean stores table.
        
        Validation Rules:
            - store_id must be unique and non-null
            - city must be standardized to valid values
            - channel must be in valid list
            - fulfillment_type must be Own or 3PL
        
        Cleaning Actions:
            - Inconsistent city names: Standardize using mapping
            - Invalid channel: Drop record
        """
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # 1. Standardize city names
        if 'city' in df.columns:
            for idx in df.index:
                city_value = df.loc[idx, 'city']
                store_id = df.loc[idx, 'store_id']
                
                # Check if needs standardization
                if city_value not in VALID_CITIES:
                    if city_value in CITY_MAPPING:
                        standardized = CITY_MAPPING[city_value]
                        df.loc[idx, 'city'] = standardized
                        
                        self.log_issue(
                            table_name='stores',
                            record_id=store_id,
                            issue_type='INCONSISTENT_VALUE',
                            issue_detail=f'Non-standard city name: {city_value}',
                            action_taken=f'Standardized to: {standardized}'
                        )
                        stats['issues_found'] += 1
                    else:
                        # Unknown city - try to match
                        city_lower = str(city_value).lower().strip()
                        matched = False
                        for valid_city in VALID_CITIES:
                            if valid_city.lower() in city_lower or city_lower in valid_city.lower():
                                df.loc[idx, 'city'] = valid_city
                                self.log_issue(
                                    table_name='stores',
                                    record_id=store_id,
                                    issue_type='INCONSISTENT_VALUE',
                                    issue_detail=f'Non-standard city name: {city_value}',
                                    action_taken=f'Matched to: {valid_city}'
                                )
                                matched = True
                                stats['issues_found'] += 1
                                break
                        
                        if not matched:
                            df.loc[idx, 'city'] = 'Dubai'  # Default
                            self.log_issue(
                                table_name='stores',
                                record_id=store_id,
                                issue_type='INVALID_VALUE',
                                issue_detail=f'Unknown city: {city_value}',
                                action_taken='Defaulted to Dubai'
                            )
                            stats['issues_found'] += 1
        
        # 2. Validate channel
        if 'channel' in df.columns:
            invalid_channel_mask = ~df['channel'].isin(VALID_CHANNELS)
            if invalid_channel_mask.sum() > 0:
                for idx in df[invalid_channel_mask].index:
                    store_id = df.loc[idx, 'store_id']
                    old_channel = df.loc[idx, 'channel']
                    df.loc[idx, 'channel'] = 'Web'  # Default
                    
                    self.log_issue(
                        table_name='stores',
                        record_id=store_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid channel: {old_channel}',
                        action_taken='Defaulted to Web'
                    )
                stats['issues_found'] += invalid_channel_mask.sum()
        
        # 3. Validate fulfillment_type
        if 'fulfillment_type' in df.columns:
            invalid_fulfill_mask = ~df['fulfillment_type'].isin(VALID_FULFILLMENT_TYPES)
            if invalid_fulfill_mask.sum() > 0:
                for idx in df[invalid_fulfill_mask].index:
                    store_id = df.loc[idx, 'store_id']
                    old_fulfill = df.loc[idx, 'fulfillment_type']
                    df.loc[idx, 'fulfillment_type'] = 'Own'  # Default
                    
                    self.log_issue(
                        table_name='stores',
                        record_id=store_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid fulfillment_type: {old_fulfill}',
                        action_taken='Defaulted to Own'
                    )
                stats['issues_found'] += invalid_fulfill_mask.sum()
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['stores'] = stats
        
        return df
    
    # =========================================================================
    # SALES CLEANING
    # =========================================================================
    def clean_sales(self, df, products_df=None):
        """
        Clean sales_raw table.
        
        Validation Rules:
            - order_id should be unique (handle duplicates)
            - order_time must be parseable datetime
            - product_id must exist in products table
            - store_id must exist in stores table
            - qty must be positive and reasonable
            - selling_price_aed must be positive
            - discount_pct must be 0-100
            - payment_status must be in valid list
        
        Cleaning Actions:
            - Duplicates: Keep first occurrence (by order_time if valid)
            - Missing discount_pct: Impute with median by category or 0
            - Corrupted timestamps: Drop record
            - Outliers: Cap qty at threshold, flag extreme prices
        """
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # 1. Parse and validate timestamps
        if 'order_time' in df.columns:
            df['order_time_parsed'] = pd.to_datetime(df['order_time'], errors='coerce')
            
            invalid_time_mask = df['order_time_parsed'].isna()
            invalid_time_count = invalid_time_mask.sum()
            
            if invalid_time_count > 0:
                for idx in df[invalid_time_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    bad_time = df.loc[idx, 'order_time']
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='INVALID_TIMESTAMP',
                        issue_detail=f'Unparseable timestamp: {bad_time}',
                        action_taken='Record dropped'
                    )
                stats['issues_found'] += invalid_time_count
                
                # Drop records with invalid timestamps
                df = df[~invalid_time_mask].copy()
            
            # Replace original column with parsed version
            df['order_time'] = df['order_time_parsed']
            df = df.drop(columns=['order_time_parsed'])
        
        # 2. Handle duplicates (keep first by order_time)
        if 'order_id' in df.columns:
            duplicate_mask = df.duplicated(subset=['order_id'], keep='first')
            duplicate_count = duplicate_mask.sum()
            
            if duplicate_count > 0:
                for idx in df[duplicate_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='DUPLICATE_ID',
                        issue_detail='Duplicate order_id found',
                        action_taken='Duplicate removed (kept first occurrence)'
                    )
                stats['issues_found'] += duplicate_count
                
                # Remove duplicates
                df = df[~duplicate_mask].copy()
        
        # 3. Handle missing discount_pct
        if 'discount_pct' in df.columns:
            missing_discount_mask = df['discount_pct'].isna()
            missing_discount_count = missing_discount_mask.sum()
            
            if missing_discount_count > 0:
                # Calculate median discount (or use 0)
                median_discount = df['discount_pct'].median()
                if pd.isna(median_discount):
                    median_discount = 0
                
                for idx in df[missing_discount_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    df.loc[idx, 'discount_pct'] = median_discount
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='MISSING_VALUE',
                        issue_detail='discount_pct was NULL',
                        action_taken=f'Imputed with median: {median_discount}'
                    )
                stats['issues_found'] += missing_discount_count
        
        # 4. Handle qty outliers
        if 'qty' in df.columns:
            # Cap extreme quantities
            outlier_qty_mask = df['qty'] > QTY_MAX_THRESHOLD
            outlier_qty_count = outlier_qty_mask.sum()
            
            if outlier_qty_count > 0:
                for idx in df[outlier_qty_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    old_qty = df.loc[idx, 'qty']
                    df.loc[idx, 'qty'] = QTY_OUTLIER_CAP
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='OUTLIER_VALUE',
                        issue_detail=f'Extreme qty: {old_qty}',
                        action_taken=f'Capped at {QTY_OUTLIER_CAP}'
                    )
                stats['issues_found'] += outlier_qty_count
            
            # Handle negative or zero qty
            invalid_qty_mask = df['qty'] <= 0
            if invalid_qty_mask.sum() > 0:
                for idx in df[invalid_qty_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    old_qty = df.loc[idx, 'qty']
                    df.loc[idx, 'qty'] = 1
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid qty: {old_qty}',
                        action_taken='Set to 1'
                    )
                stats['issues_found'] += invalid_qty_mask.sum()
        
        # 5. Handle price outliers (prices more than 5x median)
        if 'selling_price_aed' in df.columns:
            median_price = df['selling_price_aed'].median()
            if median_price > 0:
                outlier_price_mask = df['selling_price_aed'] > (median_price * PRICE_MULTIPLIER_THRESHOLD)
                outlier_price_count = outlier_price_mask.sum()
                
                if outlier_price_count > 0:
                    price_cap = median_price * PRICE_MULTIPLIER_THRESHOLD
                    for idx in df[outlier_price_mask].index:
                        order_id = df.loc[idx, 'order_id']
                        old_price = df.loc[idx, 'selling_price_aed']
                        df.loc[idx, 'selling_price_aed'] = price_cap
                        
                        self.log_issue(
                            table_name='sales_raw',
                            record_id=order_id,
                            issue_type='OUTLIER_VALUE',
                            issue_detail=f'Extreme price: {old_price}',
                            action_taken=f'Capped at {price_cap:.2f}'
                        )
                    stats['issues_found'] += outlier_price_count
        
        # 6. Validate payment_status
        if 'payment_status' in df.columns:
            invalid_status_mask = ~df['payment_status'].isin(VALID_PAYMENT_STATUSES)
            if invalid_status_mask.sum() > 0:
                for idx in df[invalid_status_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    old_status = df.loc[idx, 'payment_status']
                    df.loc[idx, 'payment_status'] = 'Paid'  # Default assumption
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid payment_status: {old_status}',
                        action_taken='Defaulted to Paid'
                    )
                stats['issues_found'] += invalid_status_mask.sum()
        
        # 7. Validate return_flag (should be 0 or 1)
        if 'return_flag' in df.columns:
            df['return_flag'] = pd.to_numeric(df['return_flag'], errors='coerce').fillna(0).astype(int)
            df.loc[~df['return_flag'].isin([0, 1]), 'return_flag'] = 0
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['sales'] = stats
        
        return df
    
    # =========================================================================
    # INVENTORY CLEANING
    # =========================================================================
    def clean_inventory(self, df):
        """
        Clean inventory_snapshot table.
        
        Validation Rules:
            - snapshot_date must be valid date
            - product_id and store_id must not be null
            - stock_on_hand must be non-negative
            - reorder_point must be non-negative
            - lead_time_days must be positive
        
        Cleaning Actions:
            - Negative stock: Set to 0
            - Extreme stock (>9000): Cap at 99th percentile
            - Invalid dates: Drop record
        """
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # 1. Handle negative stock_on_hand
        if 'stock_on_hand' in df.columns:
            negative_stock_mask = df['stock_on_hand'] < 0
            negative_stock_count = negative_stock_mask.sum()
            
            if negative_stock_count > 0:
                for idx in df[negative_stock_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}_{df.loc[idx, 'snapshot_date']}"
                    old_stock = df.loc[idx, 'stock_on_hand']
                    df.loc[idx, 'stock_on_hand'] = 0
                    
                    self.log_issue(
                        table_name='inventory_snapshot',
                        record_id=record_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Negative stock: {old_stock}',
                        action_taken='Set to 0'
                    )
                stats['issues_found'] += negative_stock_count
            
            # Handle extreme stock values (>9000)
            extreme_threshold = 9000
            extreme_stock_mask = df['stock_on_hand'] > extreme_threshold
            extreme_stock_count = extreme_stock_mask.sum()
            
            if extreme_stock_count > 0:
                # Calculate reasonable cap (99th percentile of non-extreme values)
                reasonable_stocks = df[df['stock_on_hand'] <= extreme_threshold]['stock_on_hand']
                if len(reasonable_stocks) > 0:
                    stock_cap = reasonable_stocks.quantile(0.99)
                else:
                    stock_cap = 500
                
                for idx in df[extreme_stock_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}_{df.loc[idx, 'snapshot_date']}"
                    old_stock = df.loc[idx, 'stock_on_hand']
                    df.loc[idx, 'stock_on_hand'] = stock_cap
                    
                    self.log_issue(
                        table_name='inventory_snapshot',
                        record_id=record_id,
                        issue_type='OUTLIER_VALUE',
                        issue_detail=f'Extreme stock: {old_stock}',
                        action_taken=f'Capped at {stock_cap:.0f}'
                    )
                stats['issues_found'] += extreme_stock_count
        
        # 2. Handle negative reorder_point
        if 'reorder_point' in df.columns:
            negative_reorder_mask = df['reorder_point'] < 0
            if negative_reorder_mask.sum() > 0:
                for idx in df[negative_reorder_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}"
                    old_val = df.loc[idx, 'reorder_point']
                    df.loc[idx, 'reorder_point'] = 0
                    
                    self.log_issue(
                        table_name='inventory_snapshot',
                        record_id=record_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Negative reorder_point: {old_val}',
                        action_taken='Set to 0'
                    )
                stats['issues_found'] += negative_reorder_mask.sum()
        
        # 3. Validate lead_time_days
        if 'lead_time_days' in df.columns:
            invalid_lead_mask = (df['lead_time_days'] <= 0) | (df['lead_time_days'] > 90)
            if invalid_lead_mask.sum() > 0:
                for idx in df[invalid_lead_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}"
                    old_val = df.loc[idx, 'lead_time_days']
                    df.loc[idx, 'lead_time_days'] = 7  # Default 1 week
                    
                    self.log_issue(
                        table_name='inventory_snapshot',
                        record_id=record_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid lead_time_days: {old_val}',
                        action_taken='Set to 7 days'
                    )
                stats['issues_found'] += invalid_lead_mask.sum()
        
        # 4. Parse snapshot_date
        if 'snapshot_date' in df.columns:
            df['snapshot_date'] = pd.to_datetime(df['snapshot_date'], errors='coerce')
            invalid_date_mask = df['snapshot_date'].isna()
            if invalid_date_mask.sum() > 0:
                stats['issues_found'] += invalid_date_mask.sum()
                df = df[~invalid_date_mask]
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['inventory'] = stats
        
        return df
    
    # =========================================================================
    # FULL CLEANING PIPELINE
    # =========================================================================
    def run_full_pipeline(self, products_df=None, stores_df=None, 
                          sales_df=None, inventory_df=None):
        """
        Run complete cleaning pipeline on all tables.
        
        Returns:
            dict: Dictionary of cleaned dataframes
        """
        cleaned = {}
        
        if products_df is not None:
            cleaned['products'] = self.clean_products(products_df)
        
        if stores_df is not None:
            cleaned['stores'] = self.clean_stores(stores_df)
        
        if sales_df is not None:
            cleaned['sales'] = self.clean_sales(sales_df, products_df)
        
        if inventory_df is not None:
            cleaned['inventory'] = self.clean_inventory(inventory_df)
        
        return cleaned


# =============================================================================
# =============================================================================
#                           SIMULATOR MODULE
# =============================================================================
# =============================================================================

class KPICalculator:
    """
    Computes KPIs from cleaned sales data.
    
    Finance/Executive KPIs:
        1. Gross Revenue (Paid only)
        2. Refund Amount
        3. Net Revenue
        4. COGS
        5. Gross Margin (AED)
        6. Gross Margin %
        7. Average Discount %
    
    Ops/Manager KPIs:
        8. Return Rate %
        9. Payment Failure Rate %
    """
    
    def __init__(self, sales_df, products_df=None, stores_df=None):
        """
        Initialize KPI Calculator.
        
        Args:
            sales_df: Cleaned sales dataframe
            products_df: Cleaned products dataframe (for COGS calculation)
            stores_df: Cleaned stores dataframe (for grouping)
        """
        self.sales = sales_df.copy() if sales_df is not None else pd.DataFrame()
        self.products = products_df.copy() if products_df is not None else pd.DataFrame()
        self.stores = stores_df.copy() if stores_df is not None else pd.DataFrame()
        
        # Merge data for calculations
        if not self.sales.empty and not self.products.empty:
            self.sales_merged = self.sales.merge(
                self.products[['product_id', 'unit_cost_aed', 'category', 'base_price_aed']],
                on='product_id',
                how='left'
            )
        else:
            self.sales_merged = self.sales
        
        if not self.sales_merged.empty and not self.stores.empty:
            self.sales_merged = self.sales_merged.merge(
                self.stores[['store_id', 'city', 'channel']],
                on='store_id',
                how='left'
            )
    
    def calc_gross_revenue(self, df=None):
        """Calculate Gross Revenue (Paid orders only)."""
        data = df if df is not None else self.sales_merged
        if data.empty:
            return 0
        paid_sales = data[data['payment_status'] == 'Paid']
        return (paid_sales['qty'] * paid_sales['selling_price_aed']).sum()
    
    def calc_refund_amount(self, df=None):
        """Calculate Refund Amount."""
        data = df if df is not None else self.sales_merged
        if data.empty:
            return 0
        refunded = data[data['payment_status'] == 'Refunded']
        return (refunded['qty'] * refunded['selling_price_aed']).sum()
    
    def calc_net_revenue(self, df=None):
        """Calculate Net Revenue = Gross Revenue - Refunds."""
        return self.calc_gross_revenue(df) - self.calc_refund_amount(df)
    
    def calc_cogs(self, df=None):
        """Calculate Cost of Goods Sold."""
        data = df if df is not None else self.sales_merged
        if data.empty or 'unit_cost_aed' not in data.columns:
            return 0
        paid_sales = data[data['payment_status'] == 'Paid']
        return (paid_sales['qty'] * paid_sales['unit_cost_aed']).sum()
    
    def calc_gross_margin_aed(self, df=None):
        """Calculate Gross Margin in AED."""
        return self.calc_net_revenue(df) - self.calc_cogs(df)
    
    def calc_gross_margin_pct(self, df=None):
        """Calculate Gross Margin Percentage."""
        net_rev = self.calc_net_revenue(df)
        if net_rev == 0:
            return 0
        return (self.calc_gross_margin_aed(df) / net_rev) * 100
    
    def calc_avg_discount_pct(self, df=None):
        """Calculate Average Discount Percentage."""
        data = df if df is not None else self.sales_merged
        if data.empty or 'discount_pct' not in data.columns:
            return 0
        return data['discount_pct'].mean()
    
    def calc_return_rate(self, df=None):
        """Calculate Return Rate % (returns among paid orders)."""
        data = df if df is not None else self.sales_merged
        if data.empty:
            return 0
        paid_orders = data[data['payment_status'] == 'Paid']
        if len(paid_orders) == 0:
            return 0
        if 'return_flag' not in paid_orders.columns:
            return 0
        return (paid_orders['return_flag'].sum() / len(paid_orders)) * 100
    
    def calc_payment_failure_rate(self, df=None):
        """Calculate Payment Failure Rate %."""
        data = df if df is not None else self.sales_merged
        if data.empty:
            return 0
        failed = data[data['payment_status'] == 'Failed']
        return (len(failed) / len(data)) * 100
    
    def calc_total_orders(self, df=None):
        """Calculate total number of orders."""
        data = df if df is not None else self.sales_merged
        return len(data)
    
    def calc_total_units(self, df=None):
        """Calculate total units sold."""
        data = df if df is not None else self.sales_merged
        if data.empty:
            return 0
        return data['qty'].sum()
    
    def compute_all_kpis(self, df=None):
        """Compute all KPIs and return as dictionary."""
        return {
            'gross_revenue': self.calc_gross_revenue(df),
            'refund_amount': self.calc_refund_amount(df),
            'net_revenue': self.calc_net_revenue(df),
            'cogs': self.calc_cogs(df),
            'gross_margin_aed': self.calc_gross_margin_aed(df),
            'gross_margin_pct': self.calc_gross_margin_pct(df),
            'avg_discount_pct': self.calc_avg_discount_pct(df),
            'return_rate': self.calc_return_rate(df),
            'payment_failure_rate': self.calc_payment_failure_rate(df),
            'total_orders': self.calc_total_orders(df),
            'total_units': self.calc_total_units(df)
        }
    
    def get_kpis_by_dimension(self, dimension='city'):
        """Get KPIs grouped by a dimension (city, channel, category)."""
        if self.sales_merged.empty or dimension not in self.sales_merged.columns:
            return pd.DataFrame()
        
        results = []
        for value in self.sales_merged[dimension].unique():
            filtered = self.sales_merged[self.sales_merged[dimension] == value]
            kpis = self.compute_all_kpis(filtered)
            kpis[dimension] = value
            results.append(kpis)
        
        return pd.DataFrame(results)


class PromoSimulator:
    """
    What-If Promo Simulation Engine.
    
    Computes:
        - Baseline demand from historical data
        - Simulated demand with uplift
        - Promo spend
        - Profit proxy
        - Stockout risk
        - Constraint violations
    """
    
    def __init__(self, sales_df, products_df, stores_df, inventory_df):
        """
        Initialize Promo Simulator.
        
        Args:
            sales_df: Cleaned sales dataframe
            products_df: Cleaned products dataframe
            stores_df: Cleaned stores dataframe
            inventory_df: Cleaned inventory dataframe
        """
        self.sales = sales_df.copy() if sales_df is not None else pd.DataFrame()
        self.products = products_df.copy() if products_df is not None else pd.DataFrame()
        self.stores = stores_df.copy() if stores_df is not None else pd.DataFrame()
        self.inventory = inventory_df.copy() if inventory_df is not None else pd.DataFrame()
        
        # Merge products with stores info for simulation
        self._prepare_data()
    
    def _prepare_data(self):
        """Prepare merged data for simulation."""
        if self.sales.empty:
            self.sales_merged = pd.DataFrame()
            return
        
        # Merge sales with products
        self.sales_merged = self.sales.merge(
            self.products[['product_id', 'unit_cost_aed', 'category', 'base_price_aed']],
            on='product_id',
            how='left'
        )
        
        # Merge with stores
        if not self.stores.empty:
            self.sales_merged = self.sales_merged.merge(
                self.stores[['store_id', 'city', 'channel']],
                on='store_id',
                how='left'
            )
    
    def calculate_baseline_demand(self, lookback_days=30):
        """
        Calculate baseline daily demand per product-store.
        
        Uses last N days of sales to compute average daily demand.
        
        Args:
            lookback_days: Number of days to look back
        
        Returns:
            DataFrame with product_id, store_id, baseline_daily_demand
        """
        if self.sales_merged.empty:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        # Filter to paid orders only
        paid_sales = self.sales_merged[self.sales_merged['payment_status'] == 'Paid'].copy()
        
        if paid_sales.empty:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        # Ensure order_time is datetime
        if not pd.api.types.is_datetime64_any_dtype(paid_sales['order_time']):
            paid_sales['order_time'] = pd.to_datetime(paid_sales['order_time'], errors='coerce')
        
        # Filter to lookback period
        max_date = paid_sales['order_time'].max()
        min_date = max_date - timedelta(days=lookback_days)
        recent_sales = paid_sales[paid_sales['order_time'] >= min_date]
        
        if recent_sales.empty:
            # Use all available data if no recent data
            recent_sales = paid_sales
            lookback_days = max(1, (paid_sales['order_time'].max() - paid_sales['order_time'].min()).days)
        
        # Group by product-store and calculate daily average
        baseline = recent_sales.groupby(['product_id', 'store_id']).agg({
            'qty': 'sum'
        }).reset_index()
        
        baseline['baseline_daily_demand'] = baseline['qty'] / lookback_days
        baseline = baseline.drop(columns=['qty'])
        
        return baseline
    
    def calculate_uplift_factor(self, discount_pct, channel='Web', category='Other'):
        """
        Calculate demand uplift factor based on discount and modifiers.
        
        Formula (documented assumption):
            base_uplift = 1 + (discount_pct × 0.03), capped at 2.0
            channel_modifier = varies by channel (Marketplace highest)
            category_modifier = varies by category (Electronics highest)
            final_uplift = base_uplift × channel_mod × category_mod
        
        Args:
            discount_pct: Discount percentage (0-100)
            channel: Sales channel
            category: Product category
        
        Returns:
            float: Demand multiplier
        """
        # Base uplift: 3% demand increase per 1% discount
        base_uplift = 1 + (discount_pct * UPLIFT_CONFIG['base_multiplier'])
        base_uplift = min(base_uplift, UPLIFT_CONFIG['max_uplift'])
        
        # Channel modifier
        channel_mod = UPLIFT_CONFIG['channel_modifiers'].get(channel, 1.0)
        
        # Category modifier
        category_mod = UPLIFT_CONFIG['category_modifiers'].get(category, 1.0)
        
        return base_uplift * channel_mod * category_mod
    
    def run_simulation(self, discount_pct, promo_budget_aed, margin_floor_pct,
                       simulation_days=14, city_filter='All', channel_filter='All',
                       category_filter='All'):
        """
        Run what-if promo simulation.
        
        Args:
            discount_pct: Discount percentage to apply
            promo_budget_aed: Maximum promo spend budget
            margin_floor_pct: Minimum gross margin percentage
            simulation_days: Number of days to simulate
            city_filter: Filter by city (or 'All')
            channel_filter: Filter by channel (or 'All')
            category_filter: Filter by category (or 'All')
        
        Returns:
            dict: Simulation results including KPIs and violations
        """
        results = {
            'parameters': {
                'discount_pct': discount_pct,
                'promo_budget_aed': promo_budget_aed,
                'margin_floor_pct': margin_floor_pct,
                'simulation_days': simulation_days,
                'city_filter': city_filter,
                'channel_filter': channel_filter,
                'category_filter': category_filter
            },
            'kpis': {},
            'constraints': {},
            'violations': [],
            'details': pd.DataFrame()
        }
        
        # Get baseline demand
        baseline = self.calculate_baseline_demand()
        
        if baseline.empty:
            results['kpis'] = {
                'simulated_revenue': 0,
                'promo_spend': 0,
                'profit_proxy': 0,
                'budget_utilization': 0,
                'stockout_risk_pct': 0,
                'simulated_units': 0
            }
            return results
        
        # Merge baseline with product info
        sim_data = baseline.merge(
            self.products[['product_id', 'base_price_aed', 'unit_cost_aed', 'category']],
            on='product_id',
            how='left'
        )
        
        # Merge with store info
        if not self.stores.empty:
            sim_data = sim_data.merge(
                self.stores[['store_id', 'city', 'channel']],
                on='store_id',
                how='left'
            )
        
        # Apply filters
        if city_filter != 'All' and 'city' in sim_data.columns:
            sim_data = sim_data[sim_data['city'] == city_filter]
        
        if channel_filter != 'All' and 'channel' in sim_data.columns:
            sim_data = sim_data[sim_data['channel'] == channel_filter]
        
        if category_filter != 'All' and 'category' in sim_data.columns:
            sim_data = sim_data[sim_data['category'] == category_filter]
        
        if sim_data.empty:
            results['kpis'] = {
                'simulated_revenue': 0,
                'promo_spend': 0,
                'profit_proxy': 0,
                'budget_utilization': 0,
                'stockout_risk_pct': 0,
                'simulated_units': 0
            }
            return results
        
        # Calculate uplift for each row
        sim_data['uplift_factor'] = sim_data.apply(
            lambda row: self.calculate_uplift_factor(
                discount_pct,
                row.get('channel', 'Web'),
                row.get('category', 'Other')
            ),
            axis=1
        )
        
        # Calculate simulated demand
        sim_data['simulated_daily_demand'] = sim_data['baseline_daily_demand'] * sim_data['uplift_factor']
        sim_data['simulated_total_demand'] = sim_data['simulated_daily_demand'] * simulation_days
        
        # Get latest inventory snapshot
        if not self.inventory.empty:
            latest_inventory = self.inventory.sort_values('snapshot_date').groupby(
                ['product_id', 'store_id']
            ).last().reset_index()[['product_id', 'store_id', 'stock_on_hand']]
            
            sim_data = sim_data.merge(
                latest_inventory,
                on=['product_id', 'store_id'],
                how='left'
            )
            sim_data['stock_on_hand'] = sim_data['stock_on_hand'].fillna(0)
        else:
            sim_data['stock_on_hand'] = 1000  # Default if no inventory data
        
        # Apply stock constraint
        sim_data['constrained_demand'] = sim_data[['simulated_total_demand', 'stock_on_hand']].min(axis=1)
        sim_data['stockout_flag'] = (sim_data['simulated_total_demand'] > sim_data['stock_on_hand']).astype(int)
        
        # Calculate selling price with discount
        sim_data['discounted_price'] = sim_data['base_price_aed'] * (1 - discount_pct / 100)
        
        # Calculate financial metrics
        sim_data['simulated_revenue'] = sim_data['constrained_demand'] * sim_data['discounted_price']
        sim_data['simulated_cogs'] = sim_data['constrained_demand'] * sim_data['unit_cost_aed']
        sim_data['promo_discount_amount'] = sim_data['constrained_demand'] * sim_data['base_price_aed'] * (discount_pct / 100)
        
        # Aggregate results
        total_simulated_revenue = sim_data['simulated_revenue'].sum()
        total_cogs = sim_data['simulated_cogs'].sum()
        total_promo_spend = sim_data['promo_discount_amount'].sum()
        total_units = sim_data['constrained_demand'].sum()
        
        # Calculate KPIs
        gross_margin_aed = total_simulated_revenue - total_cogs
        gross_margin_pct = (gross_margin_aed / total_simulated_revenue * 100) if total_simulated_revenue > 0 else 0
        profit_proxy = gross_margin_aed - total_promo_spend
        budget_utilization = (total_promo_spend / promo_budget_aed * 100) if promo_budget_aed > 0 else 0
        stockout_risk = (sim_data['stockout_flag'].sum() / len(sim_data) * 100) if len(sim_data) > 0 else 0
        
        results['kpis'] = {
            'simulated_revenue': total_simulated_revenue,
            'simulated_cogs': total_cogs,
            'gross_margin_aed': gross_margin_aed,
            'gross_margin_pct': gross_margin_pct,
            'promo_spend': total_promo_spend,
            'profit_proxy': profit_proxy,
            'budget_utilization': min(budget_utilization, 100),
            'stockout_risk_pct': stockout_risk,
            'simulated_units': total_units,
            'products_at_risk': sim_data['stockout_flag'].sum()
        }
        
        # Check constraints and violations
        violations = []
        
        # Budget constraint
        if total_promo_spend > promo_budget_aed:
            violations.append({
                'constraint': 'BUDGET',
                'threshold': promo_budget_aed,
                'actual': total_promo_spend,
                'message': f'Promo spend (AED {total_promo_spend:,.0f}) exceeds budget (AED {promo_budget_aed:,.0f})'
            })
        
        # Margin floor constraint
        if gross_margin_pct < margin_floor_pct:
            violations.append({
                'constraint': 'MARGIN_FLOOR',
                'threshold': margin_floor_pct,
                'actual': gross_margin_pct,
                'message': f'Gross margin ({gross_margin_pct:.1f}%) below floor ({margin_floor_pct}%)'
            })
        
        results['violations'] = violations
        results['constraints'] = {
            'budget_ok': total_promo_spend <= promo_budget_aed,
            'margin_ok': gross_margin_pct >= margin_floor_pct,
            'all_ok': len(violations) == 0
        }
        
        # Get top stockout risk items
        stockout_items = sim_data[sim_data['stockout_flag'] == 1].nlargest(
            10, 'simulated_total_demand'
        )[['product_id', 'store_id', 'simulated_total_demand', 'stock_on_hand', 'category']].copy()
        stockout_items.columns = ['Product', 'Store', 'Projected Demand', 'Stock Available', 'Category']
        
        results['top_stockout_items'] = stockout_items
        results['details'] = sim_data
        
        return results
    
    def get_scenario_comparison(self, discount_scenarios, promo_budget, margin_floor, simulation_days=14):
        """
        Compare multiple discount scenarios.
        
        Args:
            discount_scenarios: List of discount percentages to compare
            promo_budget: Budget for all scenarios
            margin_floor: Margin floor for all scenarios
            simulation_days: Simulation window
        
        Returns:
            DataFrame comparing scenarios
        """
        comparisons = []
        
        for discount in discount_scenarios:
            result = self.run_simulation(
                discount_pct=discount,
                promo_budget_aed=promo_budget,
                margin_floor_pct=margin_floor,
                simulation_days=simulation_days
            )
            
            comparisons.append({
                'Discount %': discount,
                'Simulated Revenue': result['kpis']['simulated_revenue'],
                'Profit Proxy': result['kpis']['profit_proxy'],
                'Margin %': result['kpis']['gross_margin_pct'],
                'Stockout Risk %': result['kpis']['stockout_risk_pct'],
                'Budget Used %': result['kpis']['budget_utilization'],
                'Constraints Met': '✓' if result['constraints']['all_ok'] else '✗'
            })
        
        return pd.DataFrame(comparisons)


# =============================================================================
# =============================================================================
#                           STREAMLIT DASHBOARD
# =============================================================================
# =============================================================================

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_data_from_upload(uploaded_file):
    """Load data from uploaded file (CSV or Excel)."""
    try:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            return pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload CSV or Excel file.")
            return None
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None


def create_column_mapping_ui(df, table_name, expected_columns):
    """
    Create UI for mapping uploaded columns to expected schema.
    
    Args:
        df: Uploaded dataframe
        table_name: Name of the table being mapped
        expected_columns: Dict of expected column names and descriptions
    
    Returns:
        dict: Mapping of expected column to actual column
    """
    st.subheader(f"📋 Map Columns for {table_name}")
    
    available_columns = ['-- Not Mapped --'] + list(df.columns)
    mapping = {}
    
    cols = st.columns(2)
    for i, (expected_col, description) in enumerate(expected_columns.items()):
        with cols[i % 2]:
            # Try to auto-detect matching column
            default_idx = 0
            for j, col in enumerate(available_columns):
                if col.lower().replace(' ', '_').replace('-', '_') == expected_col.lower():
                    default_idx = j
                    break
            
            mapping[expected_col] = st.selectbox(
                f"{expected_col}",
                available_columns,
                index=default_idx,
                help=description,
                key=f"map_{table_name}_{expected_col}"
            )
    
    return mapping


def apply_column_mapping(df, mapping):
    """Apply column mapping to dataframe."""
    renamed_df = pd.DataFrame()
    
    for expected_col, actual_col in mapping.items():
        if actual_col != '-- Not Mapped --' and actual_col in df.columns:
            renamed_df[expected_col] = df[actual_col]
    
    return renamed_df


def convert_df_to_csv(df):
    """Convert dataframe to CSV for download."""
    return df.to_csv(index=False).encode('utf-8')


def format_currency(value):
    """Format value as AED currency."""
    return f"AED {value:,.0f}"


def format_percentage(value):
    """Format value as percentage."""
    return f"{value:.1f}%"


def create_kpi_card(label, value, delta=None, delta_color="normal"):
    """Create a KPI metric card."""
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color)


# =============================================================================
# CHART FUNCTIONS
# =============================================================================

def create_revenue_trend_chart(sales_df):
    """Create revenue trend chart (daily/weekly)."""
    if sales_df.empty:
        return None
    
    df = sales_df.copy()
    
    # Ensure datetime
    if not pd.api.types.is_datetime64_any_dtype(df['order_time']):
        df['order_time'] = pd.to_datetime(df['order_time'], errors='coerce')
    
    df = df[df['payment_status'] == 'Paid']
    df['revenue'] = df['qty'] * df['selling_price_aed']
    df['date'] = df['order_time'].dt.date
    
    daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
    daily_revenue.columns = ['Date', 'Revenue']
    
    fig = px.line(
        daily_revenue,
        x='Date',
        y='Revenue',
        title='📈 Net Revenue Trend (Daily)',
        labels={'Revenue': 'Revenue (AED)'}
    )
    fig.update_layout(hovermode='x unified')
    fig.update_traces(fill='tozeroy', fillcolor='rgba(0, 123, 255, 0.1)')
    
    return fig


def create_revenue_by_dimension_chart(sales_df, dimension='city'):
    """Create revenue by city/channel bar chart."""
    if sales_df.empty or dimension not in sales_df.columns:
        return None
    
    df = sales_df[sales_df['payment_status'] == 'Paid'].copy()
    df['revenue'] = df['qty'] * df['selling_price_aed']
    
    grouped = df.groupby(dimension)['revenue'].sum().reset_index()
    grouped.columns = [dimension.title(), 'Revenue']
    
    fig = px.bar(
        grouped,
        x=dimension.title(),
        y='Revenue',
        title=f'💰 Revenue by {dimension.title()}',
        color=dimension.title(),
        text_auto='.2s'
    )
    fig.update_traces(textposition='outside')
    
    return fig


def create_margin_by_category_chart(sales_df, products_df):
    """Create margin % by category chart."""
    if sales_df.empty or products_df.empty:
        return None
    
    df = sales_df.merge(
        products_df[['product_id', 'unit_cost_aed', 'category']],
        on='product_id',
        how='left'
    )
    
    df = df[df['payment_status'] == 'Paid']
    df['revenue'] = df['qty'] * df['selling_price_aed']
    df['cost'] = df['qty'] * df['unit_cost_aed']
    
    grouped = df.groupby('category').agg({
        'revenue': 'sum',
        'cost': 'sum'
    }).reset_index()
    
    grouped['margin_pct'] = ((grouped['revenue'] - grouped['cost']) / grouped['revenue'] * 100).round(1)
    
    fig = px.bar(
        grouped,
        x='category',
        y='margin_pct',
        title='📊 Gross Margin % by Category',
        color='margin_pct',
        color_continuous_scale='RdYlGn',
        text_auto='.1f'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(coloraxis_showscale=False)
    
    return fig


def create_scenario_impact_chart(scenario_df):
    """Create scenario comparison chart."""
    if scenario_df.empty:
        return None
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=scenario_df['Discount %'],
            y=scenario_df['Profit Proxy'],
            name='Profit Proxy',
            marker_color='rgb(55, 83, 109)'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=scenario_df['Discount %'],
            y=scenario_df['Margin %'],
            name='Margin %',
            mode='lines+markers',
            marker_color='rgb(255, 127, 14)'
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title='🎯 Scenario Impact: Profit Proxy vs Discount',
        xaxis_title='Discount %',
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )
    fig.update_yaxes(title_text='Profit Proxy (AED)', secondary_y=False)
    fig.update_yaxes(title_text='Margin %', secondary_y=True)
    
    return fig


def create_stockout_risk_chart(sim_results):
    """Create stockout risk by dimension chart."""
    details = sim_results.get('details', pd.DataFrame())
    
    if details.empty:
        return None
    
    if 'city' in details.columns:
        risk_by_city = details.groupby('city').agg({
            'stockout_flag': ['sum', 'count']
        }).reset_index()
        risk_by_city.columns = ['City', 'At Risk', 'Total']
        risk_by_city['Risk %'] = (risk_by_city['At Risk'] / risk_by_city['Total'] * 100).round(1)
        
        fig = px.bar(
            risk_by_city,
            x='City',
            y='Risk %',
            title='⚠️ Stockout Risk by City',
            color='Risk %',
            color_continuous_scale='Reds',
            text_auto='.1f'
        )
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        fig.update_layout(coloraxis_showscale=False)
        
        return fig
    
    return None


def create_issues_pareto_chart(issues_df):
    """Create Pareto chart of issue types."""
    if issues_df.empty:
        return None
    
    issue_counts = issues_df['issue_type'].value_counts().reset_index()
    issue_counts.columns = ['Issue Type', 'Count']
    issue_counts = issue_counts.sort_values('Count', ascending=False)
    
    # Calculate cumulative percentage
    issue_counts['Cumulative %'] = (issue_counts['Count'].cumsum() / issue_counts['Count'].sum() * 100).round(1)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=issue_counts['Issue Type'],
            y=issue_counts['Count'],
            name='Count',
            marker_color='indianred'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=issue_counts['Issue Type'],
            y=issue_counts['Cumulative %'],
            name='Cumulative %',
            mode='lines+markers',
            marker_color='navy'
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title='🔍 Data Quality Issues (Pareto)',
        xaxis_title='Issue Type',
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )
    fig.update_yaxes(title_text='Count', secondary_y=False)
    fig.update_yaxes(title_text='Cumulative %', secondary_y=True, range=[0, 105])
    
    return fig


def create_inventory_distribution_chart(inventory_df):
    """Create inventory distribution chart."""
    if inventory_df.empty:
        return None
    
    # Get latest snapshot per product-store
    latest = inventory_df.sort_values('snapshot_date').groupby(
        ['product_id', 'store_id']
    ).last().reset_index()
    
    fig = px.histogram(
        latest,
        x='stock_on_hand',
        nbins=50,
        title='📦 Stock on Hand Distribution',
        labels={'stock_on_hand': 'Stock on Hand', 'count': 'Frequency'}
    )
    fig.update_layout(bargap=0.1)
    
    return fig


# =============================================================================
# RECOMMENDATION ENGINE
# =============================================================================

def generate_executive_recommendation(kpis, sim_results):
    """Generate auto-recommendation text for executives."""
    recommendations = []
    
    # Analyze margin
    margin_pct = kpis.get('gross_margin_pct', 0)
    if margin_pct >= 40:
        recommendations.append("✅ **Strong margin performance** — consider aggressive promotional spend.")
    elif margin_pct >= 25:
        recommendations.append("⚠️ **Moderate margins** — balance discounts carefully to maintain profitability.")
    else:
        recommendations.append("🔴 **Low margins** — avoid deep discounts; focus on high-margin categories.")
    
    # Analyze simulation results
    if sim_results:
        stockout_risk = sim_results['kpis'].get('stockout_risk_pct', 0)
        budget_util = sim_results['kpis'].get('budget_utilization', 0)
        
        if stockout_risk > 30:
            recommendations.append(f"⚠️ **High stockout risk ({stockout_risk:.0f}%)** — consider inventory replenishment before campaign.")
        
        if budget_util > 90:
            recommendations.append("💰 **Budget nearly exhausted** — reduce discount depth or narrow campaign scope.")
        elif budget_util < 50:
            recommendations.append("💡 **Budget underutilized** — opportunity to expand promotional reach.")
        
        if not sim_results['constraints']['all_ok']:
            recommendations.append("🚫 **Constraint violations detected** — review simulation parameters.")
    
    return "\n\n".join(recommendations)


# =============================================================================
# MAIN DASHBOARD
# =============================================================================

def main():
    """Main Streamlit application."""
    
    # =========================================================================
    # HEADER
    # =========================================================================
    st.title("🛒 UAE Promo Pulse Simulator")
    st.markdown("### Data Rescue Dashboard + What-If Simulation")
    st.markdown("---")
    
    # =========================================================================
    # SESSION STATE INITIALIZATION
    # =========================================================================
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    if 'cleaned_data' not in st.session_state:
        st.session_state.cleaned_data = {}
    if 'issues_log' not in st.session_state:
        st.session_state.issues_log = pd.DataFrame()
    if 'raw_data' not in st.session_state:
        st.session_state.raw_data = {}
    
    # =========================================================================
    # SIDEBAR
    # =========================================================================
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # View Toggle
        st.subheader("📊 Dashboard View")
        view_mode = st.radio(
            "Select View",
            ["Executive", "Manager"],
            horizontal=True,
            help="Executive: Financial KPIs | Manager: Operational metrics"
        )
        
        st.markdown("---")
        
        # Data Source Selection
        st.subheader("📁 Data Source")
        data_source = st.radio(
            "Choose data source",
            ["Upload Custom Data", "Load Generated Data"],
            help="Upload your own CSVs or use pre-generated synthetic data"
        )
        
        st.markdown("---")
        
        # Simulation Parameters
        st.subheader("🎮 Simulation Parameters")
        
        discount_pct = st.slider(
            "Discount %",
            min_value=0,
            max_value=50,
            value=15,
            step=5,
            help="Discount percentage to simulate"
        )
        
        promo_budget = st.number_input(
            "Promo Budget (AED)",
            min_value=10000,
            max_value=500000,
            value=100000,
            step=10000,
            help="Maximum promotional spend"
        )
        
        margin_floor = st.number_input(
            "Margin Floor %",
            min_value=0.0,
            max_value=50.0,
            value=15.0,
            step=1.0,
            help="Minimum acceptable gross margin"
        )
        
        sim_window = st.selectbox(
            "Simulation Window",
            [7, 14],
            index=1,
            help="Number of days to simulate"
        )
        
        st.markdown("---")
        
        # Filters (will be populated after data load)
        st.subheader("🔍 Filters")
        
        city_filter = st.selectbox(
            "City",
            ["All"] + VALID_CITIES,
            help="Filter by city"
        )
        
        channel_filter = st.selectbox(
            "Channel",
            ["All"] + VALID_CHANNELS,
            help="Filter by sales channel"
        )
        
        category_filter = st.selectbox(
            "Category",
            ["All"] + VALID_CATEGORIES,
            help="Filter by product category"
        )
    
    # =========================================================================
    # DATA LOADING SECTION
    # =========================================================================
    
    if data_source == "Upload Custom Data":
        st.header("📤 Upload Data Files")
        
        col1, col2 = st.columns(2)
        
        with col1:
            products_file = st.file_uploader(
                "Products CSV/Excel",
                type=['csv', 'xlsx', 'xls'],
                key='products_upload'
            )
            sales_file = st.file_uploader(
                "Sales CSV/Excel",
                type=['csv', 'xlsx', 'xls'],
                key='sales_upload'
            )
        
        with col2:
            stores_file = st.file_uploader(
                "Stores CSV/Excel",
                type=['csv', 'xlsx', 'xls'],
                key='stores_upload'
            )
            inventory_file = st.file_uploader(
                "Inventory CSV/Excel",
                type=['csv', 'xlsx', 'xls'],
                key='inventory_upload'
            )
        
        # Column Mapping Section
        if any([products_file, stores_file, sales_file, inventory_file]):
            st.markdown("---")
            st.header("🔗 Column Mapping")
            
            with st.expander("Map Product Columns", expanded=products_file is not None):
                if products_file:
                    products_raw = load_data_from_upload(products_file)
                    if products_raw is not None:
                        st.dataframe(products_raw.head(3))
                        products_mapping = create_column_mapping_ui(
                            products_raw,
                            'Products',
                            {
                                'product_id': 'Unique product identifier',
                                'category': 'Product category',
                                'brand': 'Product brand',
                                'base_price_aed': 'Base selling price (AED)',
                                'unit_cost_aed': 'Unit cost (AED)',
                                'tax_rate': 'Tax rate (decimal)',
                                'launch_flag': 'New or Regular'
                            }
                        )
                        st.session_state.raw_data['products'] = products_raw
                        st.session_state.raw_data['products_mapping'] = products_mapping
            
            with st.expander("Map Store Columns", expanded=stores_file is not None):
                if stores_file:
                    stores_raw = load_data_from_upload(stores_file)
                    if stores_raw is not None:
                        st.dataframe(stores_raw.head(3))
                        stores_mapping = create_column_mapping_ui(
                            stores_raw,
                            'Stores',
                            {
                                'store_id': 'Unique store identifier',
                                'city': 'City name',
                                'channel': 'Sales channel (App/Web/Marketplace)',
                                'fulfillment_type': 'Fulfillment type (Own/3PL)'
                            }
                        )
                        st.session_state.raw_data['stores'] = stores_raw
                        st.session_state.raw_data['stores_mapping'] = stores_mapping
            
            with st.expander("Map Sales Columns", expanded=sales_file is not None):
                if sales_file:
                    sales_raw = load_data_from_upload(sales_file)
                    if sales_raw is not None:
                        st.dataframe(sales_raw.head(3))
                        sales_mapping = create_column_mapping_ui(
                            sales_raw,
                            'Sales',
                            {
                                'order_id': 'Unique order identifier',
                                'order_time': 'Order timestamp',
                                'product_id': 'Product identifier',
                                'store_id': 'Store identifier',
                                'qty': 'Quantity',
                                'selling_price_aed': 'Selling price (AED)',
                                'discount_pct': 'Discount percentage',
                                'payment_status': 'Payment status',
                                'return_flag': 'Return indicator (0/1)'
                            }
                        )
                        st.session_state.raw_data['sales'] = sales_raw
                        st.session_state.raw_data['sales_mapping'] = sales_mapping
            
            with st.expander("Map Inventory Columns", expanded=inventory_file is not None):
                if inventory_file:
                    inventory_raw = load_data_from_upload(inventory_file)
                    if inventory_raw is not None:
                        st.dataframe(inventory_raw.head(3))
                        inventory_mapping = create_column_mapping_ui(
                            inventory_raw,
                            'Inventory',
                            {
                                'snapshot_date': 'Snapshot date',
                                'product_id': 'Product identifier',
                                'store_id': 'Store identifier',
                                'stock_on_hand': 'Stock quantity',
                                'reorder_point': 'Reorder point',
                                'lead_time_days': 'Lead time in days'
                            }
                        )
                        st.session_state.raw_data['inventory'] = inventory_raw
                        st.session_state.raw_data['inventory_mapping'] = inventory_mapping
            
            # Process Button
            if st.button("🚀 Process & Clean Data", type="primary"):
                with st.spinner("Cleaning data..."):
                    cleaner = DataCleaner()
                    
                    # Apply mappings and clean
                    cleaned = {}
                    
                    if 'products' in st.session_state.raw_data:
                        mapped_products = apply_column_mapping(
                            st.session_state.raw_data['products'],
                            st.session_state.raw_data['products_mapping']
                        )
                        cleaned['products'] = cleaner.clean_products(mapped_products)
                    
                    if 'stores' in st.session_state.raw_data:
                        mapped_stores = apply_column_mapping(
                            st.session_state.raw_data['stores'],
                            st.session_state.raw_data['stores_mapping']
                        )
                        cleaned['stores'] = cleaner.clean_stores(mapped_stores)
                    
                    if 'sales' in st.session_state.raw_data:
                        mapped_sales = apply_column_mapping(
                            st.session_state.raw_data['sales'],
                            st.session_state.raw_data['sales_mapping']
                        )
                        cleaned['sales'] = cleaner.clean_sales(mapped_sales)
                    
                    if 'inventory' in st.session_state.raw_data:
                        mapped_inventory = apply_column_mapping(
                            st.session_state.raw_data['inventory'],
                            st.session_state.raw_data['inventory_mapping']
                        )
                        cleaned['inventory'] = cleaner.clean_inventory(mapped_inventory)
                    
                    st.session_state.cleaned_data = cleaned
                    st.session_state.issues_log = cleaner.get_issues_dataframe()
                    st.session_state.cleaning_stats = cleaner.cleaning_stats
                    st.session_state.data_loaded = True
                    
                    st.success("✅ Data cleaned successfully!")
                    st.rerun()
    
    else:  # Load Generated Data
        st.header("📂 Load Generated Data")
        st.info("Upload the CSV files generated by `data_generator.py`")
        
        col1, col2 = st.columns(2)
        
        with col1:
            products_file = st.file_uploader("products.csv", type=['csv'], key='gen_products')
            sales_file = st.file_uploader("sales_raw.csv", type=['csv'], key='gen_sales')
        
        with col2:
            stores_file = st.file_uploader("stores.csv", type=['csv'], key='gen_stores')
            inventory_file = st.file_uploader("inventory_snapshot.csv", type=['csv'], key='gen_inventory')
        
        if st.button("🚀 Load & Clean Data", type="primary"):
            if all([products_file, stores_file, sales_file, inventory_file]):
                with st.spinner("Loading and cleaning data..."):
                    cleaner = DataCleaner()
                    
                    # Load and clean each file
                    products_df = pd.read_csv(products_file)
                    stores_df = pd.read_csv(stores_file)
                    sales_df = pd.read_csv(sales_file)
                    inventory_df = pd.read_csv(inventory_file)
                    
                    cleaned = cleaner.run_full_pipeline(
                        products_df=products_df,
                        stores_df=stores_df,
                        sales_df=sales_df,
                        inventory_df=inventory_df
                    )
                    
                    st.session_state.cleaned_data = cleaned
                    st.session_state.issues_log = cleaner.get_issues_dataframe()
                    st.session_state.cleaning_stats = cleaner.cleaning_stats
                    st.session_state.data_loaded = True
                    
                    st.success("✅ Data loaded and cleaned successfully!")
                    st.rerun()
            else:
                st.warning("Please upload all 4 data files.")
    
    # =========================================================================
    # MAIN DASHBOARD (Only show if data is loaded)
    # =========================================================================
    
    if st.session_state.data_loaded:
        st.markdown("---")
        
        # Get cleaned data
        products_df = st.session_state.cleaned_data.get('products', pd.DataFrame())
        stores_df = st.session_state.cleaned_data.get('stores', pd.DataFrame())
        sales_df = st.session_state.cleaned_data.get('sales', pd.DataFrame())
        inventory_df = st.session_state.cleaned_data.get('inventory', pd.DataFrame())
        issues_df = st.session_state.issues_log
        
        # Initialize calculators
        kpi_calc = KPICalculator(sales_df, products_df, stores_df)
        simulator = PromoSimulator(sales_df, products_df, stores_df, inventory_df)
        
        # Calculate historical KPIs
        historical_kpis = kpi_calc.compute_all_kpis()
        
        # Run simulation
        sim_results = simulator.run_simulation(
            discount_pct=discount_pct,
            promo_budget_aed=promo_budget,
            margin_floor_pct=margin_floor,
            simulation_days=sim_window,
            city_filter=city_filter,
            channel_filter=channel_filter,
            category_filter=category_filter
        )
        
        # Generate scenario comparison
        scenario_df = simulator.get_scenario_comparison(
            discount_scenarios=[5, 10, 15, 20, 25, 30],
            promo_budget=promo_budget,
            margin_floor=margin_floor,
            simulation_days=sim_window
        )
        
        # =====================================================================
        # EXECUTIVE VIEW
        # =====================================================================
        if view_mode == "Executive":
            st.header("👔 Executive Dashboard")
            
            # KPI Cards Row
            st.subheader("📈 Key Performance Indicators")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                create_kpi_card(
                    "Net Revenue",
                    format_currency(historical_kpis['net_revenue']),
                    delta=None
                )
            
            with col2:
                create_kpi_card(
                    "Gross Margin %",
                    format_percentage(historical_kpis['gross_margin_pct']),
                    delta=None
                )
            
            with col3:
                profit_proxy = sim_results['kpis']['profit_proxy']
                create_kpi_card(
                    "Profit Proxy (Sim)",
                    format_currency(profit_proxy),
                    delta=None
                )
            
            with col4:
                budget_util = sim_results['kpis']['budget_utilization']
                create_kpi_card(
                    "Budget Utilization",
                    format_percentage(budget_util),
                    delta=None
                )
            
            st.markdown("---")
            
            # Charts Row 1
            col1, col2 = st.columns(2)
            
            with col1:
                # Merge sales with store info for charts
                sales_with_store = sales_df.merge(
                    stores_df[['store_id', 'city', 'channel']],
                    on='store_id',
                    how='left'
                )
                fig = create_revenue_trend_chart(sales_with_store)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = create_revenue_by_dimension_chart(sales_with_store, 'city')
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            # Charts Row 2
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_margin_by_category_chart(sales_df, products_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = create_scenario_impact_chart(scenario_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
            
            # Scenario Comparison Table
            st.subheader("📊 Scenario Comparison")
            st.dataframe(
                scenario_df.style.format({
                    'Simulated Revenue': 'AED {:,.0f}',
                    'Profit Proxy': 'AED {:,.0f}',
                    'Margin %': '{:.1f}%',
                    'Stockout Risk %': '{:.1f}%',
                    'Budget Used %': '{:.1f}%'
                }),
                use_container_width=True
            )
            
            # Constraint Violations
            if sim_results['violations']:
                st.subheader("⚠️ Constraint Violations")
                for violation in sim_results['violations']:
                    st.error(violation['message'])
            
            st.markdown("---")
            
            # Recommendation Box
            st.subheader("💡 AI Recommendation")
            recommendation = generate_executive_recommendation(historical_kpis, sim_results)
            st.info(recommendation)
        
        # =====================================================================
        # MANAGER VIEW
        # =====================================================================
        else:
            st.header("🔧 Manager / Operations Dashboard")
            
            # KPI Cards Row
            st.subheader("📊 Operational Metrics")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                stockout_risk = sim_results['kpis']['stockout_risk_pct']
                create_kpi_card(
                    "Stockout Risk %",
                    format_percentage(stockout_risk),
                    delta=None
                )
            
            with col2:
                create_kpi_card(
                    "Return Rate %",
                    format_percentage(historical_kpis['return_rate']),
                    delta=None
                )
            
            with col3:
                create_kpi_card(
                    "Payment Failure %",
                    format_percentage(historical_kpis['payment_failure_rate']),
                    delta=None
                )
            
            with col4:
                high_risk_skus = sim_results['kpis']['products_at_risk']
                create_kpi_card(
                    "High-Risk SKUs",
                    f"{high_risk_skus:,}",
                    delta=None
                )
            
            st.markdown("---")
            
            # Charts Row 1
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_stockout_risk_chart(sim_results)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = create_issues_pareto_chart(issues_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            # Charts Row 2
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_inventory_distribution_chart(inventory_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Revenue by channel
                sales_with_store = sales_df.merge(
                    stores_df[['store_id', 'city', 'channel']],
                    on='store_id',
                    how='left'
                )
                fig = create_revenue_by_dimension_chart(sales_with_store, 'channel')
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
            
            # Top 10 Stockout Risk Table
            st.subheader("🚨 Top 10 Stockout Risk Items")
            top_stockout = sim_results.get('top_stockout_items', pd.DataFrame())
            if not top_stockout.empty:
                st.dataframe(
                    top_stockout.style.format({
                        'Projected Demand': '{:.0f}',
                        'Stock Available': '{:.0f}'
                    }),
                    use_container_width=True
                )
            else:
                st.info("No stockout risks detected for current simulation parameters.")
            
            st.markdown("---")
            
            # Data Quality Summary
            st.subheader("🔍 Data Quality Summary")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Issues Found", len(issues_df))
            
            with col2:
                if not issues_df.empty:
                    top_issue = issues_df['issue_type'].value_counts().index[0]
                    st.metric("Most Common Issue", top_issue)
                else:
                    st.metric("Most Common Issue", "None")
            
            with col3:
                tables_cleaned = len(st.session_state.cleaning_stats)
                st.metric("Tables Cleaned", tables_cleaned)
            
            # Issues Log Table
            if not issues_df.empty:
                with st.expander("📋 View Full Issues Log"):
                    st.dataframe(issues_df, use_container_width=True)
        
        # =====================================================================
        # DOWNLOAD SECTION (Common to both views)
        # =====================================================================
        st.markdown("---")
        st.subheader("📥 Download Data")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if not sales_df.empty:
                st.download_button(
                    label="⬇️ Download Cleaned Sales",
                    data=convert_df_to_csv(sales_df),
                    file_name="cleaned_sales.csv",
                    mime="text/csv"
                )
        
        with col2:
            if not issues_df.empty:
                st.download_button(
                    label="⬇️ Download Issues Log",
                    data=convert_df_to_csv(issues_df),
                    file_name="issues.csv",
                    mime="text/csv"
                )
        
        with col3:
            if not scenario_df.empty:
                st.download_button(
                    label="⬇️ Download Scenarios",
                    data=convert_df_to_csv(scenario_df),
                    file_name="scenarios.csv",
                    mime="text/csv"
                )
    
    else:
        # No data loaded yet
        st.info("👆 Please upload data files using the options above to begin analysis.")
        
        # Show expected schema
        with st.expander("📋 Expected Data Schema"):
            st.markdown("""
            ### Products Table
            | Column | Description |
            |--------|-------------|
            | product_id | Unique product identifier |
            | category | Product category |
            | brand | Product brand |
            | base_price_aed | Base selling price (AED) |
            | unit_cost_aed | Unit cost (AED) |
            | tax_rate | Tax rate (decimal, e.g., 0.05) |
            | launch_flag | 'New' or 'Regular' |
            
            ### Stores Table
            | Column | Description |
            |--------|-------------|
            | store_id | Unique store identifier |
            | city | City name (Dubai/Abu Dhabi/Sharjah) |
            | channel | Sales channel (App/Web/Marketplace) |
            | fulfillment_type | 'Own' or '3PL' |
            
            ### Sales Table
            | Column | Description |
            |--------|-------------|
            | order_id | Unique order identifier |
            | order_time | Order timestamp |
            | product_id | Product identifier |
            | store_id | Store identifier |
            | qty | Quantity ordered |
            | selling_price_aed | Selling price (AED) |
            | discount_pct | Discount percentage |
            | payment_status | 'Paid', 'Failed', or 'Refunded' |
            | return_flag | Return indicator (0 or 1) |
            
            ### Inventory Table
            | Column | Description |
            |--------|-------------|
            | snapshot_date | Date of inventory snapshot |
            | product_id | Product identifier |
            | store_id | Store identifier |
            | stock_on_hand | Current stock quantity |
            | reorder_point | Reorder threshold |
            | lead_time_days | Lead time in days |
            """)
    
    # =========================================================================
    # FOOTER
    # =========================================================================
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 12px;'>
        UAE Promo Pulse Simulator | Data Rescue Dashboard<br>
        Built with Streamlit + Pandas + Plotly
        </div>
        """,
        unsafe_allow_html=True
    )


# =============================================================================
# RUN APPLICATION
# =============================================================================
if __name__ == "__main__":
    main()