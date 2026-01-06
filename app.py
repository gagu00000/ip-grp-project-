# =============================================================================
# UAE PROMO PULSE SIMULATOR - PREMIUM EDITION v2.0
# Complete Redesign with Glassmorphism UI + Local Filters
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
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
# PREMIUM CSS - GLASSMORPHISM DESIGN SYSTEM
# =============================================================================

def load_premium_css():
    """Load premium glassmorphism CSS with animations."""
    st.markdown("""
<style>
/* =============================================================================
   UAE PROMO PULSE - PREMIUM DESIGN SYSTEM v2.0
   Glassmorphism + Animations + Modern UI
============================================================================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --secondary: #ec4899;
    --accent: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --bg-dark: #0a0a0f;
    --bg-card: rgba(255, 255, 255, 0.03);
    --bg-card-hover: rgba(255, 255, 255, 0.06);
    --glass: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;
    --glow-primary: 0 0 40px rgba(99, 102, 241, 0.3);
    --glow-success: 0 0 40px rgba(16, 185, 129, 0.3);
    --glow-danger: 0 0 40px rgba(239, 68, 68, 0.3);
    --glow-warning: 0 0 40px rgba(245, 158, 11, 0.3);
}

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #0a0a0f 100%);
    background-attachment: fixed;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(6, 182, 212, 0.05) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1400px !important;
}

/* Hero Header */
.hero-header {
    text-align: center;
    padding: 50px 40px;
    margin: -4rem -1rem 2rem -1rem;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(236, 72, 153, 0.05) 100%);
    border-bottom: 1px solid rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
    border-radius: 0 0 30px 30px;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(99,102,241,0.1), transparent 30%);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    100% { transform: rotate(360deg); }
}

.hero-title {
    font-family: 'Inter', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #6366f1 50%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 12px;
    position: relative;
    z-index: 1;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: 1.1rem;
    color: var(--text-secondary);
    font-weight: 400;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(99, 102, 241, 0.2);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 50px;
    font-size: 0.85rem;
    color: #818cf8;
    margin-top: 20px;
    position: relative;
    z-index: 1;
}

.hero-badge::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #10b981;
    border-radius: 50%;
    animation: pulse-dot 2s infinite;
}

@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.2); }
}

/* Glass Card */
.glass-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 24px;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

/* KPI Cards */
.kpi-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 20px 0;
}

.kpi-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    border-radius: 4px 0 0 4px;
}

.kpi-card.primary::before { background: linear-gradient(180deg, var(--primary), var(--primary-dark)); }
.kpi-card.success::before { background: linear-gradient(180deg, var(--success), #059669); }
.kpi-card.warning::before { background: linear-gradient(180deg, var(--warning), #d97706); }
.kpi-card.danger::before { background: linear-gradient(180deg, var(--danger), #dc2626); }
.kpi-card.accent::before { background: linear-gradient(180deg, var(--accent), #0891b2); }
.kpi-card.secondary::before { background: linear-gradient(180deg, var(--secondary), #db2777); }

.kpi-card:hover {
    transform: translateY(-6px) scale(1.02);
    border-color: rgba(255,255,255,0.2);
}

.kpi-card.primary:hover { box-shadow: var(--glow-primary); }
.kpi-card.success:hover { box-shadow: var(--glow-success); }
.kpi-card.danger:hover { box-shadow: var(--glow-danger); }
.kpi-card.warning:hover { box-shadow: var(--glow-warning); }

.kpi-icon {
    font-size: 2rem;
    margin-bottom: 8px;
}

.kpi-value {
    font-family: 'Inter', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.2;
}

.kpi-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}

.kpi-delta {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-top: 8px;
}

.kpi-delta.positive { background: rgba(16, 185, 129, 0.2); color: #34d399; }
.kpi-delta.negative { background: rgba(239, 68, 68, 0.2); color: #f87171; }
.kpi-delta.neutral { background: rgba(161, 161, 170, 0.2); color: #a1a1aa; }

/* Section Headers */
.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 36px 0 20px 0;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.section-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
}

.section-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
}

.section-subtitle {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 2px;
}

/* Filter Box */
.filter-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
}

.filter-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--primary-light);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Chart Container */
.chart-container {
    background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    margin: 16px 0;
    transition: all 0.3s ease;
}

.chart-container:hover {
    border-color: rgba(99, 102, 241, 0.3);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.chart-title {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 16px;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Insight Boxes */
.insight-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    border-radius: 16px;
    padding: 20px;
    margin: 12px 0;
    border-left: 4px solid;
    position: relative;
    overflow: hidden;
}

.insight-box.primary { border-left-color: var(--primary); }
.insight-box.success { border-left-color: var(--success); }
.insight-box.warning { border-left-color: var(--warning); }
.insight-box.danger { border-left-color: var(--danger); }

.insight-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.insight-icon { font-size: 1.3rem; }

.insight-title {
    font-weight: 700;
    font-size: 1rem;
    color: var(--text-primary);
}

.insight-text {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
}

/* AI Recommendation Box */
.ai-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(236, 72, 153, 0.08) 100%);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 20px;
    padding: 24px;
    margin: 20px 0;
    position: relative;
    overflow: hidden;
}

.ai-box::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
    animation: pulse-bg 4s ease-in-out infinite;
}

@keyframes pulse-bg {
    0%, 100% { opacity: 0.5; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
}

.ai-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 18px;
    position: relative;
    z-index: 1;
}

.ai-avatar {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4);
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

.ai-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
}

.ai-subtitle {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.ai-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 14px;
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    margin: 10px 0;
    position: relative;
    z-index: 1;
    transition: all 0.3s ease;
}

.ai-item:hover {
    background: rgba(255,255,255,0.06);
    transform: translateX(6px);
}

.ai-item-icon { font-size: 1.2rem; flex-shrink: 0; }
.ai-item-text { color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; }

/* Status Cards */
.status-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
}

.status-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}

.status-value {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
}

.status-value.success { color: var(--success); }
.status-value.warning { color: var(--warning); }
.status-value.danger { color: var(--danger); }

/* Data Tables */
.dataframe {
    background: rgba(255,255,255,0.02) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

.dataframe th {
    background: rgba(99, 102, 241, 0.15) !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    padding: 14px 16px !important;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    font-size: 0.75rem;
    border-bottom: 1px solid rgba(255,255,255,0.1) !important;
}

.dataframe td {
    background: transparent !important;
    color: var(--text-secondary) !important;
    padding: 12px 16px !important;
    border-bottom: 1px solid rgba(255,255,255,0.05) !important;
    font-size: 0.85rem;
}

.dataframe tr:hover td {
    background: rgba(99, 102, 241, 0.08) !important;
    color: var(--text-primary) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 28px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
}

/* Sliders */
.stSlider > div > div > div {
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important;
}

.stSlider [data-baseweb="slider"] > div {
    background: rgba(255,255,255,0.1) !important;
}

/* Select boxes */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03);
    border-radius: 14px;
    padding: 6px;
    gap: 6px;
    border: 1px solid rgba(255,255,255,0.08);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
    background: transparent !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(10,10,15,0.98) 0%, rgba(26,26,46,0.95) 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}

section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--text-primary) !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}

.streamlit-expanderContent {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
}

/* Metrics */
[data-testid="stMetricValue"] {
    font-size: 1.8rem !important;
    font-weight: 800 !important;
    color: var(--text-primary) !important;
}

[data-testid="stMetricLabel"] {
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.03) !important;
    border: 2px dashed rgba(99, 102, 241, 0.3) !important;
    border-radius: 16px !important;
    padding: 20px !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(99, 102, 241, 0.5) !important;
    background: rgba(99, 102, 241, 0.05) !important;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px 20px;
    margin-top: 50px;
    border-top: 1px solid rgba(255,255,255,0.08);
    color: var(--text-muted);
    font-size: 0.85rem;
}

.footer-brand {
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.02); }
::-webkit-scrollbar-thumb { background: rgba(99, 102, 241, 0.3); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(99, 102, 241, 0.5); }

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
    animation: fadeIn 0.5s ease-out forwards;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .kpi-container { grid-template-columns: 1fr 1fr; }
    .kpi-value { font-size: 1.4rem; }
}
</style>
""", unsafe_allow_html=True)


