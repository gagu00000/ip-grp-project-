"""
=============================================================================
UAE PROMO PULSE SIMULATOR + DATA RESCUE DASHBOARD
=============================================================================
Premium Executive Dashboard with Navy Blue & Silver Theme

Features:
    - Modern dark theme with gradient backgrounds
    - Custom KPI cards with hover effects
    - Styled insight boxes and status badges
    - Professional Plotly charts with consistent theming
    - Executive/Manager toggle views
    - Faculty dataset testing with column mapping
    - Defensive error handling throughout

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
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# COLOR PALETTE - NAVY BLUE & SILVER EXECUTIVE THEME
# =============================================================================

COLORS = {
    # Main Colors
    'primary': '#3a86ff',
    'secondary': '#4cc9f0',
    'accent': '#7209b7',
    
    # Status Colors
    'success': '#4ade80',
    'warning': '#fb923c',
    'danger': '#f87171',
    
    # Neutral Colors
    'neutral': '#8facc4',
    'dark': '#0a1628',
    'medium': '#1a2d47',
    'light': '#2a4a7f',
    
    # Text Colors
    'text_primary': '#ffffff',
    'text_secondary': '#e8e8e8',
    'text_muted': '#8facc4',
    'text_dark': '#b0b0b0',
}

CHART_COLORS = [
    '#3a86ff',  # Blue
    '#4cc9f0',  # Cyan
    '#4ade80',  # Green
    '#fb923c',  # Orange
    '#f87171',  # Red
    '#a78bfa',  # Light Purple
    '#7209b7',  # Dark Purple
    '#fbbf24',  # Yellow
    '#ec4899',  # Pink
    '#14b8a6',  # Teal
]

# =============================================================================
# CUSTOM CSS STYLING
# =============================================================================

st.markdown("""
<style>
    /* ===== IMPORTS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* ===== ROOT VARIABLES ===== */
    :root {
        --primary: #3a86ff;
        --secondary: #4cc9f0;
        --success: #4ade80;
        --warning: #fb923c;
        --danger: #f87171;
        --dark: #0a1628;
        --medium: #1a2d47;
        --light: #2a4a7f;
    }
    
    /* ===== MAIN BACKGROUND ===== */
    .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #1a2d47 50%, #0d1b2a 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1628 0%, #152238 100%);
        border-right: 2px solid #3a86ff;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #e8e8e8;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stNumberInput label,
    [data-testid="stSidebar"] .stDateInput label {
        color: #e8e8e8 !important;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: #e8e8e8 !important;
    }
    
    /* ===== SIDEBAR HEADER ===== */
    .sidebar-header {
        background: linear-gradient(135deg, #3a86ff 0%, #4cc9f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    
    /* ===== HEADINGS ===== */
    h1 {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1.8rem !important;
        border-bottom: 2px solid #3a86ff;
        padding-bottom: 10px;
        margin-bottom: 25px !important;
    }
    
    h3 {
        color: #e8e8e8 !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
    }
    
    h4, h5, h6 {
        color: #e8e8e8 !important;
    }
    
    /* ===== PARAGRAPH TEXT ===== */
    p, .stMarkdown {
        color: #d0d0d0;
    }
    
    /* ===== NATIVE METRICS ===== */
    [data-testid="stMetricValue"] {
        color: #3a86ff;
        font-size: 2rem;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        color: #8facc4;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.75rem;
    }
    
    [data-testid="stMetricDelta"] svg {
        display: none;
    }
    
    [data-testid="stMetricDelta"] {
        color: #4ade80;
    }
    
    /* ===== DIVIDER ===== */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #3a86ff, transparent);
        margin: 30px 0;
        border: none;
    }
    
    .divider-subtle {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a4a7f, transparent);
        margin: 20px 0;
        border: none;
    }
    
    /* ===== KPI CARDS ===== */
    .kpi-container {
        display: flex;
        gap: 20px;
        margin: 20px 0;
    }
    
    .kpi-card {
        background: linear-gradient(135deg, #1a2d47 0%, #0d1b2a 100%);
        border: 1px solid #2a4a7f;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3a86ff, #4cc9f0);
    }
    
    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(58, 134, 255, 0.2);
        border-color: #3a86ff;
    }
    
    .kpi-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
        margin: 10px 0;
        line-height: 1.2;
    }
    
    .kpi-value-small {
        font-size: 1.6rem;
    }
    
    .kpi-label {
        color: #8facc4;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }
    
    .kpi-delta {
        margin-top: 10px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .kpi-delta-positive {
        color: #4ade80;
    }
    
    .kpi-delta-negative {
        color: #f87171;
    }
    
    .kpi-delta-neutral {
        color: #8facc4;
    }
    
    /* KPI Card Color Variants */
    .kpi-card-primary::before {
        background: linear-gradient(90deg, #3a86ff, #4cc9f0);
    }
    
    .kpi-card-success::before {
        background: linear-gradient(90deg, #4ade80, #14b8a6);
    }
    
    .kpi-card-warning::before {
        background: linear-gradient(90deg, #fb923c, #fbbf24);
    }
    
    .kpi-card-danger::before {
        background: linear-gradient(90deg, #f87171, #ec4899);
    }
    
    /* ===== INSIGHT BOX ===== */
    .insight-box {
        background: linear-gradient(135deg, #1a2d47 0%, #0d1b2a 100%);
        border: 1px solid #2a4a7f;
        border-left: 4px solid #3a86ff;
        border-radius: 12px;
        padding: 24px 28px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .insight-box-success {
        border-left-color: #4ade80;
    }
    
    .insight-box-warning {
        border-left-color: #fb923c;
    }
    
    .insight-box-danger {
        border-left-color: #f87171;
    }
    
    .insight-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 15px;
    }
    
    .insight-icon {
        font-size: 1.5rem;
    }
    
    .insight-title {
        color: #3a86ff;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 0;
    }
    
    .insight-title-success {
        color: #4ade80;
    }
    
    .insight-title-warning {
        color: #fb923c;
    }
    
    .insight-title-danger {
        color: #f87171;
    }
    
    .insight-text {
        color: #d0d0d0;
        font-size: 0.95rem;
        line-height: 1.8;
        margin: 0;
    }
    
    /* ===== STATUS BOX ===== */
    .status-box {
        background: linear-gradient(135deg, rgba(58, 134, 255, 0.1), #0d1b2a);
        border: 1px solid #3a86ff;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 15px 0;
    }
    
    .status-box-success {
        background: linear-gradient(135deg, rgba(74, 222, 128, 0.1), #0d1b2a);
        border-color: #4ade80;
    }
    
    .status-box-warning {
        background: linear-gradient(135deg, rgba(251, 146, 60, 0.1), #0d1b2a);
        border-color: #fb923c;
    }
    
    .status-box-danger {
        background: linear-gradient(135deg, rgba(248, 113, 113, 0.1), #0d1b2a);
        border-color: #f87171;
    }
    
    .status-label {
        color: #8facc4;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }
    
    .status-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #3a86ff;
    }
    
    .status-value-success {
        color: #4ade80;
    }
    
    .status-value-warning {
        color: #fb923c;
    }
    
    .status-value-danger {
        color: #f87171;
    }
    
    /* ===== RECOMMENDATION BOX ===== */
    .recommendation-box {
        background: linear-gradient(135deg, #1a2d47 0%, #152238 100%);
        border: 1px solid #2a4a7f;
        border-radius: 16px;
        padding: 28px;
        margin: 25px 0;
        position: relative;
        overflow: hidden;
    }
    
    .recommendation-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #3a86ff, #4cc9f0, #4ade80);
    }
    
    .recommendation-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    .recommendation-icon {
        font-size: 1.8rem;
    }
    
    .recommendation-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0;
    }
    
    .recommendation-content {
        color: #d0d0d0;
        font-size: 1rem;
        line-height: 2;
    }
    
    .recommendation-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin: 12px 0;
        padding: 14px 18px;
        background: rgba(58, 134, 255, 0.08);
        border-radius: 10px;
        border-left: 4px solid #3a86ff;
    }
    
    .recommendation-item-success {
        border-left-color: #4ade80;
        background: rgba(74, 222, 128, 0.08);
    }
    
    .recommendation-item-warning {
        border-left-color: #fb923c;
        background: rgba(251, 146, 60, 0.08);
    }
    
    .recommendation-item-danger {
        border-left-color: #f87171;
        background: rgba(248, 113, 113, 0.08);
    }
    
    .recommendation-item strong {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* ===== CONSTRAINT CARDS ===== */
    .constraint-card {
        background: linear-gradient(135deg, #1a2d47 0%, #0d1b2a 100%);
        border: 1px solid #2a4a7f;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    .constraint-icon {
        font-size: 2rem;
    }
    
    .constraint-content {
        flex: 1;
    }
    
    .constraint-label {
        color: #8facc4;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .constraint-status {
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 4px;
    }
    
    .constraint-pass {
        color: #4ade80;
    }
    
    .constraint-fail {
        color: #f87171;
    }
    
    /* ===== DATA TABLE STYLING ===== */
    .styled-table {
        background: #1a2d47;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #2a4a7f;
    }
    
    .stDataFrame {
        border: 1px solid #2a4a7f !important;
        border-radius: 12px !important;
    }
    
    .stDataFrame [data-testid="stTable"] {
        background: #1a2d47;
    }
    
    /* ===== RADIO BUTTONS ===== */
    .stRadio > div {
        background: linear-gradient(135deg, rgba(58, 134, 255, 0.1), rgba(26, 45, 71, 0.5));
        border-radius: 12px;
        padding: 12px 16px;
        border: 1px solid #2a4a7f;
    }
    
    .stRadio > div:hover {
        border-color: #3a86ff;
    }
    
    .stRadio > div > label {
        color: #e8e8e8 !important;
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #3a86ff 0%, #4cc9f0 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 28px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(58, 134, 255, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #1a2d47 0%, #0d1b2a 100%);
        border: 1px solid #3a86ff;
        color: #3a86ff;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #3a86ff 0%, #4cc9f0 100%);
        color: white;
    }
    
    /* ===== SELECT BOXES ===== */
    .stSelectbox > div > div {
        background-color: #1a2d47;
        border-color: #2a4a7f;
        border-radius: 8px;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #3a86ff;
    }
    
    /* ===== SLIDERS ===== */
    .stSlider > div > div > div {
        background-color: #3a86ff;
    }
    
    /* ===== NUMBER INPUT ===== */
    .stNumberInput > div > div > input {
        background-color: #1a2d47;
        border-color: #2a4a7f;
        color: #e8e8e8;
        border-radius: 8px;
    }
    
    /* ===== TEXT INPUT ===== */
    .stTextInput > div > div > input {
        background-color: #1a2d47;
        border-color: #2a4a7f;
        color: #e8e8e8;
        border-radius: 8px;
    }
    
    /* ===== FILE UPLOADER ===== */
    .stFileUploader > div {
        background-color: #1a2d47;
        border: 2px dashed #2a4a7f;
        border-radius: 12px;
        padding: 20px;
    }
    
    .stFileUploader > div:hover {
        border-color: #3a86ff;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(135deg, rgba(58, 134, 255, 0.1), rgba(26, 45, 71, 0.5));
        border-radius: 12px;
        padding: 6px;
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #8facc4;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3a86ff 0%, #4cc9f0 100%);
        color: white;
    }
    
    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #1a2d47 0%, #152238 100%);
        border: 1px solid #2a4a7f;
        border-radius: 10px;
        color: #e8e8e8;
        font-weight: 500;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #3a86ff;
    }
    
    .streamlit-expanderContent {
        background: #0d1b2a;
        border: 1px solid #2a4a7f;
        border-top: none;
        border-radius: 0 0 10px 10px;
    }
    
    /* ===== ALERTS ===== */
    .stAlert {
        border-radius: 10px;
    }
    
    /* ===== SPINNER ===== */
    .stSpinner > div {
        border-top-color: #3a86ff !important;
    }
    
    /* ===== PROGRESS BAR ===== */
    .stProgress > div > div {
        background: linear-gradient(90deg, #3a86ff, #4cc9f0);
        border-radius: 10px;
    }
    
    /* ===== SECTION HEADER ===== */
    .section-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 30px 0 20px 0;
    }
    
    .section-icon {
        font-size: 1.8rem;
    }
    
    .section-title {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 0;
    }
    
    .section-subtitle {
        color: #8facc4;
        font-size: 0.9rem;
        margin-top: 5px;
    }
    
    /* ===== VIEW TOGGLE ===== */
    .view-toggle {
        background: linear-gradient(135deg, #1a2d47 0%, #0d1b2a 100%);
        border: 1px solid #2a4a7f;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 20px;
    }
    
    .view-toggle-label {
        color: #8facc4;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a1628;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #3a86ff, #4cc9f0);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #4cc9f0, #3a86ff);
    }
    
    /* ===== PAGE HEADER ===== */
    .page-header {
        background: linear-gradient(135deg, rgba(58, 134, 255, 0.1), rgba(26, 45, 71, 0.3));
        border: 1px solid #2a4a7f;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .page-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #3a86ff 0%, #4cc9f0 50%, #4ade80 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .page-subtitle {
        color: #8facc4;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* ===== FOOTER ===== */
    .footer {
        text-align: center;
        padding: 30px 0;
        margin-top: 50px;
        border-top: 1px solid #2a4a7f;
        color: #8facc4;
        font-size: 0.85rem;
    }
    
    .footer-brand {
        color: #3a86ff;
        font-weight: 600;
    }
    
    /* ===== ANIMATION ===== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .kpi-value {
            font-size: 1.6rem;
        }
        .page-title {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONSTANTS & CONFIGURATION
# =============================================================================

VALID_CITIES = ['Dubai', 'Abu Dhabi', 'Sharjah']
VALID_CHANNELS = ['App', 'Web', 'Marketplace']
VALID_CATEGORIES = ['Electronics', 'Fashion', 'Grocery', 'Home & Garden', 'Beauty', 'Sports']
VALID_PAYMENT_STATUSES = ['Paid', 'Failed', 'Refunded']
VALID_FULFILLMENT_TYPES = ['Own', '3PL']
VALID_LAUNCH_FLAGS = ['New', 'Regular']

CITY_MAPPING = {
    'dubai': 'Dubai', 'DUBAI': 'Dubai', 'Dubayy': 'Dubai', 'DXB': 'Dubai', 'Dубай': 'Dubai',
    'abu dhabi': 'Abu Dhabi', 'ABU DHABI': 'Abu Dhabi', 'AbuDhabi': 'Abu Dhabi', 
    'AD': 'Abu Dhabi', 'Abudhabi': 'Abu Dhabi', 'abudhabi': 'Abu Dhabi',
    'sharjah': 'Sharjah', 'SHARJAH': 'Sharjah', 'Shj': 'Sharjah', 
    'Sharijah': 'Sharjah', 'Al Sharjah': 'Sharjah'
}

QTY_MAX_THRESHOLD = 20
QTY_OUTLIER_CAP = 10
PRICE_MULTIPLIER_THRESHOLD = 5

UPLIFT_CONFIG = {
    'base_multiplier': 0.03,
    'max_uplift': 2.0,
    'channel_modifiers': {
        'Marketplace': 1.20,
        'App': 1.05,
        'Web': 1.00
    },
    'category_modifiers': {
        'Electronics': 1.25,
        'Fashion': 1.15,
        'Sports': 1.10,
        'Beauty': 1.05,
        'Home & Garden': 1.00,
        'Grocery': 0.85
    }
}


# =============================================================================
# UI HELPER COMPONENTS
# =============================================================================

def render_page_header():
    """Render the main page header."""
    st.markdown("""
    <div class="page-header animate-fade-in">
        <div class="page-title">🚀 UAE Promo Pulse Simulator</div>
        <div class="page-subtitle">Data Rescue Dashboard + What-If Promotional Simulation</div>
    </div>
    """, unsafe_allow_html=True)


def render_divider():
    """Render a styled divider."""
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


def render_subtle_divider():
    """Render a subtle divider."""
    st.markdown('<div class="divider-subtle"></div>', unsafe_allow_html=True)


def render_section_header(icon, title, subtitle=None):
    """Render a section header."""
    subtitle_html = f'<div class="section-subtitle">{subtitle}</div>' if subtitle else ''
    st.markdown(f"""
    <div class="section-header">
        <span class="section-icon">{icon}</span>
        <div>
            <div class="section-title">{title}</div>
            {subtitle_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_kpi_card(icon, value, label, delta=None, delta_type="neutral", card_type="primary"):
    """Render a styled KPI card."""
    delta_class = f"kpi-delta-{delta_type}"
    delta_symbol = "▲" if delta_type == "positive" else "▼" if delta_type == "negative" else "●"
    delta_html = f'<div class="kpi-delta {delta_class}">{delta_symbol} {delta}</div>' if delta else ''
    
    return f"""
    <div class="kpi-card kpi-card-{card_type}">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """


def render_kpi_row(kpis):
    """Render a row of KPI cards."""
    cols = st.columns(len(kpis))
    for col, kpi in zip(cols, kpis):
        with col:
            st.markdown(render_kpi_card(**kpi), unsafe_allow_html=True)


def render_insight_box(icon, title, content, box_type="primary"):
    """Render an insight box."""
    st.markdown(f"""
    <div class="insight-box insight-box-{box_type}">
        <div class="insight-header">
            <span class="insight-icon">{icon}</span>
            <div class="insight-title insight-title-{box_type}">{title}</div>
        </div>
        <p class="insight-text">{content}</p>
    </div>
    """, unsafe_allow_html=True)


def render_status_box(label, value, status_type="primary"):
    """Render a status box."""
    st.markdown(f"""
    <div class="status-box status-box-{status_type}">
        <div class="status-label">{label}</div>
        <div class="status-value status-value-{status_type}">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def render_constraint_card(icon, label, status, is_pass):
    """Render a constraint status card."""
    status_class = "constraint-pass" if is_pass else "constraint-fail"
    st.markdown(f"""
    <div class="constraint-card">
        <span class="constraint-icon">{icon}</span>
        <div class="constraint-content">
            <div class="constraint-label">{label}</div>
            <div class="constraint-status {status_class}">{status}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_recommendation_box(recommendations):
    """Render the AI recommendation box."""
    items_html = ""
    for rec in recommendations:
        item_type = rec.get('type', 'primary')
        text_content = rec['text']
        items_html += f"""
        <div class="recommendation-item recommendation-item-{item_type}">
            <span style="font-size: 1.2rem;">{rec['icon']}</span>
            <span style="color: #d0d0d0;">{text_content}</span>
        </div>
        """
    
    st.markdown(f"""
    <div class="recommendation-box">
        <div class="recommendation-header">
            <span class="recommendation-icon">🤖</span>
            <div class="recommendation-title">AI-Powered Recommendations</div>
        </div>
        <div class="recommendation-content">
            {items_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the page footer."""
    st.markdown("""
    <div class="footer">
        <span class="footer-brand">UAE Promo Pulse Simulator</span> | 
        Data Rescue Dashboard | Built with Streamlit + Plotly
        <br>© 2024 Data Rescue Team
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# PLOTLY CHART THEME
# =============================================================================

def get_chart_layout(title="", height=400):
    """Returns consistent Plotly layout for dark theme."""
    return dict(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e8e8e8', family='Inter'),
        title=dict(
            text=title,
            font=dict(color='#ffffff', size=16, family='Inter'),
            x=0,
            xanchor='left'
        ),
        xaxis=dict(
            gridcolor='rgba(58,134,255,0.1)',
            linecolor='#2a4a7f',
            tickfont=dict(color='#8facc4', size=11),
            title_font=dict(color='#8facc4', size=12)
        ),
        yaxis=dict(
            gridcolor='rgba(58,134,255,0.1)',
            linecolor='#2a4a7f',
            tickfont=dict(color='#8facc4', size=11),
            title_font=dict(color='#8facc4', size=12)
        ),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e8e8e8', size=11),
            bordercolor='#2a4a7f'
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        height=height,
        hoverlabel=dict(
            bgcolor='#1a2d47',
            font_size=12,
            font_family='Inter',
            bordercolor='#3a86ff'
        )
    )


def style_plotly_chart(fig, title="", height=400):
    """Apply consistent styling to a Plotly figure."""
    fig.update_layout(**get_chart_layout(title, height))
    return fig


# =============================================================================
# DATA CLEANER MODULE
# =============================================================================

class DataCleaner:
    """Data Rescue Toolkit: Validates and cleans dirty datasets."""
    
    def __init__(self):
        self.issues_log = []
        self.cleaning_stats = {}
    
    def log_issue(self, table_name, record_id, issue_type, issue_detail, action_taken):
        """Log a data quality issue."""
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
    
    def clean_products(self, df):
        """Clean products table."""
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # Ensure required columns exist
        if 'product_id' not in df.columns:
            df['product_id'] = [f'PROD_{i:05d}' for i in range(len(df))]
        
        if 'base_price_aed' not in df.columns:
            df['base_price_aed'] = 100.0
        
        if 'unit_cost_aed' not in df.columns:
            df['unit_cost_aed'] = np.nan
        
        # Handle missing unit_cost_aed
        missing_cost_mask = df['unit_cost_aed'].isna()
        missing_cost_count = missing_cost_mask.sum()
        
        if missing_cost_count > 0:
            for idx in df[missing_cost_mask].index:
                product_id = df.loc[idx, 'product_id']
                base_price = df.loc[idx, 'base_price_aed']
                imputed_cost = round(base_price * 0.5, 2)
                df.loc[idx, 'unit_cost_aed'] = imputed_cost
                
                self.log_issue(
                    table_name='products',
                    record_id=product_id,
                    issue_type='MISSING_VALUE',
                    issue_detail=f'unit_cost_aed was NULL, base_price={base_price}',
                    action_taken=f'Imputed as 50% of base_price: {imputed_cost}'
                )
            stats['issues_found'] += missing_cost_count
        
        # Validate unit_cost <= base_price
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
        
        # Validate category
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
        else:
            df['category'] = 'Other'
        
        # Validate tax_rate
        if 'tax_rate' in df.columns:
            invalid_tax_mask = (df['tax_rate'] < 0) | (df['tax_rate'] > 1)
            if invalid_tax_mask.sum() > 0:
                for idx in df[invalid_tax_mask].index:
                    product_id = df.loc[idx, 'product_id']
                    old_tax = df.loc[idx, 'tax_rate']
                    df.loc[idx, 'tax_rate'] = 0.05
                    
                    self.log_issue(
                        table_name='products',
                        record_id=product_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid tax_rate: {old_tax}',
                        action_taken='Set to 0.05 (UAE VAT)'
                    )
                stats['issues_found'] += invalid_tax_mask.sum()
        else:
            df['tax_rate'] = 0.05
        
        # Validate launch_flag
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
        else:
            df['launch_flag'] = 'Regular'
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['products'] = stats
        
        return df
    
    def clean_stores(self, df):
        """Clean stores table."""
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # Ensure required columns exist
        if 'store_id' not in df.columns:
            df['store_id'] = [f'STORE_{i:03d}' for i in range(len(df))]
        
        # Standardize city names
        if 'city' in df.columns:
            for idx in df.index:
                city_value = df.loc[idx, 'city']
                store_id = df.loc[idx, 'store_id']
                
                if pd.isna(city_value):
                    df.loc[idx, 'city'] = 'Dubai'
                    self.log_issue(
                        table_name='stores',
                        record_id=store_id,
                        issue_type='MISSING_VALUE',
                        issue_detail='city was NULL',
                        action_taken='Defaulted to Dubai'
                    )
                    stats['issues_found'] += 1
                elif city_value not in VALID_CITIES:
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
                            df.loc[idx, 'city'] = 'Dubai'
                            self.log_issue(
                                table_name='stores',
                                record_id=store_id,
                                issue_type='INVALID_VALUE',
                                issue_detail=f'Unknown city: {city_value}',
                                action_taken='Defaulted to Dubai'
                            )
                            stats['issues_found'] += 1
        else:
            df['city'] = 'Dubai'
        
        # Validate channel
        if 'channel' in df.columns:
            invalid_channel_mask = ~df['channel'].isin(VALID_CHANNELS)
            if invalid_channel_mask.sum() > 0:
                for idx in df[invalid_channel_mask].index:
                    store_id = df.loc[idx, 'store_id']
                    old_channel = df.loc[idx, 'channel']
                    df.loc[idx, 'channel'] = 'Web'
                    
                    self.log_issue(
                        table_name='stores',
                        record_id=store_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid channel: {old_channel}',
                        action_taken='Defaulted to Web'
                    )
                stats['issues_found'] += invalid_channel_mask.sum()
        else:
            df['channel'] = 'Web'
        
        # Validate fulfillment_type
        if 'fulfillment_type' in df.columns:
            invalid_fulfill_mask = ~df['fulfillment_type'].isin(VALID_FULFILLMENT_TYPES)
            if invalid_fulfill_mask.sum() > 0:
                for idx in df[invalid_fulfill_mask].index:
                    store_id = df.loc[idx, 'store_id']
                    old_fulfill = df.loc[idx, 'fulfillment_type']
                    df.loc[idx, 'fulfillment_type'] = 'Own'
                    
                    self.log_issue(
                        table_name='stores',
                        record_id=store_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid fulfillment_type: {old_fulfill}',
                        action_taken='Defaulted to Own'
                    )
                stats['issues_found'] += invalid_fulfill_mask.sum()
        else:
            df['fulfillment_type'] = 'Own'
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['stores'] = stats
        
        return df
    
    def clean_sales(self, df, products_df=None):
        """Clean sales table."""
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # Ensure required columns exist
        if 'order_id' not in df.columns:
            df['order_id'] = [f'ORD_{i:08d}' for i in range(len(df))]
        
        if 'qty' not in df.columns:
            df['qty'] = 1
        
        if 'selling_price_aed' not in df.columns:
            df['selling_price_aed'] = 100.0
        
        if 'payment_status' not in df.columns:
            df['payment_status'] = 'Paid'
        
        if 'return_flag' not in df.columns:
            df['return_flag'] = 0
        
        if 'discount_pct' not in df.columns:
            df['discount_pct'] = 0.0
        
        # Parse and validate timestamps
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
                
                df = df[~invalid_time_mask].copy()
            
            df['order_time'] = df['order_time_parsed']
            df = df.drop(columns=['order_time_parsed'])
        else:
            df['order_time'] = datetime.now()
        
        # Handle duplicates
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
                
                df = df[~duplicate_mask].copy()
        
        # Handle missing discount_pct
        if 'discount_pct' in df.columns:
            missing_discount_mask = df['discount_pct'].isna()
            missing_discount_count = missing_discount_mask.sum()
            
            if missing_discount_count > 0:
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
        
        # Handle qty outliers
        if 'qty' in df.columns:
            # Convert to numeric
            df['qty'] = pd.to_numeric(df['qty'], errors='coerce').fillna(1).astype(int)
            
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
        
        # Handle price outliers
        if 'selling_price_aed' in df.columns:
            df['selling_price_aed'] = pd.to_numeric(df['selling_price_aed'], errors='coerce').fillna(100)
            
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
        
        # Validate payment_status
        if 'payment_status' in df.columns:
            invalid_status_mask = ~df['payment_status'].isin(VALID_PAYMENT_STATUSES)
            if invalid_status_mask.sum() > 0:
                for idx in df[invalid_status_mask].index:
                    order_id = df.loc[idx, 'order_id']
                    old_status = df.loc[idx, 'payment_status']
                    df.loc[idx, 'payment_status'] = 'Paid'
                    
                    self.log_issue(
                        table_name='sales_raw',
                        record_id=order_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid payment_status: {old_status}',
                        action_taken='Defaulted to Paid'
                    )
                stats['issues_found'] += invalid_status_mask.sum()
        
        # Validate return_flag
        if 'return_flag' in df.columns:
            df['return_flag'] = pd.to_numeric(df['return_flag'], errors='coerce').fillna(0).astype(int)
            df.loc[~df['return_flag'].isin([0, 1]), 'return_flag'] = 0
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['sales'] = stats
        
        return df
    
    def clean_inventory(self, df):
        """Clean inventory table."""
        if df is None or df.empty:
            return df
        
        df = df.copy()
        original_count = len(df)
        stats = {'original': original_count, 'issues_found': 0}
        
        # Ensure required columns exist
        if 'product_id' not in df.columns:
            df['product_id'] = 'PROD_00001'
        
        if 'store_id' not in df.columns:
            df['store_id'] = 'STORE_001'
        
        if 'stock_on_hand' not in df.columns:
            df['stock_on_hand'] = 100
        
        if 'snapshot_date' not in df.columns:
            df['snapshot_date'] = datetime.now().date()
        
        # Handle negative stock_on_hand
        if 'stock_on_hand' in df.columns:
            df['stock_on_hand'] = pd.to_numeric(df['stock_on_hand'], errors='coerce').fillna(0)
            
            negative_stock_mask = df['stock_on_hand'] < 0
            negative_stock_count = negative_stock_mask.sum()
            
            if negative_stock_count > 0:
                for idx in df[negative_stock_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}"
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
            
            # Handle extreme stock values
            extreme_threshold = 9000
            extreme_stock_mask = df['stock_on_hand'] > extreme_threshold
            extreme_stock_count = extreme_stock_mask.sum()
            
            if extreme_stock_count > 0:
                reasonable_stocks = df[df['stock_on_hand'] <= extreme_threshold]['stock_on_hand']
                if len(reasonable_stocks) > 0:
                    stock_cap = reasonable_stocks.quantile(0.99)
                else:
                    stock_cap = 500
                
                for idx in df[extreme_stock_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}"
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
        
        # Handle negative reorder_point
        if 'reorder_point' in df.columns:
            df['reorder_point'] = pd.to_numeric(df['reorder_point'], errors='coerce').fillna(10)
            
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
        else:
            df['reorder_point'] = 10
        
        # Validate lead_time_days
        if 'lead_time_days' in df.columns:
            df['lead_time_days'] = pd.to_numeric(df['lead_time_days'], errors='coerce').fillna(7)
            
            invalid_lead_mask = (df['lead_time_days'] <= 0) | (df['lead_time_days'] > 90)
            if invalid_lead_mask.sum() > 0:
                for idx in df[invalid_lead_mask].index:
                    record_id = f"{df.loc[idx, 'product_id']}_{df.loc[idx, 'store_id']}"
                    old_val = df.loc[idx, 'lead_time_days']
                    df.loc[idx, 'lead_time_days'] = 7
                    
                    self.log_issue(
                        table_name='inventory_snapshot',
                        record_id=record_id,
                        issue_type='INVALID_VALUE',
                        issue_detail=f'Invalid lead_time_days: {old_val}',
                        action_taken='Set to 7 days'
                    )
                stats['issues_found'] += invalid_lead_mask.sum()
        else:
            df['lead_time_days'] = 7
        
        # Parse snapshot_date
        if 'snapshot_date' in df.columns:
            df['snapshot_date'] = pd.to_datetime(df['snapshot_date'], errors='coerce')
            invalid_date_mask = df['snapshot_date'].isna()
            if invalid_date_mask.sum() > 0:
                stats['issues_found'] += invalid_date_mask.sum()
                df.loc[invalid_date_mask, 'snapshot_date'] = datetime.now()
        
        stats['final'] = len(df)
        stats['dropped'] = original_count - len(df)
        self.cleaning_stats['inventory'] = stats
        
        return df
    
    def run_full_pipeline(self, products_df=None, stores_df=None, 
                          sales_df=None, inventory_df=None):
        """Run the full cleaning pipeline."""
        cleaned = {}
        
        if products_df is not None and not products_df.empty:
            cleaned['products'] = self.clean_products(products_df)
        else:
            cleaned['products'] = pd.DataFrame()
        
        if stores_df is not None and not stores_df.empty:
            cleaned['stores'] = self.clean_stores(stores_df)
        else:
            cleaned['stores'] = pd.DataFrame()
        
        if sales_df is not None and not sales_df.empty:
            cleaned['sales'] = self.clean_sales(sales_df, products_df)
        else:
            cleaned['sales'] = pd.DataFrame()
        
        if inventory_df is not None and not inventory_df.empty:
            cleaned['inventory'] = self.clean_inventory(inventory_df)
        else:
            cleaned['inventory'] = pd.DataFrame()
        
        return cleaned


# =============================================================================
# KPI CALCULATOR MODULE (FIXED WITH DEFENSIVE CHECKS)
# =============================================================================

class KPICalculator:
    """Computes KPIs from cleaned sales data with defensive checks."""
    
    def __init__(self, sales_df, products_df=None, stores_df=None):
        self.sales = sales_df.copy() if sales_df is not None and not sales_df.empty else pd.DataFrame()
        self.products = products_df.copy() if products_df is not None and not products_df.empty else pd.DataFrame()
        self.stores = stores_df.copy() if stores_df is not None and not stores_df.empty else pd.DataFrame()
        self.sales_merged = self._merge_data()
    
    def _merge_data(self):
        """Safely merge sales with products and stores."""
        if self.sales.empty:
            return pd.DataFrame()
        
        merged = self.sales.copy()
        
        # Merge with products
        if not self.products.empty and 'product_id' in merged.columns and 'product_id' in self.products.columns:
            product_cols = ['product_id']
            for col in ['unit_cost_aed', 'category', 'base_price_aed']:
                if col in self.products.columns:
                    product_cols.append(col)
            
            if len(product_cols) > 1:
                merged = merged.merge(
                    self.products[product_cols],
                    on='product_id',
                    how='left'
                )
        
        # Merge with stores
        if not self.stores.empty and 'store_id' in merged.columns and 'store_id' in self.stores.columns:
            store_cols = ['store_id']
            for col in ['city', 'channel']:
                if col in self.stores.columns:
                    store_cols.append(col)
            
            if len(store_cols) > 1:
                merged = merged.merge(
                    self.stores[store_cols],
                    on='store_id',
                    how='left'
                )
        
        return merged
    
    def _safe_column_check(self, df, col):
        """Check if column exists in dataframe."""
        return df is not None and not df.empty and col in df.columns
    
    def calc_gross_revenue(self, df=None):
        """Calculate gross revenue."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'payment_status'):
            return 0
        if not self._safe_column_check(data, 'qty') or not self._safe_column_check(data, 'selling_price_aed'):
            return 0
        paid_sales = data[data['payment_status'] == 'Paid']
        return (paid_sales['qty'] * paid_sales['selling_price_aed']).sum()
    
    def calc_refund_amount(self, df=None):
        """Calculate refund amount."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'payment_status'):
            return 0
        if not self._safe_column_check(data, 'qty') or not self._safe_column_check(data, 'selling_price_aed'):
            return 0
        refunded = data[data['payment_status'] == 'Refunded']
        return (refunded['qty'] * refunded['selling_price_aed']).sum()
    
    def calc_net_revenue(self, df=None):
        """Calculate net revenue."""
        return self.calc_gross_revenue(df) - self.calc_refund_amount(df)
    
    def calc_cogs(self, df=None):
        """Calculate cost of goods sold."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'unit_cost_aed'):
            return 0
        if not self._safe_column_check(data, 'payment_status') or not self._safe_column_check(data, 'qty'):
            return 0
        paid_sales = data[data['payment_status'] == 'Paid']
        return (paid_sales['qty'] * paid_sales['unit_cost_aed']).sum()
    
    def calc_gross_margin_aed(self, df=None):
        """Calculate gross margin in AED."""
        return self.calc_net_revenue(df) - self.calc_cogs(df)
    
    def calc_gross_margin_pct(self, df=None):
        """Calculate gross margin percentage."""
        net_rev = self.calc_net_revenue(df)
        if net_rev == 0:
            return 0
        return (self.calc_gross_margin_aed(df) / net_rev) * 100
    
    def calc_avg_discount_pct(self, df=None):
        """Calculate average discount percentage."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'discount_pct'):
            return 0
        return data['discount_pct'].mean()
    
    def calc_return_rate(self, df=None):
        """Calculate return rate."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'payment_status'):
            return 0
        paid_orders = data[data['payment_status'] == 'Paid']
        if len(paid_orders) == 0:
            return 0
        if not self._safe_column_check(paid_orders, 'return_flag'):
            return 0
        return (paid_orders['return_flag'].sum() / len(paid_orders)) * 100
    
    def calc_payment_failure_rate(self, df=None):
        """Calculate payment failure rate."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'payment_status'):
            return 0
        failed = data[data['payment_status'] == 'Failed']
        return (len(failed) / len(data)) * 100
    
    def calc_total_orders(self, df=None):
        """Calculate total orders."""
        data = df if df is not None else self.sales_merged
        return len(data) if data is not None and not data.empty else 0
    
    def calc_total_units(self, df=None):
        """Calculate total units sold."""
        data = df if df is not None else self.sales_merged
        if data is None or data.empty:
            return 0
        if not self._safe_column_check(data, 'qty'):
            return 0
        return data['qty'].sum()
    
    def compute_all_kpis(self, df=None):
        """Compute all KPIs."""
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
        """Get KPIs grouped by dimension."""
        if self.sales_merged.empty or dimension not in self.sales_merged.columns:
            return pd.DataFrame()
        
        results = []
        for value in self.sales_merged[dimension].unique():
            if pd.isna(value):
                continue
            filtered = self.sales_merged[self.sales_merged[dimension] == value]
            kpis = self.compute_all_kpis(filtered)
            kpis[dimension] = value
            results.append(kpis)
        
        return pd.DataFrame(results) if results else pd.DataFrame()


# =============================================================================
# PROMO SIMULATOR MODULE (FIXED WITH DEFENSIVE CHECKS)
# =============================================================================

class PromoSimulator:
    """What-If Promo Simulation Engine with defensive checks."""
    
    def __init__(self, sales_df, products_df, stores_df, inventory_df):
        self.sales = sales_df.copy() if sales_df is not None and not sales_df.empty else pd.DataFrame()
        self.products = products_df.copy() if products_df is not None and not products_df.empty else pd.DataFrame()
        self.stores = stores_df.copy() if stores_df is not None and not stores_df.empty else pd.DataFrame()
        self.inventory = inventory_df.copy() if inventory_df is not None and not inventory_df.empty else pd.DataFrame()
        self.sales_merged = pd.DataFrame()
        self._prepare_data()
    
    def _safe_get_columns(self, df, columns):
        """Safely get columns that exist in dataframe."""
        if df is None or df.empty:
            return []
        existing = [col for col in columns if col in df.columns]
        return existing
    
    def _prepare_data(self):
        """Prepare merged data with defensive checks."""
        if self.sales.empty:
            self.sales_merged = pd.DataFrame()
            return
        
        self.sales_merged = self.sales.copy()
        
        # Merge with products if available
        if not self.products.empty and 'product_id' in self.sales_merged.columns:
            product_cols = self._safe_get_columns(
                self.products, 
                ['product_id', 'unit_cost_aed', 'category', 'base_price_aed']
            )
            
            if 'product_id' in product_cols:
                merge_cols = [col for col in product_cols if col in self.products.columns]
                if merge_cols:
                    self.sales_merged = self.sales_merged.merge(
                        self.products[merge_cols],
                        on='product_id',
                        how='left'
                    )
        
        # Merge with stores if available
        if not self.stores.empty and 'store_id' in self.sales_merged.columns:
            store_cols = self._safe_get_columns(
                self.stores,
                ['store_id', 'city', 'channel']
            )
            
            if 'store_id' in store_cols:
                merge_cols = [col for col in store_cols if col in self.stores.columns]
                if merge_cols:
                    self.sales_merged = self.sales_merged.merge(
                        self.stores[merge_cols],
                        on='store_id',
                        how='left'
                    )
    
    def calculate_baseline_demand(self, lookback_days=30):
        """Calculate baseline demand with defensive checks."""
        if self.sales_merged.empty:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        # Check for required columns
        required_cols = ['product_id', 'store_id', 'qty', 'payment_status', 'order_time']
        missing_cols = [col for col in required_cols if col not in self.sales_merged.columns]
        
        if missing_cols:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        paid_sales = self.sales_merged[self.sales_merged['payment_status'] == 'Paid'].copy()
        
        if paid_sales.empty:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        # Parse datetime
        if not pd.api.types.is_datetime64_any_dtype(paid_sales['order_time']):
            paid_sales['order_time'] = pd.to_datetime(paid_sales['order_time'], errors='coerce')
        
        # Remove rows with invalid timestamps
        paid_sales = paid_sales.dropna(subset=['order_time'])
        
        if paid_sales.empty:
            return pd.DataFrame(columns=['product_id', 'store_id', 'baseline_daily_demand'])
        
        max_date = paid_sales['order_time'].max()
        min_date = max_date - timedelta(days=lookback_days)
        recent_sales = paid_sales[paid_sales['order_time'] >= min_date]
        
        if recent_sales.empty:
            recent_sales = paid_sales
            date_range = (paid_sales['order_time'].max() - paid_sales['order_time'].min()).days
            lookback_days = max(1, date_range)
        
        baseline = recent_sales.groupby(['product_id', 'store_id']).agg({
            'qty': 'sum'
        }).reset_index()
        
        baseline['baseline_daily_demand'] = baseline['qty'] / max(lookback_days, 1)
        baseline = baseline.drop(columns=['qty'])
        
        return baseline
    
    def calculate_uplift_factor(self, discount_pct, channel='Web', category='Other'):
        """Calculate demand uplift factor."""
        base_uplift = 1 + (discount_pct * UPLIFT_CONFIG['base_multiplier'])
        base_uplift = min(base_uplift, UPLIFT_CONFIG['max_uplift'])
        
        channel_mod = UPLIFT_CONFIG['channel_modifiers'].get(channel, 1.0)
        category_mod = UPLIFT_CONFIG['category_modifiers'].get(category, 1.0)
        
        final_uplift = base_uplift * channel_mod * category_mod
        return min(final_uplift, UPLIFT_CONFIG['max_uplift'])
    
    def run_simulation(self, discount_pct, promo_budget_aed, margin_floor_pct,
                       simulation_days=14, city_filter='All', channel_filter='All',
                       category_filter='All'):
        """Run promotion simulation with comprehensive error handling."""
        
        # Initialize results structure
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
            'kpis': {
                'simulated_revenue': 0,
                'simulated_cogs': 0,
                'gross_margin_aed': 0,
                'gross_margin_pct': 0,
                'promo_spend': 0,
                'profit_proxy': 0,
                'budget_utilization': 0,
                'stockout_risk_pct': 0,
                'simulated_units': 0,
                'products_at_risk': 0
            },
            'constraints': {
                'budget_ok': True,
                'margin_ok': True,
                'all_ok': True
            },
            'violations': [],
            'details': pd.DataFrame(),
            'top_stockout_items': pd.DataFrame(columns=['Product', 'Store', 'Projected Demand', 'Stock Available', 'Category'])
        }
        
        # Get baseline demand
        baseline = self.calculate_baseline_demand()
        
        if baseline.empty:
            return results
        
        # Start building simulation data
        sim_data = baseline.copy()
        
        # Merge with products data
        if not self.products.empty:
            product_cols_to_merge = []
            for col in ['product_id', 'base_price_aed', 'unit_cost_aed', 'category']:
                if col in self.products.columns:
                    product_cols_to_merge.append(col)
            
            if 'product_id' in product_cols_to_merge:
                sim_data = sim_data.merge(
                    self.products[product_cols_to_merge],
                    on='product_id',
                    how='left'
                )
        
        # Merge with stores data
        if not self.stores.empty:
            store_cols_to_merge = []
            for col in ['store_id', 'city', 'channel']:
                if col in self.stores.columns:
                    store_cols_to_merge.append(col)
            
            if 'store_id' in store_cols_to_merge:
                sim_data = sim_data.merge(
                    self.stores[store_cols_to_merge],
                    on='store_id',
                    how='left'
                )
        
        # Fill missing values with defaults
        if 'base_price_aed' not in sim_data.columns:
            sim_data['base_price_aed'] = 100
        else:
            sim_data['base_price_aed'] = sim_data['base_price_aed'].fillna(100)
        
        if 'unit_cost_aed' not in sim_data.columns:
            sim_data['unit_cost_aed'] = sim_data['base_price_aed'] * 0.5
        else:
            sim_data['unit_cost_aed'] = sim_data['unit_cost_aed'].fillna(sim_data['base_price_aed'] * 0.5)
        
        if 'category' not in sim_data.columns:
            sim_data['category'] = 'Other'
        else:
            sim_data['category'] = sim_data['category'].fillna('Other')
        
        if 'city' not in sim_data.columns:
            sim_data['city'] = 'Dubai'
        else:
            sim_data['city'] = sim_data['city'].fillna('Dubai')
        
        if 'channel' not in sim_data.columns:
            sim_data['channel'] = 'Web'
        else:
            sim_data['channel'] = sim_data['channel'].fillna('Web')
        
        # Apply filters
        if city_filter != 'All' and 'city' in sim_data.columns:
            sim_data = sim_data[sim_data['city'] == city_filter]
        
        if channel_filter != 'All' and 'channel' in sim_data.columns:
            sim_data = sim_data[sim_data['channel'] == channel_filter]
        
        if category_filter != 'All' and 'category' in sim_data.columns:
            sim_data = sim_data[sim_data['category'] == category_filter]
        
        if sim_data.empty:
            return results
        
        # Calculate uplift factors
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
        
        # Merge with inventory
        if not self.inventory.empty and 'product_id' in self.inventory.columns and 'store_id' in self.inventory.columns:
            if 'snapshot_date' in self.inventory.columns:
                latest_inventory = self.inventory.sort_values('snapshot_date').groupby(
                    ['product_id', 'store_id']
                ).last().reset_index()
            else:
                latest_inventory = self.inventory.groupby(
                    ['product_id', 'store_id']
                ).first().reset_index()
            
            if 'stock_on_hand' in latest_inventory.columns:
                sim_data = sim_data.merge(
                    latest_inventory[['product_id', 'store_id', 'stock_on_hand']],
                    on=['product_id', 'store_id'],
                    how='left'
                )
                sim_data['stock_on_hand'] = sim_data['stock_on_hand'].fillna(0)
            else:
                sim_data['stock_on_hand'] = 1000
        else:
            sim_data['stock_on_hand'] = 1000
        
        # Calculate constrained demand and stockout flag
        sim_data['constrained_demand'] = sim_data[['simulated_total_demand', 'stock_on_hand']].min(axis=1)
        sim_data['stockout_flag'] = (sim_data['simulated_total_demand'] > sim_data['stock_on_hand']).astype(int)
        
        # Calculate financial metrics
        sim_data['discounted_price'] = sim_data['base_price_aed'] * (1 - discount_pct / 100)
        sim_data['simulated_revenue'] = sim_data['constrained_demand'] * sim_data['discounted_price']
        sim_data['simulated_cogs'] = sim_data['constrained_demand'] * sim_data['unit_cost_aed']
        sim_data['promo_discount_amount'] = sim_data['constrained_demand'] * sim_data['base_price_aed'] * (discount_pct / 100)
        
        # Aggregate KPIs
        total_simulated_revenue = sim_data['simulated_revenue'].sum()
        total_cogs = sim_data['simulated_cogs'].sum()
        total_promo_spend = sim_data['promo_discount_amount'].sum()
        total_units = sim_data['constrained_demand'].sum()
        
        gross_margin_aed = total_simulated_revenue - total_cogs
        gross_margin_pct = (gross_margin_aed / total_simulated_revenue * 100) if total_simulated_revenue > 0 else 0
        profit_proxy = gross_margin_aed - total_promo_spend
        budget_utilization = (total_promo_spend / promo_budget_aed * 100) if promo_budget_aed > 0 else 0
        stockout_risk = (sim_data['stockout_flag'].sum() / len(sim_data) * 100) if len(sim_data) > 0 else 0
        
        # Update results
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
            'products_at_risk': int(sim_data['stockout_flag'].sum())
        }
        
        # Check constraints
        violations = []
        
        if total_promo_spend > promo_budget_aed:
            violations.append({
                'constraint': 'BUDGET',
                'threshold': promo_budget_aed,
                'actual': total_promo_spend,
                'message': f'Promo spend (AED {total_promo_spend:,.0f}) exceeds budget (AED {promo_budget_aed:,.0f})'
            })
        
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
        
        # Get top stockout items
        stockout_items = sim_data[sim_data['stockout_flag'] == 1].copy()
        if not stockout_items.empty:
            stockout_items = stockout_items.nlargest(10, 'simulated_total_demand')
            results['top_stockout_items'] = stockout_items[
                ['product_id', 'store_id', 'simulated_total_demand', 'stock_on_hand', 'category']
            ].copy()
            results['top_stockout_items'].columns = ['Product', 'Store', 'Projected Demand', 'Stock Available', 'Category']
        else:
            results['top_stockout_items'] = pd.DataFrame(columns=['Product', 'Store', 'Projected Demand', 'Stock Available', 'Category'])
        
        results['details'] = sim_data
        
        return results
    
    def get_scenario_comparison(self, discount_scenarios, promo_budget, margin_floor, simulation_days=14):
        """Generate scenario comparison table."""
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
# CHART FUNCTIONS (FIXED WITH DEFENSIVE CHECKS)
# =============================================================================

def create_revenue_trend_chart(sales_df):
    """Create revenue trend chart with defensive checks."""
    if sales_df is None or sales_df.empty:
        return None
    
    required_cols = ['order_time', 'payment_status', 'qty', 'selling_price_aed']
    if not all(col in sales_df.columns for col in required_cols):
        return None
    
    df = sales_df.copy()
    
    if not pd.api.types.is_datetime64_any_dtype(df['order_time']):
        df['order_time'] = pd.to_datetime(df['order_time'], errors='coerce')
    
    df = df.dropna(subset=['order_time'])
    df = df[df['payment_status'] == 'Paid']
    
    if df.empty:
        return None
    
    df['revenue'] = df['qty'] * df['selling_price_aed']
    df['date'] = df['order_time'].dt.date
    
    daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
    daily_revenue.columns = ['Date', 'Revenue']
    
    if daily_revenue.empty:
        return None
    
    fig = px.area(
        daily_revenue,
        x='Date',
        y='Revenue',
        color_discrete_sequence=[COLORS['primary']]
    )
    
    fig.update_traces(
        fill='tozeroy',
        fillcolor='rgba(58, 134, 255, 0.2)',
        line=dict(color=COLORS['primary'], width=2)
    )
    
    fig = style_plotly_chart(fig, '📈 Revenue Trend', height=350)
    fig.update_layout(hovermode='x unified')
    
    return fig


def create_revenue_by_dimension_chart(sales_df, dimension='city'):
    """Create revenue by city/channel bar chart with defensive checks."""
    if sales_df is None or sales_df.empty:
        return None
    
    required_cols = ['payment_status', 'qty', 'selling_price_aed']
    if not all(col in sales_df.columns for col in required_cols):
        return None
    
    if dimension not in sales_df.columns:
        return None
    
    df = sales_df[sales_df['payment_status'] == 'Paid'].copy()
    
    if df.empty:
        return None
    
    df['revenue'] = df['qty'] * df['selling_price_aed']
    
    grouped = df.groupby(dimension)['revenue'].sum().reset_index()
    grouped.columns = [dimension.title(), 'Revenue']
    grouped = grouped.sort_values('Revenue', ascending=True)
    
    if grouped.empty:
        return None
    
    fig = px.bar(
        grouped,
        x='Revenue',
        y=dimension.title(),
        orientation='h',
        color='Revenue',
        color_continuous_scale=[[0, COLORS['medium']], [0.5, COLORS['primary']], [1, COLORS['secondary']]]
    )
    
    fig.update_traces(
        marker_line_color=COLORS['primary'],
        marker_line_width=1,
        texttemplate='AED %{x:,.0f}',
        textposition='outside'
    )
    
    fig = style_plotly_chart(fig, f'💰 Revenue by {dimension.title()}', height=350)
    fig.update_layout(coloraxis_showscale=False)
    
    return fig


def create_margin_by_category_chart(sales_df, products_df):
    """Create margin % by category chart with defensive checks."""
    if sales_df is None or sales_df.empty or products_df is None or products_df.empty:
        return None
    
    required_sales_cols = ['product_id', 'payment_status', 'qty', 'selling_price_aed']
    if not all(col in sales_df.columns for col in required_sales_cols):
        return None
    
    required_product_cols = ['product_id', 'unit_cost_aed', 'category']
    if not all(col in products_df.columns for col in required_product_cols):
        return None
    
    df = sales_df.merge(
        products_df[['product_id', 'unit_cost_aed', 'category']],
        on='product_id',
        how='left'
    )
    
    df = df[df['payment_status'] == 'Paid']
    
    if df.empty:
        return None
    
    df['revenue'] = df['qty'] * df['selling_price_aed']
    df['cost'] = df['qty'] * df['unit_cost_aed']
    
    grouped = df.groupby('category').agg({
        'revenue': 'sum',
        'cost': 'sum'
    }).reset_index()
    
    grouped['margin_pct'] = ((grouped['revenue'] - grouped['cost']) / grouped['revenue'] * 100).round(1)
    grouped = grouped.sort_values('margin_pct', ascending=True)
    
    if grouped.empty:
        return None
    
    colors = [COLORS['danger'] if x < 20 else COLORS['warning'] if x < 35 else COLORS['success'] 
              for x in grouped['margin_pct']]
    
    fig = go.Figure(go.Bar(
        x=grouped['margin_pct'],
        y=grouped['category'],
        orientation='h',
        marker_color=colors,
        text=[f'{x:.1f}%' for x in grouped['margin_pct']],
        textposition='outside'
    ))
    
    fig = style_plotly_chart(fig, '📊 Gross Margin by Category', height=350)
    
    return fig


def create_scenario_impact_chart(scenario_df):
    """Create scenario comparison chart with defensive checks."""
    if scenario_df is None or scenario_df.empty:
        return None
    
    required_cols = ['Discount %', 'Profit Proxy', 'Margin %']
    if not all(col in scenario_df.columns for col in required_cols):
        return None
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=scenario_df['Discount %'],
            y=scenario_df['Profit Proxy'],
            name='Profit Proxy',
            marker_color=COLORS['primary'],
            marker_line_color=COLORS['secondary'],
            marker_line_width=1
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=scenario_df['Discount %'],
            y=scenario_df['Margin %'],
            name='Margin %',
            mode='lines+markers',
            line=dict(color=COLORS['success'], width=3),
            marker=dict(size=10, color=COLORS['success'])
        ),
        secondary_y=True
    )
    
    fig = style_plotly_chart(fig, '🎯 Scenario Impact Analysis', height=350)
    fig.update_yaxes(title_text='Profit Proxy (AED)', secondary_y=False, gridcolor='rgba(58,134,255,0.1)')
    fig.update_yaxes(title_text='Margin %', secondary_y=True, gridcolor='rgba(74,222,128,0.1)')
    
    return fig


def create_stockout_risk_chart(sim_results):
    """Create stockout risk by dimension chart with defensive checks."""
    if sim_results is None:
        return None
    
    details = sim_results.get('details', pd.DataFrame())
    
    if details is None or details.empty:
        return None
    
    if 'city' not in details.columns or 'stockout_flag' not in details.columns:
        return None
    
    risk_by_city = details.groupby('city').agg({
        'stockout_flag': ['sum', 'count']
    }).reset_index()
    risk_by_city.columns = ['City', 'At Risk', 'Total']
    risk_by_city['Risk %'] = (risk_by_city['At Risk'] / risk_by_city['Total'] * 100).round(1)
    
    if risk_by_city.empty:
        return None
    
    colors = [COLORS['success'] if x < 20 else COLORS['warning'] if x < 40 else COLORS['danger'] 
              for x in risk_by_city['Risk %']]
    
    fig = go.Figure(go.Bar(
        x=risk_by_city['City'],
        y=risk_by_city['Risk %'],
        marker_color=colors,
        text=[f'{x:.1f}%' for x in risk_by_city['Risk %']],
        textposition='outside'
    ))
    
    fig = style_plotly_chart(fig, '⚠️ Stockout Risk by City', height=350)
    
    return fig


def create_issues_pareto_chart(issues_df):
    """Create Pareto chart of issue types with defensive checks."""
    if issues_df is None or issues_df.empty:
        return None
    
    if 'issue_type' not in issues_df.columns:
        return None
    
    issue_counts = issues_df['issue_type'].value_counts().reset_index()
    issue_counts.columns = ['Issue Type', 'Count']
    issue_counts = issue_counts.sort_values('Count', ascending=False)
    issue_counts['Cumulative %'] = (issue_counts['Count'].cumsum() / issue_counts['Count'].sum() * 100).round(1)
    
    if issue_counts.empty:
        return None
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=issue_counts['Issue Type'],
            y=issue_counts['Count'],
            name='Count',
            marker_color=COLORS['danger'],
            marker_line_color=COLORS['warning'],
            marker_line_width=1
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=issue_counts['Issue Type'],
            y=issue_counts['Cumulative %'],
            name='Cumulative %',
            mode='lines+markers',
            line=dict(color=COLORS['secondary'], width=3),
            marker=dict(size=8, color=COLORS['secondary'])
        ),
        secondary_y=True
    )
    
    fig = style_plotly_chart(fig, '🔍 Data Quality Issues (Pareto)', height=350)
    fig.update_yaxes(title_text='Count', secondary_y=False)
    fig.update_yaxes(title_text='Cumulative %', secondary_y=True, range=[0, 105])
    
    return fig


def create_inventory_distribution_chart(inventory_df):
    """Create inventory distribution chart with defensive checks."""
    if inventory_df is None or inventory_df.empty:
        return None
    
    if 'stock_on_hand' not in inventory_df.columns:
        return None
    
    if 'snapshot_date' in inventory_df.columns and 'product_id' in inventory_df.columns and 'store_id' in inventory_df.columns:
        latest = inventory_df.sort_values('snapshot_date').groupby(
            ['product_id', 'store_id']
        ).last().reset_index()
    else:
        latest = inventory_df.copy()
    
    if latest.empty:
        return None
    
    fig = px.histogram(
        latest,
        x='stock_on_hand',
        nbins=30,
        color_discrete_sequence=[COLORS['primary']]
    )
    
    fig.update_traces(
        marker_line_color=COLORS['secondary'],
        marker_line_width=1
    )
    
    fig = style_plotly_chart(fig, '📦 Stock Distribution', height=350)
    fig.update_layout(bargap=0.1)
    
    return fig


def create_channel_performance_chart(sales_df):
    """Create channel performance donut chart with defensive checks."""
    if sales_df is None or sales_df.empty:
        return None
    
    if 'channel' not in sales_df.columns:
        return None
    
    required_cols = ['payment_status', 'qty', 'selling_price_aed']
    if not all(col in sales_df.columns for col in required_cols):
        return None
    
    df = sales_df[sales_df['payment_status'] == 'Paid'].copy()
    
    if df.empty:
        return None
    
    df['revenue'] = df['qty'] * df['selling_price_aed']
    
    channel_revenue = df.groupby('channel')['revenue'].sum().reset_index()
    
    if channel_revenue.empty:
        return None
    
    fig = go.Figure(go.Pie(
        labels=channel_revenue['channel'],
        values=channel_revenue['revenue'],
        hole=0.6,
        marker=dict(colors=CHART_COLORS[:len(channel_revenue)]),
        textinfo='label+percent',
        textposition='outside',
        textfont=dict(color='#e8e8e8')
    ))
    
    fig = style_plotly_chart(fig, '📱 Revenue by Channel', height=350)
    fig.update_layout(showlegend=False)
    
    return fig


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_data_from_upload(uploaded_file):
    """Load data from uploaded file."""
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
    """Create UI for mapping uploaded columns to expected schema."""
    st.markdown(f"**Map columns for {table_name}**")
    
    available_columns = ['-- Not Mapped --'] + list(df.columns)
    mapping = {}
    
    cols = st.columns(2)
    for i, (expected_col, description) in enumerate(expected_columns.items()):
        with cols[i % 2]:
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
    if value >= 1000000:
        return f"AED {value/1000000:.2f}M"
    elif value >= 1000:
        return f"AED {value/1000:.1f}K"
    return f"AED {value:,.0f}"


def format_percentage(value):
    """Format value as percentage."""
    return f"{value:.1f}%"


def format_number(value):
    """Format large numbers."""
    if value >= 1000000:
        return f"{value/1000000:.2f}M"
    elif value >= 1000:
        return f"{value/1000:.1f}K"
    return f"{value:,.0f}"


def generate_executive_recommendations(kpis, sim_results):
    """Generate AI recommendations for executives."""
    recommendations = []
    
    margin_pct = kpis.get('gross_margin_pct', 0)
    if margin_pct >= 40:
        recommendations.append({
            'icon': '✅',
            'text': f'<strong>Strong margin performance ({margin_pct:.1f}%)</strong> — Consider aggressive promotional spend to capture market share.',
            'type': 'success'
        })
    elif margin_pct >= 25:
        recommendations.append({
            'icon': '⚠️',
            'text': f'<strong>Moderate margins ({margin_pct:.1f}%)</strong> — Balance discounts carefully to maintain profitability.',
            'type': 'warning'
        })
    else:
        recommendations.append({
            'icon': '🔴',
            'text': f'<strong>Low margins ({margin_pct:.1f}%)</strong> — Avoid deep discounts; focus on high-margin categories.',
            'type': 'danger'
        })
    
    if sim_results:
        stockout_risk = sim_results['kpis'].get('stockout_risk_pct', 0)
        budget_util = sim_results['kpis'].get('budget_utilization', 0)
        
        if stockout_risk > 30:
            recommendations.append({
                'icon': '📦',
                'text': f'<strong>High stockout risk ({stockout_risk:.0f}%)</strong> — Consider inventory replenishment before campaign launch.',
                'type': 'warning'
            })
        
        if budget_util > 90:
            recommendations.append({
                'icon': '💰',
                'text': f'<strong>Budget nearly exhausted ({budget_util:.0f}%)</strong> — Reduce discount depth or narrow campaign scope.',
                'type': 'danger'
            })
        elif budget_util < 50:
            recommendations.append({
                'icon': '💡',
                'text': f'<strong>Budget underutilized ({budget_util:.0f}%)</strong> — Opportunity to expand promotional reach or increase discount.',
                'type': 'primary'
            })
        
        if not sim_results['constraints']['all_ok']:
            recommendations.append({
                'icon': '🚫',
                'text': '<strong>Constraint violations detected</strong> — Review and adjust simulation parameters before proceeding.',
                'type': 'danger'
            })
        else:
            recommendations.append({
                'icon': '✨',
                'text': '<strong>All constraints satisfied</strong> — Campaign parameters are within acceptable bounds.',
                'type': 'success'
            })
    
    return recommendations


# =============================================================================
# MAIN DASHBOARD
# =============================================================================

def main():
    """Main Streamlit application."""
    
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
    if 'cleaning_stats' not in st.session_state:
        st.session_state.cleaning_stats = {}
    
    # =========================================================================
    # SIDEBAR
    # =========================================================================
    with st.sidebar:
        st.markdown('<div class="sidebar-header">⚙️ Control Panel</div>', unsafe_allow_html=True)
        
        render_subtle_divider()
        
        # View Toggle
        st.markdown("**📊 Dashboard View**")
        view_mode = st.radio(
            "Select View",
            ["👔 Executive", "🔧 Manager"],
            horizontal=True,
            label_visibility="collapsed"
        )
        view_mode = "Executive" if "Executive" in view_mode else "Manager"
        
        render_subtle_divider()
        
        # Data Source Selection
        st.markdown("**📁 Data Source**")
        data_source = st.radio(
            "Choose data source",
            ["📤 Upload Custom", "📂 Load Generated"],
            label_visibility="collapsed"
        )
        
        render_subtle_divider()
        
        # Simulation Parameters
        st.markdown("**🎮 Simulation Parameters**")
        
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
            max_value=1000000,
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
            [7, 14, 21, 30],
            index=1,
            help="Number of days to simulate"
        )
        
        render_subtle_divider()
        
        # Filters
        st.markdown("**🔍 Filters**")
        
        city_filter = st.selectbox(
            "City",
            ["All"] + VALID_CITIES
        )
        
        channel_filter = st.selectbox(
            "Channel",
            ["All"] + VALID_CHANNELS
        )
        
        category_filter = st.selectbox(
            "Category",
            ["All"] + VALID_CATEGORIES
        )
    
    # =========================================================================
    # MAIN CONTENT
    # =========================================================================
    
    # Page Header
    render_page_header()
    
    # =========================================================================
    # DATA LOADING SECTION
    # =========================================================================
    
    if "Upload" in data_source:
        render_section_header("📤", "Upload Data Files", "Upload your CSV or Excel files")
        
        col1, col2 = st.columns(2)
        
        with col1:
            products_file = st.file_uploader(
                "📦 Products",
                type=['csv', 'xlsx', 'xls'],
                key='products_upload'
            )
            sales_file = st.file_uploader(
                "🛒 Sales",
                type=['csv', 'xlsx', 'xls'],
                key='sales_upload'
            )
        
        with col2:
            stores_file = st.file_uploader(
                "🏪 Stores",
                type=['csv', 'xlsx', 'xls'],
                key='stores_upload'
            )
            inventory_file = st.file_uploader(
                "📊 Inventory",
                type=['csv', 'xlsx', 'xls'],
                key='inventory_upload'
            )
        
        # Column Mapping Section
        if any([products_file, stores_file, sales_file, inventory_file]):
            render_divider()
            render_section_header("🔗", "Column Mapping", "Map your columns to the expected schema")
            
            with st.expander("📦 Map Product Columns", expanded=products_file is not None):
                if products_file:
                    products_raw = load_data_from_upload(products_file)
                    if products_raw is not None:
                        st.dataframe(products_raw.head(3), use_container_width=True)
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
            
            with st.expander("🏪 Map Store Columns", expanded=stores_file is not None):
                if stores_file:
                    stores_raw = load_data_from_upload(stores_file)
                    if stores_raw is not None:
                        st.dataframe(stores_raw.head(3), use_container_width=True)
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
            
            with st.expander("🛒 Map Sales Columns", expanded=sales_file is not None):
                if sales_file:
                    sales_raw = load_data_from_upload(sales_file)
                    if sales_raw is not None:
                        st.dataframe(sales_raw.head(3), use_container_width=True)
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
            
            with st.expander("📊 Map Inventory Columns", expanded=inventory_file is not None):
                if inventory_file:
                    inventory_raw = load_data_from_upload(inventory_file)
                    if inventory_raw is not None:
                        st.dataframe(inventory_raw.head(3), use_container_width=True)
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
            
            st.markdown("")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🚀 Process & Clean Data", type="primary", use_container_width=True):
                    with st.spinner("🔄 Cleaning data..."):
                        cleaner = DataCleaner()
                        cleaned = {}
                        
                        if 'products' in st.session_state.raw_data and 'products_mapping' in st.session_state.raw_data:
                            mapped_products = apply_column_mapping(
                                st.session_state.raw_data['products'],
                                st.session_state.raw_data['products_mapping']
                            )
                            cleaned['products'] = cleaner.clean_products(mapped_products)
                        else:
                            cleaned['products'] = pd.DataFrame()
                        
                        if 'stores' in st.session_state.raw_data and 'stores_mapping' in st.session_state.raw_data:
                            mapped_stores = apply_column_mapping(
                                st.session_state.raw_data['stores'],
                                st.session_state.raw_data['stores_mapping']
                            )
                            cleaned['stores'] = cleaner.clean_stores(mapped_stores)
                        else:
                            cleaned['stores'] = pd.DataFrame()
                        
                        if 'sales' in st.session_state.raw_data and 'sales_mapping' in st.session_state.raw_data:
                            mapped_sales = apply_column_mapping(
                                st.session_state.raw_data['sales'],
                                st.session_state.raw_data['sales_mapping']
                            )
                            cleaned['sales'] = cleaner.clean_sales(mapped_sales)
                        else:
                            cleaned['sales'] = pd.DataFrame()
                        
                        if 'inventory' in st.session_state.raw_data and 'inventory_mapping' in st.session_state.raw_data:
                            mapped_inventory = apply_column_mapping(
                                st.session_state.raw_data['inventory'],
                                st.session_state.raw_data['inventory_mapping']
                            )
                            cleaned['inventory'] = cleaner.clean_inventory(mapped_inventory)
                        else:
                            cleaned['inventory'] = pd.DataFrame()
                        
                        st.session_state.cleaned_data = cleaned
                        st.session_state.issues_log = cleaner.get_issues_dataframe()
                        st.session_state.cleaning_stats = cleaner.cleaning_stats
                        st.session_state.data_loaded = True
                        
                        st.success("✅ Data cleaned successfully!")
                        st.rerun()
    
    else:  # Load Generated Data
        render_section_header("📂", "Load Generated Data", "Upload the CSV files from data_generator.py")
        
        col1, col2 = st.columns(2)
        
        with col1:
            products_file = st.file_uploader("📦 products.csv", type=['csv'], key='gen_products')
            sales_file = st.file_uploader("🛒 sales_raw.csv", type=['csv'], key='gen_sales')
        
        with col2:
            stores_file = st.file_uploader("🏪 stores.csv", type=['csv'], key='gen_stores')
            inventory_file = st.file_uploader("📊 inventory_snapshot.csv", type=['csv'], key='gen_inventory')
        
        st.markdown("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Load & Clean Data", type="primary", use_container_width=True):
                if all([products_file, stores_file, sales_file, inventory_file]):
                    with st.spinner("🔄 Loading and cleaning data..."):
                        cleaner = DataCleaner()
                        
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
                    st.warning("⚠️ Please upload all 4 data files.")
    
    # =========================================================================
    # MAIN DASHBOARD (Only show if data is loaded)
    # =========================================================================
    
    if st.session_state.data_loaded:
        render_divider()
        
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
            render_section_header("👔", "Executive Dashboard", "Financial KPIs & Strategic Insights")
            
            # KPI Cards Row
            st.markdown("")
            kpis_row1 = [
                {
                    'icon': '💰',
                    'value': format_currency(historical_kpis['net_revenue']),
                    'label': 'Net Revenue',
                    'card_type': 'primary'
                },
                {
                    'icon': '📈',
                    'value': format_percentage(historical_kpis['gross_margin_pct']),
                    'label': 'Gross Margin',
                    'delta': 'Historical',
                    'delta_type': 'neutral',
                    'card_type': 'success' if historical_kpis['gross_margin_pct'] >= 30 else 'warning'
                },
                {
                    'icon': '🎯',
                    'value': format_currency(sim_results['kpis']['profit_proxy']),
                    'label': 'Profit Proxy (Sim)',
                    'card_type': 'primary'
                },
                {
                    'icon': '💳',
                    'value': format_percentage(sim_results['kpis']['budget_utilization']),
                    'label': 'Budget Utilization',
                    'card_type': 'success' if sim_results['kpis']['budget_utilization'] <= 80 else 'warning'
                }
            ]
            render_kpi_row(kpis_row1)
            
            render_subtle_divider()
            
            # Charts Row 1
            col1, col2 = st.columns(2)
            
            with col1:
                sales_with_store = sales_df.merge(
                    stores_df[['store_id', 'city', 'channel']],
                    on='store_id',
                    how='left'
                ) if not sales_df.empty and not stores_df.empty and 'store_id' in sales_df.columns and 'store_id' in stores_df.columns else sales_df
                
                fig = create_revenue_trend_chart(sales_with_store)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Revenue trend chart requires sales data with order_time, qty, and selling_price_aed.', 'warning')
            
            with col2:
                fig = create_revenue_by_dimension_chart(sales_with_store, 'city')
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Revenue by city chart requires sales data with city dimension.', 'warning')
            
            # Charts Row 2
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_margin_by_category_chart(sales_df, products_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Margin by category chart requires sales and products data.', 'warning')
            
            with col2:
                fig = create_scenario_impact_chart(scenario_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Scenario impact chart requires simulation results.', 'warning')
            
            render_subtle_divider()
            
            # Constraint Status
            render_section_header("🔒", "Constraint Status")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                render_constraint_card(
                    '💰',
                    'Budget Constraint',
                    'Within Limit' if sim_results['constraints']['budget_ok'] else 'Exceeded',
                    sim_results['constraints']['budget_ok']
                )
            
            with col2:
                render_constraint_card(
                    '📊',
                    'Margin Floor',
                    'Above Floor' if sim_results['constraints']['margin_ok'] else 'Below Floor',
                    sim_results['constraints']['margin_ok']
                )
            
            with col3:
                render_constraint_card(
                    '✅',
                    'All Constraints',
                    'All Passed' if sim_results['constraints']['all_ok'] else 'Violations Detected',
                    sim_results['constraints']['all_ok']
                )
            
            render_subtle_divider()
            
            # Scenario Comparison Table
            render_section_header("📊", "Scenario Comparison")
            if not scenario_df.empty:
                st.dataframe(
                    scenario_df.style.format({
                        'Simulated Revenue': 'AED {:,.0f}',
                        'Profit Proxy': 'AED {:,.0f}',
                        'Margin %': '{:.1f}%',
                        'Stockout Risk %': '{:.1f}%',
                        'Budget Used %': '{:.1f}%'
                    }),
                    use_container_width=True,
                    height=280
                )
            else:
                render_insight_box('📊', 'No Data', 'Scenario comparison requires simulation to run.', 'warning')
            
            render_subtle_divider()
            
            # Recommendation Box
            recommendations = generate_executive_recommendations(historical_kpis, sim_results)
            render_recommendation_box(recommendations)
        
        # =====================================================================
        # MANAGER VIEW
        # =====================================================================
        else:
            render_section_header("🔧", "Manager Dashboard", "Operational Metrics & Risk Analysis")
            
            # KPI Cards Row
            st.markdown("")
            kpis_row1 = [
                {
                    'icon': '⚠️',
                    'value': format_percentage(sim_results['kpis']['stockout_risk_pct']),
                    'label': 'Stockout Risk',
                    'card_type': 'danger' if sim_results['kpis']['stockout_risk_pct'] > 30 else 'warning' if sim_results['kpis']['stockout_risk_pct'] > 15 else 'success'
                },
                {
                    'icon': '↩️',
                    'value': format_percentage(historical_kpis['return_rate']),
                    'label': 'Return Rate',
                    'card_type': 'success' if historical_kpis['return_rate'] < 5 else 'warning'
                },
                {
                    'icon': '❌',
                    'value': format_percentage(historical_kpis['payment_failure_rate']),
                    'label': 'Payment Failure',
                    'card_type': 'success' if historical_kpis['payment_failure_rate'] < 10 else 'danger'
                },
                {
                    'icon': '📦',
                    'value': format_number(sim_results['kpis']['products_at_risk']),
                    'label': 'High-Risk SKUs',
                    'card_type': 'danger' if sim_results['kpis']['products_at_risk'] > 50 else 'warning' if sim_results['kpis']['products_at_risk'] > 20 else 'success'
                }
            ]
            render_kpi_row(kpis_row1)
            
            render_subtle_divider()
            
            # Charts Row 1
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_stockout_risk_chart(sim_results)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Stockout risk chart requires simulation results with city data.', 'warning')
            
            with col2:
                fig = create_issues_pareto_chart(issues_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('✅', 'No Issues', 'No data quality issues found!', 'success')
            
            # Charts Row 2
            col1, col2 = st.columns(2)
            
            with col1:
                fig = create_inventory_distribution_chart(inventory_df)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Inventory distribution chart requires inventory data.', 'warning')
            
            with col2:
                sales_with_store = sales_df.merge(
                    stores_df[['store_id', 'city', 'channel']],
                    on='store_id',
                    how='left'
                ) if not sales_df.empty and not stores_df.empty and 'store_id' in sales_df.columns and 'store_id' in stores_df.columns else sales_df
                
                fig = create_channel_performance_chart(sales_with_store)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    render_insight_box('📊', 'No Data', 'Channel performance chart requires sales data with channel dimension.', 'warning')
            
            render_subtle_divider()
            
            # Top 10 Stockout Risk Table
            render_section_header("🚨", "Top 10 Stockout Risk Items")
            top_stockout = sim_results.get('top_stockout_items', pd.DataFrame())
            if not top_stockout.empty:
                st.dataframe(
                    top_stockout.style.format({
                        'Projected Demand': '{:.0f}',
                        'Stock Available': '{:.0f}'
                    }),
                    use_container_width=True,
                    height=350
                )
            else:
                render_insight_box(
                    '✅',
                    'No Stockout Risks',
                    'No stockout risks detected for current simulation parameters. Inventory levels are sufficient to meet projected demand.',
                    'success'
                )
            
            render_subtle_divider()
            
            # Data Quality Summary
            render_section_header("🔍", "Data Quality Summary")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                render_status_box("Total Issues", format_number(len(issues_df)), "warning" if len(issues_df) > 100 else "success")
            
            with col2:
                if not issues_df.empty and 'issue_type' in issues_df.columns:
                    top_issue = issues_df['issue_type'].value_counts().index[0]
                    render_status_box("Top Issue Type", top_issue.replace('_', ' ').title(), "primary")
                else:
                    render_status_box("Top Issue Type", "None", "success")
            
            with col3:
                tables_cleaned = len(st.session_state.cleaning_stats) if st.session_state.cleaning_stats else 0
                render_status_box("Tables Cleaned", str(tables_cleaned), "primary")
            
            with col4:
                total_records = sum(stats.get('original', 0) for stats in st.session_state.cleaning_stats.values()) if st.session_state.cleaning_stats else 0
                render_status_box("Records Processed", format_number(total_records), "primary")
            
            # Issues Log Expander
            if not issues_df.empty:
                with st.expander("📋 View Full Issues Log"):
                    st.dataframe(issues_df, use_container_width=True, height=400)
        
        # =====================================================================
        # DOWNLOAD SECTION (Common to both views)
        # =====================================================================
        render_divider()
        render_section_header("📥", "Download Data")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if not sales_df.empty:
                st.download_button(
                    label="⬇️ Cleaned Sales",
                    data=convert_df_to_csv(sales_df),
                    file_name="cleaned_sales.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        
        with col2:
            if not issues_df.empty:
                st.download_button(
                    label="⬇️ Issues Log",
                    data=convert_df_to_csv(issues_df),
                    file_name="issues.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        
        with col3:
            if not scenario_df.empty:
                st.download_button(
                    label="⬇️ Scenarios",
                    data=convert_df_to_csv(scenario_df),
                    file_name="scenarios.csv",
                    mime="text/csv",
                    use_container_width=True
                )
    
    else:
        # No data loaded yet
        render_insight_box(
            '👆',
            'Getting Started',
            'Please upload your data files using the options above to begin analysis. You can either upload custom CSV/Excel files or load the pre-generated synthetic data from <code>data_generator.py</code>.',
            'primary'
        )
        
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
    render_footer()


# =============================================================================
# RUN APPLICATION
# =============================================================================
if __name__ == "__main__":
    main()