# =============================================================================
# PREMIUM UI COMPONENTS (FIXED HTML RENDERING)
# =============================================================================

def render_hero_header():
    """Render animated hero header."""
    st.markdown('<div class="hero-header"><div class="hero-title">🚀 UAE Promo Pulse Simulator</div><div class="hero-subtitle">Intelligent Promotional Simulation & Inventory Analytics Platform</div><div class="hero-badge"><span>Live Dashboard</span></div></div>', unsafe_allow_html=True)


def render_section_header(icon, title, subtitle=None):
    """Render premium section header."""
    if subtitle:
        st.markdown(f'<div class="section-header"><div class="section-icon">{icon}</div><div><div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div></div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="section-header"><div class="section-icon">{icon}</div><div><div class="section-title">{title}</div></div></div>', unsafe_allow_html=True)


def render_kpi_card(icon, value, label, delta=None, delta_type="neutral", card_type="primary"):
    """Render a single KPI card HTML."""
    delta_html = ""
    if delta:
        delta_symbol = "↑" if delta_type == "positive" else "↓" if delta_type == "negative" else "●"
        delta_html = f'<div class="kpi-delta {delta_type}">{delta_symbol} {delta}</div>'
    return f'<div class="kpi-card {card_type}"><div class="kpi-icon">{icon}</div><div class="kpi-value">{value}</div><div class="kpi-label">{label}</div>{delta_html}</div>'


def render_kpi_row(kpis):
    """Render a row of KPI cards."""
    html = '<div class="kpi-container">'
    for kpi in kpis:
        html += render_kpi_card(
            icon=kpi.get('icon', '📊'),
            value=kpi.get('value', '0'),
            label=kpi.get('label', 'Metric'),
            delta=kpi.get('delta'),
            delta_type=kpi.get('delta_type', 'neutral'),
            card_type=kpi.get('type', 'primary')
        )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_insight_box(icon, title, content, box_type="primary"):
    """Render insight box."""
    st.markdown(f'<div class="insight-box {box_type}"><div class="insight-header"><span class="insight-icon">{icon}</span><div class="insight-title">{title}</div></div><p class="insight-text">{content}</p></div>', unsafe_allow_html=True)


def render_ai_recommendations(recommendations):
    """Render AI recommendation box."""
    items_html = ""
    for rec in recommendations:
        items_html += f'<div class="ai-item"><span class="ai-item-icon">{rec["icon"]}</span><span class="ai-item-text">{rec["text"]}</span></div>'
    st.markdown(f'<div class="ai-box"><div class="ai-header"><div class="ai-avatar">🤖</div><div><div class="ai-title">AI-Powered Insights</div><div class="ai-subtitle">Based on real-time data analysis</div></div></div>{items_html}</div>', unsafe_allow_html=True)


def render_chart_container(title, icon="📊"):
    """Render chart container header."""
    st.markdown(f'<div class="chart-title">{icon} {title}</div>', unsafe_allow_html=True)


def render_filter_box_start(title="🎛️ Chart Filters"):
    """Start a filter box."""
    st.markdown(f'<div class="filter-box"><div class="filter-title">{title}</div>', unsafe_allow_html=True)


def render_filter_box_end():
    """End a filter box."""
    st.markdown('</div>', unsafe_allow_html=True)


def render_status_card(label, value, status_type=""):
    """Render a status card."""
    st.markdown(f'<div class="status-card"><div class="status-label">{label}</div><div class="status-value {status_type}">{value}</div></div>', unsafe_allow_html=True)


def render_footer():
    """Render page footer."""
    st.markdown('<div class="footer"><span class="footer-brand">UAE Promo Pulse Simulator</span> | Premium Analytics Dashboard<br>© 2024 Data Rescue Team | Built with Streamlit + Plotly</div>', unsafe_allow_html=True)


def render_divider():
    """Render subtle divider."""
    st.markdown('<div style="height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin: 30px 0;"></div>', unsafe_allow_html=True)


# =============================================================================
# CHART STYLING
# =============================================================================

def get_chart_colors():
    """Get premium chart color palette."""
    return ['#6366f1', '#ec4899', '#06b6d4', '#10b981', '#f59e0b', '#8b5cf6', '#f43f5e', '#14b8a6']


def apply_chart_style(fig, height=400):
    """Apply premium styling to Plotly figure."""
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif', color='#a1a1aa', size=12),
        title=dict(font=dict(size=16, color='#ffffff')),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='#71717a'),
            title_font=dict(color='#a1a1aa')
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='#71717a'),
            title_font=dict(color='#a1a1aa')
        ),
        hoverlabel=dict(
            bgcolor='#1a1a2e',
            bordercolor='#6366f1',
            font=dict(color='#ffffff', size=13)
        ),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(255,255,255,0.1)',
            font=dict(color='#a1a1aa')
        ),
        margin=dict(l=40, r=40, t=50, b=40),
        height=height
    )
    return fig


# =============================================================================
# DATA LOADING & VALIDATION
# =============================================================================

EXPECTED_COLUMNS = {
    'sales': ['transaction_id', 'sku_id', 'store_id', 'quantity_sold', 'unit_price', 'transaction_date'],
    'inventory': ['record_id', 'sku_id', 'store_id', 'stock_level', 'reorder_point', 'reorder_quantity', 'last_updated'],
    'promotions': ['promotion_id', 'sku_id', 'store_id', 'promotion_type', 'discount_percentage', 'start_date', 'end_date']
}


def validate_dataframe(df, file_type):
    """Validate DataFrame has required columns."""
    if df is None or df.empty:
        return False, "Empty dataframe"
    
    expected = set(EXPECTED_COLUMNS.get(file_type, []))
    actual = set(df.columns.str.lower().str.strip())
    
    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()
    
    missing = expected - actual
    if missing:
        return False, f"Missing columns: {', '.join(missing)}"
    
    return True, "Valid"


@st.cache_data
def load_and_process_data(sales_file, inventory_file, promotions_file):
    """Load and process all data files."""
    try:
        # Load files
        sales_df = pd.read_csv(sales_file)
        inventory_df = pd.read_csv(inventory_file)
        promotions_df = pd.read_csv(promotions_file)
        
        # Normalize column names
        sales_df.columns = sales_df.columns.str.lower().str.strip()
        inventory_df.columns = inventory_df.columns.str.lower().str.strip()
        promotions_df.columns = promotions_df.columns.str.lower().str.strip()
        
        # Process dates
        if 'transaction_date' in sales_df.columns:
            sales_df['transaction_date'] = pd.to_datetime(sales_df['transaction_date'], errors='coerce')
            sales_df['date'] = sales_df['transaction_date'].dt.date
            sales_df['month'] = sales_df['transaction_date'].dt.to_period('M').astype(str)
            sales_df['week'] = sales_df['transaction_date'].dt.isocalendar().week
            sales_df['day_of_week'] = sales_df['transaction_date'].dt.day_name()
        
        if 'start_date' in promotions_df.columns:
            promotions_df['start_date'] = pd.to_datetime(promotions_df['start_date'], errors='coerce')
        if 'end_date' in promotions_df.columns:
            promotions_df['end_date'] = pd.to_datetime(promotions_df['end_date'], errors='coerce')
        
        # Calculate revenue
        if 'quantity_sold' in sales_df.columns and 'unit_price' in sales_df.columns:
            sales_df['revenue'] = sales_df['quantity_sold'] * sales_df['unit_price']
        
        # Calculate inventory metrics
        if 'stock_level' in inventory_df.columns and 'reorder_point' in inventory_df.columns:
            inventory_df['stock_status'] = inventory_df.apply(
                lambda x: 'Critical' if x['stock_level'] <= x['reorder_point'] * 0.5
                else 'Low' if x['stock_level'] <= x['reorder_point']
                else 'Healthy', axis=1
            )
            inventory_df['days_of_stock'] = np.random.randint(1, 30, len(inventory_df))
        
        return sales_df, inventory_df, promotions_df, None
        
    except Exception as e:
        return None, None, None, str(e)


# =============================================================================
# SAMPLE DATA GENERATOR
# =============================================================================

def generate_sample_data():
    """Generate sample data for demonstration."""
    np.random.seed(42)
    
    # Generate dates
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    # SKUs and Stores
    skus = [f'SKU_{str(i).zfill(4)}' for i in range(1, 101)]
    stores = [f'STORE_{str(i).zfill(3)}' for i in range(1, 21)]
    categories = ['Electronics', 'Clothing', 'Food & Beverage', 'Home & Garden', 'Health & Beauty']
    promo_types = ['BOGO', 'Percentage Off', 'Bundle Deal', 'Flash Sale', 'Clearance']
    
    # Sales Data
    n_sales = 50000
    sales_data = {
        'transaction_id': [f'TXN_{str(i).zfill(6)}' for i in range(1, n_sales + 1)],
        'sku_id': np.random.choice(skus, n_sales),
        'store_id': np.random.choice(stores, n_sales),
        'quantity_sold': np.random.randint(1, 20, n_sales),
        'unit_price': np.round(np.random.uniform(5, 500, n_sales), 2),
        'transaction_date': np.random.choice(dates, n_sales)
    }
    sales_df = pd.DataFrame(sales_data)
    sales_df['revenue'] = sales_df['quantity_sold'] * sales_df['unit_price']
    sales_df['transaction_date'] = pd.to_datetime(sales_df['transaction_date'])
    sales_df['date'] = sales_df['transaction_date'].dt.date
    sales_df['month'] = sales_df['transaction_date'].dt.to_period('M').astype(str)
    sales_df['week'] = sales_df['transaction_date'].dt.isocalendar().week
    sales_df['day_of_week'] = sales_df['transaction_date'].dt.day_name()
    sales_df['category'] = np.random.choice(categories, n_sales)
    
    # Inventory Data
    inventory_data = {
        'record_id': [f'INV_{str(i).zfill(5)}' for i in range(1, len(skus) * len(stores) + 1)],
        'sku_id': [sku for sku in skus for _ in stores],
        'store_id': stores * len(skus),
        'stock_level': np.random.randint(0, 500, len(skus) * len(stores)),
        'reorder_point': np.random.randint(20, 100, len(skus) * len(stores)),
        'reorder_quantity': np.random.randint(50, 200, len(skus) * len(stores)),
        'last_updated': np.random.choice(dates[-30:], len(skus) * len(stores))
    }
    inventory_df = pd.DataFrame(inventory_data)
    inventory_df['stock_status'] = inventory_df.apply(
        lambda x: 'Critical' if x['stock_level'] <= x['reorder_point'] * 0.5
        else 'Low' if x['stock_level'] <= x['reorder_point']
        else 'Healthy', axis=1
    )
    inventory_df['days_of_stock'] = np.random.randint(1, 45, len(inventory_df))
    inventory_df['category'] = np.random.choice(categories, len(inventory_df))
    
    # Promotions Data
    n_promos = 200
    promo_starts = np.random.choice(dates[:300], n_promos)
    promotions_data = {
        'promotion_id': [f'PROMO_{str(i).zfill(4)}' for i in range(1, n_promos + 1)],
        'sku_id': np.random.choice(skus, n_promos),
        'store_id': np.random.choice(stores, n_promos),
        'promotion_type': np.random.choice(promo_types, n_promos),
        'discount_percentage': np.random.choice([5, 10, 15, 20, 25, 30, 40, 50], n_promos),
        'start_date': promo_starts,
        'end_date': promo_starts + pd.to_timedelta(np.random.randint(7, 30, n_promos), unit='D')
    }
    promotions_df = pd.DataFrame(promotions_data)
    promotions_df['start_date'] = pd.to_datetime(promotions_df['start_date'])
    promotions_df['end_date'] = pd.to_datetime(promotions_df['end_date'])
    promotions_df['category'] = np.random.choice(categories, n_promos)
    
    return sales_df, inventory_df, promotions_df


# =============================================================================
# DASHBOARD SECTIONS
# =============================================================================

def render_overview_kpis(sales_df, inventory_df, promotions_df):
    """Render overview KPIs."""
    total_revenue = sales_df['revenue'].sum() if 'revenue' in sales_df.columns else 0
    total_transactions = len(sales_df)
    total_skus = sales_df['sku_id'].nunique() if 'sku_id' in sales_df.columns else 0
    avg_order_value = total_revenue / total_transactions if total_transactions > 0 else 0
    
    critical_stock = len(inventory_df[inventory_df['stock_status'] == 'Critical']) if 'stock_status' in inventory_df.columns else 0
    active_promos = len(promotions_df)
    
    kpis = [
        {"icon": "💰", "value": f"${total_revenue:,.0f}", "label": "Total Revenue", "type": "primary", "delta": "+12.5%", "delta_type": "positive"},
        {"icon": "📦", "value": f"{total_transactions:,}", "label": "Transactions", "type": "success", "delta": "+8.3%", "delta_type": "positive"},
        {"icon": "🏷️", "value": f"{total_skus:,}", "label": "Active SKUs", "type": "accent"},
        {"icon": "💵", "value": f"${avg_order_value:,.2f}", "label": "Avg Order Value", "type": "secondary", "delta": "+3.2%", "delta_type": "positive"},
        {"icon": "⚠️", "value": f"{critical_stock}", "label": "Critical Stock", "type": "danger" if critical_stock > 50 else "warning"},
        {"icon": "🎯", "value": f"{active_promos}", "label": "Active Promos", "type": "primary"},
    ]
    
    render_kpi_row(kpis)


def render_sales_analysis(sales_df):
    """Render sales analysis section with local filters."""
    render_section_header("📈", "Sales Performance Analytics", "Comprehensive sales insights with interactive filters")
    
    # Local filter for this section
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        time_granularity = st.selectbox(
            "📅 Time Granularity",
            ["Daily", "Weekly", "Monthly"],
            key="sales_time_granularity"
        )
    
    with col2:
        if 'category' in sales_df.columns:
            categories = ['All Categories'] + sorted(sales_df['category'].dropna().unique().tolist())
            selected_category = st.selectbox(
                "🏷️ Category Filter",
                categories,
                key="sales_category_filter"
            )
        else:
            selected_category = 'All Categories'
    
    with col3:
        chart_type = st.selectbox(
            "📊 Chart Type",
            ["Area Chart", "Line Chart", "Bar Chart"],
            key="sales_chart_type"
        )
    
    # Filter data
    filtered_df = sales_df.copy()
    if selected_category != 'All Categories' and 'category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    
    # Aggregate based on granularity
    if time_granularity == "Daily":
        agg_df = filtered_df.groupby('date').agg({'revenue': 'sum', 'quantity_sold': 'sum'}).reset_index()
        agg_df.columns = ['Date', 'Revenue', 'Units']
    elif time_granularity == "Weekly":
        agg_df = filtered_df.groupby('week').agg({'revenue': 'sum', 'quantity_sold': 'sum'}).reset_index()
        agg_df.columns = ['Week', 'Revenue', 'Units']
    else:
        agg_df = filtered_df.groupby('month').agg({'revenue': 'sum', 'quantity_sold': 'sum'}).reset_index()
        agg_df.columns = ['Month', 'Revenue', 'Units']
    
    # Create charts
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_container("Revenue Trend", "💰")
        x_col = agg_df.columns[0]
        
        if chart_type == "Area Chart":
            fig = px.area(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'])
            fig.update_traces(fill='tozeroy', fillcolor='rgba(99, 102, 241, 0.3)')
        elif chart_type == "Line Chart":
            fig = px.line(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'], markers=True)
        else:
            fig = px.bar(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'])
        
        fig = apply_chart_style(fig, height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_container("Units Sold Trend", "📦")
        
        if chart_type == "Area Chart":
            fig2 = px.area(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'])
            fig2.update_traces(fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.3)')
        elif chart_type == "Line Chart":
            fig2 = px.line(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'], markers=True)
        else:
            fig2 = px.bar(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'])
        
        fig2 = apply_chart_style(fig2, height=350)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Category breakdown
    if 'category' in sales_df.columns:
        st.markdown("")
        render_chart_container("Revenue by Category", "🏷️")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            top_n = st.slider("Number of categories", 3, 10, 5, key="sales_top_n_categories")
        
        cat_df = filtered_df.groupby('category').agg({'revenue': 'sum'}).reset_index()
        cat_df = cat_df.nlargest(top_n, 'revenue')
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig3 = px.pie(cat_df, values='revenue', names='category', 
                         color_discrete_sequence=get_chart_colors(),
                         hole=0.5)
            fig3 = apply_chart_style(fig3, height=350)
            fig3.update_traces(textposition='outside', textinfo='percent+label')
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            fig4 = px.bar(cat_df.sort_values('revenue', ascending=True), 
                         x='revenue', y='category', orientation='h',
                         color='revenue', color_continuous_scale=['#6366f1', '#ec4899'])
            fig4 = apply_chart_style(fig4, height=350)
            fig4.update_layout(showlegend=False, coloraxis_showscale=False)
            st.plotly_chart(fig4, use_container_width=True)


def render_inventory_analysis(inventory_df, sales_df):
    """Render inventory analysis section with local filters."""
    render_section_header("📦", "Inventory Health Monitor", "Real-time stock levels and risk assessment")
    
    # Local filters
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        status_filter = st.multiselect(
            "🚦 Stock Status",
            options=['Critical', 'Low', 'Healthy'],
            default=['Critical', 'Low', 'Healthy'],
            key="inv_status_filter"
        )
    
    with col2:
        if 'category' in inventory_df.columns:
            inv_categories = ['All'] + sorted(inventory_df['category'].dropna().unique().tolist())
            inv_category = st.selectbox(
                "🏷️ Category",
                inv_categories,
                key="inv_category_filter"
            )
        else:
            inv_category = 'All'
    
    with col3:
        if 'store_id' in inventory_df.columns:
            stores = ['All Stores'] + sorted(inventory_df['store_id'].dropna().unique().tolist())
            selected_store = st.selectbox(
                "🏪 Store",
                stores,
                key="inv_store_filter"
            )
        else:
            selected_store = 'All Stores'
    
    # Filter data
    filtered_inv = inventory_df.copy()
    if status_filter:
        filtered_inv = filtered_inv[filtered_inv['stock_status'].isin(status_filter)]
    if inv_category != 'All' and 'category' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['category'] == inv_category]
    if selected_store != 'All Stores' and 'store_id' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['store_id'] == selected_store]
    
    # KPIs for this section
    total_items = len(filtered_inv)
    critical = len(filtered_inv[filtered_inv['stock_status'] == 'Critical'])
    low = len(filtered_inv[filtered_inv['stock_status'] == 'Low'])
    healthy = len(filtered_inv[filtered_inv['stock_status'] == 'Healthy'])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_status_card("Total Items", f"{total_items:,}")
    with col2:
        render_status_card("Critical", f"{critical:,}", "danger")
    with col3:
        render_status_card("Low Stock", f"{low:,}", "warning")
    with col4:
        render_status_card("Healthy", f"{healthy:,}", "success")
    
    st.markdown("")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_container("Stock Status Distribution", "🚦")
        status_counts = filtered_inv['stock_status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        
        colors_map = {'Critical': '#ef4444', 'Low': '#f59e0b', 'Healthy': '#10b981'}
        fig = px.pie(status_counts, values='Count', names='Status',
                    color='Status', color_discrete_map=colors_map,
                    hole=0.6)
        fig = apply_chart_style(fig, height=350)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_container("Stock Levels by Store", "🏪")
        
        store_stock = filtered_inv.groupby('store_id').agg({
            'stock_level': 'sum',
            'sku_id': 'count'
        }).reset_index()
        store_stock.columns = ['Store', 'Total Stock', 'SKU Count']
        store_stock = store_stock.nlargest(10, 'Total Stock')
        
        fig2 = px.bar(store_stock, x='Store', y='Total Stock',
                     color='Total Stock', color_continuous_scale=['#f59e0b', '#10b981'])
        fig2 = apply_chart_style(fig2, height=350)
        fig2.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Critical items table
    st.markdown("")
    render_chart_container("🚨 Top Stockout Risk Items", "⚠️")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        n_items = st.slider("Show items", 5, 20, 10, key="stockout_items_slider")
    
    critical_items = filtered_inv[filtered_inv['stock_status'].isin(['Critical', 'Low'])].copy()
    if len(critical_items) > 0:
        critical_items = critical_items.nsmallest(n_items, 'stock_level')
        display_cols = ['sku_id', 'store_id', 'stock_level', 'reorder_point', 'stock_status']
        if 'days_of_stock' in critical_items.columns:
            display_cols.append('days_of_stock')
        st.dataframe(critical_items[display_cols], use_container_width=True, hide_index=True)
    else:
        render_insight_box("✅", "All Clear!", "No critical stock items found with current filters.", "success")


def render_promotions_analysis(promotions_df, sales_df):
    """Render promotions analysis section with local filters."""
    render_section_header("🎯", "Promotional Performance Hub", "Analyze and optimize promotional campaigns")
    
    # Local filters
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        if 'promotion_type' in promotions_df.columns:
            promo_types = ['All Types'] + sorted(promotions_df['promotion_type'].dropna().unique().tolist())
            selected_promo_type = st.selectbox(
                "🏷️ Promotion Type",
                promo_types,
                key="promo_type_filter"
            )
        else:
            selected_promo_type = 'All Types'
    
    with col2:
        if 'discount_percentage' in promotions_df.columns:
            min_disc, max_disc = int(promotions_df['discount_percentage'].min()), int(promotions_df['discount_percentage'].max())
            discount_range = st.slider(
                "💸 Discount Range (%)",
                min_disc, max_disc, (min_disc, max_disc),
                key="promo_discount_range"
            )
        else:
            discount_range = (0, 100)
    
    with col3:
        view_mode = st.selectbox(
            "📊 View Mode",
            ["Overview", "Detailed Analysis", "Comparison"],
            key="promo_view_mode"
        )
    
    # Filter data
    filtered_promo = promotions_df.copy()
    if selected_promo_type != 'All Types' and 'promotion_type' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['promotion_type'] == selected_promo_type]
    if 'discount_percentage' in filtered_promo.columns:
        filtered_promo = filtered_promo[
            (filtered_promo['discount_percentage'] >= discount_range[0]) &
            (filtered_promo['discount_percentage'] <= discount_range[1])
        ]
    
    # KPIs
    total_promos = len(filtered_promo)
    avg_discount = filtered_promo['discount_percentage'].mean() if 'discount_percentage' in filtered_promo.columns else 0
    unique_skus = filtered_promo['sku_id'].nunique() if 'sku_id' in filtered_promo.columns else 0
    
    col1, col2, col3 = st.columns(3)
    with col1:
        render_status_card("Total Promotions", f"{total_promos:,}")
    with col2:
        render_status_card("Avg Discount", f"{avg_discount:.1f}%")
    with col3:
        render_status_card("SKUs on Promo", f"{unique_skus:,}")
    
    st.markdown("")
    
    # Charts based on view mode
    if view_mode == "Overview":
        col1, col2 = st.columns(2)
        
        with col1:
            render_chart_container("Promotions by Type", "📊")
            if 'promotion_type' in filtered_promo.columns:
                type_counts = filtered_promo['promotion_type'].value_counts().reset_index()
                type_counts.columns = ['Type', 'Count']
                
                fig = px.bar(type_counts, x='Type', y='Count',
                            color='Count', color_continuous_scale=['#6366f1', '#ec4899'])
                fig = apply_chart_style(fig, height=350)
                fig.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_chart_container("Discount Distribution", "💸")
            if 'discount_percentage' in filtered_promo.columns:
                fig2 = px.histogram(filtered_promo, x='discount_percentage', nbins=15,
                                   color_discrete_sequence=['#10b981'])
                fig2 = apply_chart_style(fig2, height=350)
                fig2.update_layout(xaxis_title="Discount %", yaxis_title="Count")
                st.plotly_chart(fig2, use_container_width=True)
    
    elif view_mode == "Detailed Analysis":
        render_chart_container("Promotion Timeline", "📅")
        if 'start_date' in filtered_promo.columns:
            promo_timeline = filtered_promo.groupby(filtered_promo['start_date'].dt.to_period('M').astype(str)).size().reset_index()
            promo_timeline.columns = ['Month', 'Promotions']
            
            fig = px.line(promo_timeline, x='Month', y='Promotions', markers=True,
                         color_discrete_sequence=['#6366f1'])
            fig = apply_chart_style(fig, height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        # Promotion effectiveness (simulated)
        render_chart_container("Promotion Effectiveness Score", "🎯")
        if 'promotion_type' in filtered_promo.columns:
            effectiveness = filtered_promo.groupby('promotion_type').agg({
                'discount_percentage': 'mean',
                'sku_id': 'count'
            }).reset_index()
            effectiveness.columns = ['Type', 'Avg Discount', 'Count']
            effectiveness['Effectiveness'] = (100 - effectiveness['Avg Discount']) * np.log1p(effectiveness['Count'])
            
            fig = px.scatter(effectiveness, x='Avg Discount', y='Effectiveness', size='Count',
                           color='Type', color_discrete_sequence=get_chart_colors(),
                           hover_name='Type')
            fig = apply_chart_style(fig, height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    else:  # Comparison
        render_chart_container("Type Comparison", "⚖️")
        if 'promotion_type' in filtered_promo.columns and 'discount_percentage' in filtered_promo.columns:
            fig = px.box(filtered_promo, x='promotion_type', y='discount_percentage',
                        color='promotion_type', color_discrete_sequence=get_chart_colors())
            fig = apply_chart_style(fig, height=400)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)


def render_promo_simulator(sales_df, inventory_df, promotions_df):
    """Render the What-If Promotion Simulator."""
    render_section_header("🧪", "What-If Promotion Simulator", "Simulate promotional scenarios and predict outcomes")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### ⚙️ Simulation Parameters")
        
        # Product selection
        if 'category' in sales_df.columns:
            sim_category = st.selectbox(
                "📦 Product Category",
                sorted(sales_df['category'].unique()),
                key="sim_category"
            )
        else:
            sim_category = "General"
        
        # Discount slider
        sim_discount = st.slider(
            "💸 Discount Percentage",
            min_value=5,
            max_value=70,
            value=20,
            step=5,
            key="sim_discount"
        )
        
        # Duration
        sim_duration = st.slider(
            "📅 Campaign Duration (days)",
            min_value=1,
            max_value=30,
            value=7,
            key="sim_duration"
        )
        
        # Promotion type
        sim_promo_type = st.selectbox(
            "🎯 Promotion Type",
            ["Percentage Off", "BOGO", "Bundle Deal", "Flash Sale"],
            key="sim_promo_type"
        )
        
        # Target audience
        sim_audience = st.multiselect(
            "👥 Target Audience",
            ["All Customers", "Premium Members", "New Customers", "Lapsed Customers"],
            default=["All Customers"],
            key="sim_audience"
        )
        
        run_simulation = st.button("🚀 Run Simulation", type="primary", use_container_width=True)
    
    with col2:
        if run_simulation or st.session_state.get('simulation_run', False):
            st.session_state['simulation_run'] = True
            
            # Calculate base metrics
            if 'category' in sales_df.columns:
                base_sales = sales_df[sales_df['category'] == sim_category]['revenue'].sum()
                base_units = sales_df[sales_df['category'] == sim_category]['quantity_sold'].sum()
            else:
                base_sales = sales_df['revenue'].sum()
                base_units = sales_df['quantity_sold'].sum()
            
            # Simulation logic (simplified model)
            elasticity = -1.5 - (0.02 * sim_discount)  # Price elasticity
            lift_factor = 1 + (abs(elasticity) * sim_discount / 100)
            
            # Adjust for promo type
            type_multiplier = {
                "Percentage Off": 1.0,
                "BOGO": 1.3,
                "Bundle Deal": 1.15,
                "Flash Sale": 1.4
            }
            lift_factor *= type_multiplier.get(sim_promo_type, 1.0)
            
            # Duration effect
            duration_effect = min(1 + (sim_duration / 14) * 0.3, 1.5)
            
            # Calculate projections
            projected_units = int(base_units * lift_factor * duration_effect * (sim_duration / 365))
            projected_revenue = projected_units * (base_sales / base_units) * (1 - sim_discount / 100) if base_units > 0 else 0
            base_period_revenue = base_sales * (sim_duration / 365)
            revenue_impact = projected_revenue - base_period_revenue
            
            # Display results
            st.markdown("#### 📊 Simulation Results")
            
            result_kpis = [
                {"icon": "📈", "value": f"{lift_factor:.1%}", "label": "Sales Lift", "type": "success" if lift_factor > 1 else "danger"},
                {"icon": "📦", "value": f"{projected_units:,}", "label": "Projected Units", "type": "primary"},
                {"icon": "💰", "value": f"${projected_revenue:,.0f}", "label": "Projected Revenue", "type": "accent"},
                {"icon": "📊", "value": f"${revenue_impact:+,.0f}", "label": "Revenue Impact", "type": "success" if revenue_impact > 0 else "danger"},
            ]
            render_kpi_row(result_kpis)
            
            st.markdown("")
            
            # Projection chart
            render_chart_container("Projected vs Baseline Performance", "📈")
            
            days = list(range(1, sim_duration + 1))
            baseline = [base_period_revenue / sim_duration * d for d in days]
            projected = [projected_revenue / sim_duration * d for d in days]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=days, y=baseline, name='Baseline',
                line=dict(color='#71717a', dash='dash'),
                fill='tozeroy', fillcolor='rgba(113, 113, 122, 0.1)'
            ))
            fig.add_trace(go.Scatter(
                x=days, y=projected, name='With Promotion',
                line=dict(color='#6366f1', width=3),
                fill='tozeroy', fillcolor='rgba(99, 102, 241, 0.2)'
            ))
            fig = apply_chart_style(fig, height=350)
            fig.update_layout(xaxis_title="Day", yaxis_title="Cumulative Revenue ($)")
            st.plotly_chart(fig, use_container_width=True)
            
            # AI Recommendations
            recommendations = [
                {"icon": "🎯", "text": f"A {sim_discount}% discount on {sim_category} could generate {lift_factor:.0%} sales lift"},
                {"icon": "⏰", "text": f"Optimal campaign duration: {max(7, sim_duration)} days for maximum impact"},
                {"icon": "💡", "text": f"Consider {sim_promo_type} for this category - historically performs {type_multiplier.get(sim_promo_type, 1)*100-100:.0f}% better"},
            ]
            
            if revenue_impact < 0:
                recommendations.append({"icon": "⚠️", "text": "Warning: Projected negative margin impact. Consider reducing discount or duration."})
            else:
                recommendations.append({"icon": "✅", "text": f"Positive ROI expected. Estimated incremental profit: ${revenue_impact * 0.3:,.0f}"})
            
            render_ai_recommendations(recommendations)
        
        else:
            # Show placeholder
            st.markdown("")
            render_insight_box(
                "💡",
                "Configure Your Simulation",
                "Adjust the parameters on the left and click 'Run Simulation' to see projected outcomes for your promotional campaign.",
                "primary"
            )


def render_store_performance(sales_df, inventory_df):
    """Render store performance analysis."""
    render_section_header("🏪", "Store Performance Analysis", "Compare performance across store locations")
    
    # Local filters
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        metric_type = st.selectbox(
            "📊 Performance Metric",
            ["Revenue", "Units Sold", "Transactions", "Avg Order Value"],
            key="store_metric"
        )
    
    with col2:
        if 'month' in sales_df.columns:
            months = ['All Time'] + sorted(sales_df['month'].unique().tolist())
            selected_month = st.selectbox(
                "📅 Time Period",
                months,
                key="store_time_period"
            )
        else:
            selected_month = 'All Time'
    
    with col3:
        top_n_stores = st.slider(
            "🏪 Number of Stores",
            5, 20, 10,
            key="store_top_n"
        )
    
    # Filter data
    filtered_sales = sales_df.copy()
    if selected_month != 'All Time' and 'month' in filtered_sales.columns:
        filtered_sales = filtered_sales[filtered_sales['month'] == selected_month]
    
    # Calculate store metrics
    store_metrics = filtered_sales.groupby('store_id').agg({
        'revenue': 'sum',
        'quantity_sold': 'sum',
        'transaction_id': 'nunique'
    }).reset_index()
    store_metrics.columns = ['Store', 'Revenue', 'Units', 'Transactions']
    store_metrics['AOV'] = store_metrics['Revenue'] / store_metrics['Transactions']
    
    # Select metric
    metric_map = {
        "Revenue": "Revenue",
        "Units Sold": "Units",
        "Transactions": "Transactions",
        "Avg Order Value": "AOV"
    }
    selected_metric = metric_map[metric_type]
    
    store_metrics = store_metrics.nlargest(top_n_stores, selected_metric)
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_container(f"Top Stores by {metric_type}", "🏆")
        fig = px.bar(
            store_metrics.sort_values(selected_metric, ascending=True),
            x=selected_metric,
            y='Store',
            orientation='h',
            color=selected_metric,
            color_continuous_scale=['#6366f1', '#ec4899']
        )
        fig = apply_chart_style(fig, height=400)
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_container("Store Performance Distribution", "📊")
        fig2 = px.scatter(
            store_metrics,
            x='Revenue',
            y='Units',
            size='Transactions',
            color='AOV',
            hover_name='Store',
            color_continuous_scale=['#f59e0b', '#10b981']
        )
        fig2 = apply_chart_style(fig2, height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Store comparison table
    render_chart_container("Store Metrics Comparison", "📋")
    
    display_df = store_metrics.copy()
    display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"${x:,.0f}")
    display_df['Units'] = display_df['Units'].apply(lambda x: f"{x:,}")
    display_df['Transactions'] = display_df['Transactions'].apply(lambda x: f"{x:,}")
    display_df['AOV'] = display_df['AOV'].apply(lambda x: f"${x:.2f}")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)


def render_time_analysis(sales_df):
    """Render time-based analysis."""
    render_section_header("⏰", "Time-Based Analytics", "Discover temporal patterns and trends")
    
    # Local filters
    col1, col2 = st.columns([2, 2])
    
    with col1:
        analysis_type = st.selectbox(
            "📊 Analysis Type",
            ["Day of Week", "Hourly Pattern", "Monthly Trend", "Weekly Comparison"],
            key="time_analysis_type"
        )
    
    with col2:
        if 'category' in sales_df.columns:
            time_category = st.selectbox(
                "🏷️ Category",
                ['All Categories'] + sorted(sales_df['category'].unique().tolist()),
                key="time_category"
            )
        else:
            time_category = 'All Categories'
    
    # Filter data
    filtered_df = sales_df.copy()
    if time_category != 'All Categories' and 'category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['category'] == time_category]
    
    if analysis_type == "Day of Week":
        render_chart_container("Sales by Day of Week", "📅")
        
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_sales = filtered_df.groupby('day_of_week').agg({'revenue': 'sum', 'quantity_sold': 'sum'}).reset_index()
        dow_sales['day_of_week'] = pd.Categorical(dow_sales['day_of_week'], categories=day_order, ordered=True)
        dow_sales = dow_sales.sort_values('day_of_week')
        
        fig = px.bar(dow_sales, x='day_of_week', y='revenue',
                    color='revenue', color_continuous_scale=['#6366f1', '#ec4899'])
        fig = apply_chart_style(fig, height=400)
        fig.update_layout(xaxis_title="Day", yaxis_title="Revenue ($)", coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Insights
        best_day = dow_sales.loc[dow_sales['revenue'].idxmax(), 'day_of_week']
        worst_day = dow_sales.loc[dow_sales['revenue'].idxmin(), 'day_of_week']
        render_insight_box("📈", "Peak Day", f"{best_day} generates the highest revenue. Consider scheduling major promotions on this day.", "success")
        render_insight_box("📉", "Opportunity Day", f"{worst_day} has the lowest sales. Consider targeted promotions to boost performance.", "warning")
    
    elif analysis_type == "Monthly Trend":
        render_chart_container("Monthly Revenue Trend", "📈")
        
        monthly_sales = filtered_df.groupby('month').agg({'revenue': 'sum', 'quantity_sold': 'sum'}).reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=monthly_sales['month'],
            y=monthly_sales['revenue'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color='#6366f1', width=3),
            fill='tozeroy',
            fillcolor='rgba(99, 102, 241, 0.2)'
        ))
        fig = apply_chart_style(fig, height=400)
        fig.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)")
        st.plotly_chart(fig, use_container_width=True)
    
    elif analysis_type == "Weekly Comparison":
        render_chart_container("Weekly Performance Comparison", "📊")
        
        weekly_sales = filtered_df.groupby('week').agg({'revenue': 'sum'}).reset_index()
        
        fig = px.area(weekly_sales, x='week', y='revenue',
                     color_discrete_sequence=['#10b981'])
        fig.update_traces(fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.3)')
        fig = apply_chart_style(fig, height=400)
        fig.update_layout(xaxis_title="Week Number", yaxis_title="Revenue ($)")
        st.plotly_chart(fig, use_container_width=True)
    
    else:  # Hourly Pattern - simulated
        render_chart_container("Simulated Hourly Sales Pattern", "🕐")
        
        hours = list(range(24))
        # Simulate typical retail pattern
        hourly_pattern = [10, 5, 3, 2, 2, 5, 15, 30, 50, 70, 85, 95, 100, 90, 85, 80, 85, 90, 95, 80, 60, 40, 25, 15]
        
        hourly_df = pd.DataFrame({'Hour': hours, 'Sales Index': hourly_pattern})
        
        fig = px.line(hourly_df, x='Hour', y='Sales Index', markers=True,
                     color_discrete_sequence=['#f59e0b'])
        fig.add_vrect(x0=11, x1=14, fillcolor="rgba(16, 185, 129, 0.1)", 
                     layer="below", line_width=0, annotation_text="Peak Hours")
        fig = apply_chart_style(fig, height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        render_insight_box("🕐", "Peak Hours", "11 AM - 2 PM shows highest traffic. Ensure adequate staffing during these hours.", "primary")


# =============================================================================
# SIDEBAR
# =============================================================================

def render_sidebar():
    """Render sidebar with data upload and navigation."""
    with st.sidebar:
        st.markdown("### 🚀 UAE Promo Pulse")
        st.markdown("---")
        
        # Data source selection
        st.markdown("#### 📂 Data Source")
        data_source = st.radio(
            "Select data source:",
            ["📊 Sample Data", "📁 Upload Files"],
            label_visibility="collapsed"
        )
        
        if data_source == "📁 Upload Files":
            st.markdown("---")
            st.markdown("#### 📤 Upload Your Data")
            
            sales_file = st.file_uploader("Sales Data (CSV)", type=['csv'], key='sales_upload')
            inventory_file = st.file_uploader("Inventory Data (CSV)", type=['csv'], key='inventory_upload')
            promotions_file = st.file_uploader("Promotions Data (CSV)", type=['csv'], key='promotions_upload')
            
            if sales_file and inventory_file and promotions_file:
                sales_df, inventory_df, promotions_df, error = load_and_process_data(
                    sales_file, inventory_file, promotions_file
                )
                if error:
                    st.error(f"Error: {error}")
                    return None, None, None
                st.success("✅ Data loaded successfully!")
                return sales_df, inventory_df, promotions_df
            else:
                st.info("📌 Please upload all three files")
                return None, None, None
        else:
            # Use sample data
            return generate_sample_data()


# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point."""
    # Load CSS
    load_premium_css()
    
    # Render sidebar and get data
    data = render_sidebar()
    
    if data[0] is None:
        render_hero_header()
        render_insight_box(
            "📊",
            "Welcome to UAE Promo Pulse Simulator",
            "Select 'Sample Data' in the sidebar to explore the dashboard with demo data, or upload your own CSV files.",
            "primary"
        )
        return
    
    sales_df, inventory_df, promotions_df = data
    
    # Render hero header
    render_hero_header()
    
    # Overview KPIs
    render_overview_kpis(sales_df, inventory_df, promotions_df)
    
    render_divider()
    
    # Main tabs
    tabs = st.tabs([
        "📈 Sales Analytics",
        "📦 Inventory Health",
        "🎯 Promotions",
        "🧪 Simulator",
        "🏪 Store Performance",
        "⏰ Time Analysis"
    ])
    
    with tabs[0]:
        render_sales_analysis(sales_df)
    
    with tabs[1]:
        render_inventory_analysis(inventory_df, sales_df)
    
    with tabs[2]:
        render_promotions_analysis(promotions_df, sales_df)
    
    with tabs[3]:
        render_promo_simulator(sales_df, inventory_df, promotions_df)
    
    with tabs[4]:
        render_store_performance(sales_df, inventory_df)
    
    with tabs[5]:
        render_time_analysis(sales_df)
    
    # Footer
    render_footer()


if __name__ == "__main__":
    main()
