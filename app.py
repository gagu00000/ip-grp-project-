# =============================================================================
# UAE PROMO PULSE SIMULATOR - PREMIUM EDITION v2.0
# Complete Production-Ready Dashboard
# Total Lines: ~3900+
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
# PREMIUM CSS - GLASSMORPHISM DESIGN SYSTEM (COMPLETE)
# =============================================================================

def load_premium_css():
    """Load complete premium glassmorphism CSS with all animations."""
    st.markdown("""
<style>
/* =============================================================================
   UAE PROMO PULSE - PREMIUM DESIGN SYSTEM v2.0
   Glassmorphism + Animations + Modern UI
   Complete Stylesheet
============================================================================= */

/* Import Premium Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* =============================================================================
   CSS VARIABLES - DESIGN TOKENS
============================================================================= */

:root {
    /* Primary Colors */
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --primary-glow: rgba(99, 102, 241, 0.4);
    
    /* Secondary Colors */
    --secondary: #ec4899;
    --secondary-light: #f472b6;
    --secondary-dark: #db2777;
    
    /* Accent Colors */
    --accent: #06b6d4;
    --accent-light: #22d3ee;
    --accent-dark: #0891b2;
    
    /* Semantic Colors */
    --success: #10b981;
    --success-light: #34d399;
    --success-dark: #059669;
    --success-glow: rgba(16, 185, 129, 0.4);
    
    --warning: #f59e0b;
    --warning-light: #fbbf24;
    --warning-dark: #d97706;
    --warning-glow: rgba(245, 158, 11, 0.4);
    
    --danger: #ef4444;
    --danger-light: #f87171;
    --danger-dark: #dc2626;
    --danger-glow: rgba(239, 68, 68, 0.4);
    
    --info: #3b82f6;
    --info-light: #60a5fa;
    --info-dark: #2563eb;
    
    /* Neutral Colors */
    --neutral-50: #fafafa;
    --neutral-100: #f4f4f5;
    --neutral-200: #e4e4e7;
    --neutral-300: #d4d4d8;
    --neutral-400: #a1a1aa;
    --neutral-500: #71717a;
    --neutral-600: #52525b;
    --neutral-700: #3f3f46;
    --neutral-800: #27272a;
    --neutral-900: #18181b;
    
    /* Background Colors */
    --bg-dark: #0a0a0f;
    --bg-darker: #050507;
    --bg-card: rgba(255, 255, 255, 0.03);
    --bg-card-hover: rgba(255, 255, 255, 0.06);
    --bg-card-active: rgba(255, 255, 255, 0.08);
    
    /* Glass Effect */
    --glass: rgba(255, 255, 255, 0.05);
    --glass-light: rgba(255, 255, 255, 0.08);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-border-light: rgba(255, 255, 255, 0.15);
    
    /* Text Colors */
    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;
    --text-disabled: #52525b;
    
    /* Shadows & Glows */
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.3);
    --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.3);
    --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.4);
    --shadow-2xl: 0 25px 50px rgba(0, 0, 0, 0.5);
    
    --glow-primary: 0 0 40px rgba(99, 102, 241, 0.3);
    --glow-secondary: 0 0 40px rgba(236, 72, 153, 0.3);
    --glow-success: 0 0 40px rgba(16, 185, 129, 0.3);
    --glow-warning: 0 0 40px rgba(245, 158, 11, 0.3);
    --glow-danger: 0 0 40px rgba(239, 68, 68, 0.3);
    --glow-accent: 0 0 40px rgba(6, 182, 212, 0.3);
    
    /* Spacing */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;
    --space-2xl: 48px;
    --space-3xl: 64px;
    
    /* Border Radius */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --radius-xl: 20px;
    --radius-2xl: 28px;
    --radius-full: 9999px;
    
    /* Transitions */
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-bounce: 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
    
    /* Z-Index Scale */
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-fixed: 300;
    --z-modal-backdrop: 400;
    --z-modal: 500;
    --z-popover: 600;
    --z-tooltip: 700;
}

/* =============================================================================
   GLOBAL STYLES & RESETS
============================================================================= */

*, *::before, *::after {
    box-sizing: border-box;
}

.stApp {
    background: linear-gradient(135deg, var(--bg-dark) 0%, #1a1a2e 50%, var(--bg-dark) 100%);
    background-attachment: fixed;
    min-height: 100vh;
}

/* Animated Background Mesh */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(ellipse at 10% 10%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
        radial-gradient(ellipse at 90% 20%, rgba(236, 72, 153, 0.08) 0%, transparent 40%),
        radial-gradient(ellipse at 50% 50%, rgba(6, 182, 212, 0.05) 0%, transparent 50%),
        radial-gradient(ellipse at 20% 80%, rgba(16, 185, 129, 0.06) 0%, transparent 40%),
        radial-gradient(ellipse at 80% 90%, rgba(245, 158, 11, 0.05) 0%, transparent 40%);
    pointer-events: none;
    z-index: 0;
    animation: meshFloat 30s ease-in-out infinite;
}

@keyframes meshFloat {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}

/* Hide Streamlit Defaults */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none !important;}

/* Main Container */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1600px !important;
}

/* =============================================================================
   HERO HEADER SECTION
============================================================================= */

.hero-header {
    text-align: center;
    padding: 60px 40px 50px 40px;
    margin: -3rem -2rem 2rem -2rem;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(236, 72, 153, 0.06) 50%, rgba(6, 182, 212, 0.04) 100%);
    border-bottom: 1px solid var(--glass-border);
    position: relative;
    overflow: hidden;
    border-radius: 0 0 var(--radius-2xl) var(--radius-2xl);
}

.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg at 50% 50%, transparent 0deg, rgba(99, 102, 241, 0.08) 60deg, transparent 120deg, rgba(236, 72, 153, 0.05) 180deg, transparent 240deg, rgba(6, 182, 212, 0.05) 300deg, transparent 360deg);
    animation: heroRotate 25s linear infinite;
}

@keyframes heroRotate {
    100% { transform: rotate(360deg); }
}

.hero-header::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), var(--secondary), var(--primary), transparent);
    opacity: 0.5;
}

.hero-title {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 40%, var(--secondary) 70%, var(--accent) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 14px;
    position: relative;
    z-index: 1;
    letter-spacing: -0.03em;
    line-height: 1.1;
    text-shadow: 0 0 80px rgba(99, 102, 241, 0.5);
}

.hero-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 1.15rem;
    color: var(--text-secondary);
    font-weight: 400;
    position: relative;
    z-index: 1;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

.hero-badge-container {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 24px;
    position: relative;
    z-index: 1;
    flex-wrap: wrap;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 18px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--primary-light);
    transition: var(--transition-base);
}

.hero-badge:hover {
    background: rgba(99, 102, 241, 0.25);
    border-color: rgba(99, 102, 241, 0.5);
    transform: translateY(-2px);
}

.hero-badge.success {
    background: rgba(16, 185, 129, 0.15);
    border-color: rgba(16, 185, 129, 0.3);
    color: var(--success-light);
}

.hero-badge.warning {
    background: rgba(245, 158, 11, 0.15);
    border-color: rgba(245, 158, 11, 0.3);
    color: var(--warning-light);
}

.hero-badge-dot {
    width: 8px;
    height: 8px;
    background: var(--success);
    border-radius: 50%;
    animation: pulseDot 2s ease-in-out infinite;
}

@keyframes pulseDot {
    0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
    50% { opacity: 0.8; transform: scale(1.1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
}

/* =============================================================================
   KPI CARDS - PREMIUM DESIGN
============================================================================= */

.kpi-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 24px 0;
}

.kpi-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-xl);
    padding: 22px 20px;
    position: relative;
    overflow: hidden;
    transition: all var(--transition-base);
    cursor: default;
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    border-radius: var(--radius-sm) 0 0 var(--radius-sm);
    transition: var(--transition-base);
}

.kpi-card::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
    transition: left 0.6s ease;
}

.kpi-card:hover::after {
    left: 100%;
}

.kpi-card:hover {
    transform: translateY(-6px) scale(1.02);
    border-color: var(--glass-border-light);
}

/* KPI Card Variants */
.kpi-card.primary::before { background: linear-gradient(180deg, var(--primary), var(--primary-dark)); }
.kpi-card.primary:hover { box-shadow: var(--glow-primary), var(--shadow-xl); }

.kpi-card.secondary::before { background: linear-gradient(180deg, var(--secondary), var(--secondary-dark)); }
.kpi-card.secondary:hover { box-shadow: var(--glow-secondary), var(--shadow-xl); }

.kpi-card.success::before { background: linear-gradient(180deg, var(--success), var(--success-dark)); }
.kpi-card.success:hover { box-shadow: var(--glow-success), var(--shadow-xl); }

.kpi-card.warning::before { background: linear-gradient(180deg, var(--warning), var(--warning-dark)); }
.kpi-card.warning:hover { box-shadow: var(--glow-warning), var(--shadow-xl); }

.kpi-card.danger::before { background: linear-gradient(180deg, var(--danger), var(--danger-dark)); }
.kpi-card.danger:hover { box-shadow: var(--glow-danger), var(--shadow-xl); }

.kpi-card.accent::before { background: linear-gradient(180deg, var(--accent), var(--accent-dark)); }
.kpi-card.accent:hover { box-shadow: var(--glow-accent), var(--shadow-xl); }

.kpi-card.info::before { background: linear-gradient(180deg, var(--info), var(--info-dark)); }

.kpi-icon {
    font-size: 1.8rem;
    margin-bottom: 10px;
    display: block;
}

.kpi-value {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.1;
    letter-spacing: -0.02em;
}

.kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    color: var(--text-secondary);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-top: 6px;
}

.kpi-delta {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border-radius: var(--radius-md);
    font-size: 0.72rem;
    font-weight: 700;
    margin-top: 10px;
    letter-spacing: 0.02em;
}

.kpi-delta.positive {
    background: rgba(16, 185, 129, 0.15);
    color: var(--success-light);
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.kpi-delta.negative {
    background: rgba(239, 68, 68, 0.15);
    color: var(--danger-light);
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.kpi-delta.neutral {
    background: rgba(161, 161, 170, 0.15);
    color: var(--text-secondary);
    border: 1px solid rgba(161, 161, 170, 0.2);
}

/* =============================================================================
   SECTION HEADERS
============================================================================= */

.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 40px 0 24px 0;
    padding-bottom: 18px;
    border-bottom: 1px solid var(--glass-border);
    position: relative;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 100px;
    height: 2px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: var(--radius-full);
}

.section-icon {
    width: 48px;
    height: 48px;
    border-radius: var(--radius-lg);
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.35);
    flex-shrink: 0;
}

.section-content {
    flex: 1;
}

.section-title {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.01em;
    line-height: 1.2;
}

.section-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-top: 4px;
    font-weight: 400;
}

/* =============================================================================
   FILTER BOX
============================================================================= */

.filter-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(99, 102, 241, 0.03) 100%);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: var(--radius-xl);
    padding: 20px 24px;
    margin-bottom: 24px;
    position: relative;
}

.filter-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.filter-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--primary-light);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.filter-row {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    align-items: flex-end;
}

/* =============================================================================
   CHART CONTAINER
============================================================================= */

.chart-container {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.04) 0%, rgba(255, 255, 255, 0.01) 100%);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-xl);
    padding: 24px;
    margin: 16px 0;
    transition: all var(--transition-base);
    position: relative;
    overflow: hidden;
}

.chart-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
}

.chart-container:hover {
    border-color: rgba(99, 102, 241, 0.3);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2), var(--glow-primary);
}

.chart-title {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 16px;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.chart-title-icon {
    font-size: 1.2rem;
}

/* =============================================================================
   INSIGHT BOXES
============================================================================= */

.insight-box {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-radius: var(--radius-lg);
    padding: 20px 24px;
    margin: 14px 0;
    border-left: 4px solid;
    position: relative;
    overflow: hidden;
    transition: all var(--transition-base);
}

.insight-box:hover {
    transform: translateX(4px);
}

.insight-box::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 150px;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.02));
    pointer-events: none;
}

.insight-box.primary { border-left-color: var(--primary); }
.insight-box.success { border-left-color: var(--success); }
.insight-box.warning { border-left-color: var(--warning); }
.insight-box.danger { border-left-color: var(--danger); }
.insight-box.info { border-left-color: var(--info); }
.insight-box.accent { border-left-color: var(--accent); }

.insight-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
}

.insight-icon {
    font-size: 1.4rem;
}

.insight-title {
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--text-primary);
}

.insight-text {
    color: var(--text-secondary);
    font-size: 0.92rem;
    line-height: 1.65;
    margin: 0;
}

/* =============================================================================
   AI RECOMMENDATION BOX
============================================================================= */

.ai-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(236, 72, 153, 0.06) 50%, rgba(6, 182, 212, 0.04) 100%);
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: var(--radius-xl);
    padding: 28px;
    margin: 24px 0;
    position: relative;
    overflow: hidden;
}

.ai-box::before {
    content: '';
    position: absolute;
    top: -100%;
    right: -100%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(99, 102, 241, 0.1) 0%, transparent 50%);
    animation: aiPulse 6s ease-in-out infinite;
}

@keyframes aiPulse {
    0%, 100% { opacity: 0.4; transform: scale(1) rotate(0deg); }
    50% { opacity: 0.8; transform: scale(1.1) rotate(180deg); }
}

.ai-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 22px;
    position: relative;
    z-index: 1;
}

.ai-avatar {
    width: 52px;
    height: 52px;
    border-radius: var(--radius-lg);
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
    animation: aiFloat 4s ease-in-out infinite;
}

@keyframes aiFloat {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    25% { transform: translateY(-4px) rotate(2deg); }
    75% { transform: translateY(4px) rotate(-2deg); }
}

.ai-info {
    flex: 1;
}

.ai-title {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-primary);
}

.ai-subtitle {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 2px;
}

.ai-items {
    position: relative;
    z-index: 1;
}

.ai-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 16px 18px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: var(--radius-lg);
    margin: 12px 0;
    transition: all var(--transition-base);
}

.ai-item:hover {
    background: rgba(255, 255, 255, 0.07);
    border-color: rgba(99, 102, 241, 0.3);
    transform: translateX(8px);
}

.ai-item-icon {
    font-size: 1.3rem;
    flex-shrink: 0;
    margin-top: 2px;
}

.ai-item-text {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
}

/* =============================================================================
   STATUS CARDS
============================================================================= */

.status-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    padding: 18px 20px;
    text-align: center;
    transition: all var(--transition-base);
}

.status-card:hover {
    border-color: var(--glass-border-light);
    transform: translateY(-3px);
}

.status-label {
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
    margin-bottom: 8px;
}

.status-value {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text-primary);
}

.status-value.success { color: var(--success); }
.status-value.warning { color: var(--warning); }
.status-value.danger { color: var(--danger); }
.status-value.primary { color: var(--primary-light); }

/* =============================================================================
   CONSTRAINT CARDS
============================================================================= */

.constraint-card {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 16px 20px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    margin: 10px 0;
    transition: all var(--transition-base);
}

.constraint-card:hover {
    border-color: var(--glass-border-light);
    background: var(--bg-card-hover);
}

.constraint-icon {
    font-size: 1.5rem;
}

.constraint-content {
    flex: 1;
}

.constraint-label {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 4px;
}

.constraint-status {
    font-weight: 700;
    font-size: 0.95rem;
}

.constraint-status.pass { color: var(--success); }
.constraint-status.fail { color: var(--danger); }
.constraint-status.warning { color: var(--warning); }

/* =============================================================================
   DATA TABLES
============================================================================= */

.stDataFrame {
    border-radius: var(--radius-lg) !important;
    overflow: hidden !important;
}

.dataframe {
    background: rgba(255, 255, 255, 0.02) !important;
    border-radius: var(--radius-lg) !important;
    overflow: hidden !important;
    border: 1px solid var(--glass-border) !important;
}

.dataframe th {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(99, 102, 241, 0.08) 100%) !important;
    color: var(--text-primary) !important;
    font-weight: 700 !important;
    padding: 14px 18px !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-size: 0.75rem;
    border-bottom: 1px solid rgba(99, 102, 241, 0.2) !important;
    white-space: nowrap;
}

.dataframe td {
    background: transparent !important;
    color: var(--text-secondary) !important;
    padding: 13px 18px !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04) !important;
    font-size: 0.88rem;
    transition: all var(--transition-fast);
}

.dataframe tr:hover td {
    background: rgba(99, 102, 241, 0.08) !important;
    color: var(--text-primary) !important;
}

.dataframe tr:last-child td {
    border-bottom: none !important;
}

/* =============================================================================
   FORM ELEMENTS
============================================================================= */

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius-lg) !important;
    padding: 12px 28px !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    transition: all var(--transition-base) !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    letter-spacing: 0.01em;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.45) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Secondary Buttons */
.stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 2px solid var(--glass-border-light) !important;
    color: var(--text-primary) !important;
    box-shadow: none !important;
}

.stButton > button[kind="secondary"]:hover {
    background: var(--bg-card-hover) !important;
    border-color: var(--primary) !important;
}

/* Sliders */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important;
}

.stSlider > div > div > div {
    background: rgba(255, 255, 255, 0.1) !important;
}

.stSlider [data-baseweb="slider"] > div:first-child {
    background: rgba(255, 255, 255, 0.08) !important;
}

/* Select boxes */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    transition: all var(--transition-fast) !important;
}

.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover {
    border-color: var(--primary) !important;
}

.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}

/* Text inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    padding: 12px 16px !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}

/* Text area */
.stTextArea > div > div > textarea {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
}

/* Checkbox & Radio */
.stCheckbox > label,
.stRadio > label {
    color: var(--text-secondary) !important;
}

/* =============================================================================
   TABS
============================================================================= */

.stTabs [data-baseweb="tab-list"] {
    background: rgba(255, 255, 255, 0.03);
    border-radius: var(--radius-xl);
    padding: 8px;
    gap: 6px;
    border: 1px solid var(--glass-border);
    flex-wrap: wrap;
}

.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-lg) !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    color: var(--text-secondary) !important;
    background: transparent !important;
    border: 1px solid transparent !important;
    transition: all var(--transition-base) !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-primary) !important;
    background: rgba(255, 255, 255, 0.05) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
    border-color: transparent !important;
}

.stTabs [data-baseweb="tab-panel"] {
    padding-top: 24px !important;
}

/* =============================================================================
   SIDEBAR
============================================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(10, 10, 15, 0.98) 0%, rgba(26, 26, 46, 0.95) 100%) !important;
    border-right: 1px solid var(--glass-border) !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--text-primary) !important;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {
    color: var(--text-secondary) !important;
}

/* Sidebar Navigation */
.sidebar-nav {
    margin: 20px 0;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 18px;
    margin: 6px 0;
    border-radius: var(--radius-lg);
    background: transparent;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all var(--transition-base);
    border: 1px solid transparent;
    font-weight: 500;
}

.nav-item:hover {
    background: rgba(99, 102, 241, 0.1);
    color: var(--text-primary);
    border-color: rgba(99, 102, 241, 0.2);
}

.nav-item.active {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(99, 102, 241, 0.1) 100%);
    color: var(--text-primary);
    border-color: rgba(99, 102, 241, 0.3);
}

.nav-icon { font-size: 1.2rem; }
.nav-text { font-size: 0.9rem; }

/* =============================================================================
   EXPANDER
============================================================================= */

.streamlit-expanderHeader {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius-lg) !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    padding: 16px 20px !important;
    transition: all var(--transition-base) !important;
}

.streamlit-expanderHeader:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    border-color: var(--glass-border-light) !important;
}

.streamlit-expanderContent {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid var(--glass-border) !important;
    border-top: none !important;
    border-radius: 0 0 var(--radius-lg) var(--radius-lg) !important;
    padding: 20px !important;
}

/* =============================================================================
   METRICS (Native Streamlit)
============================================================================= */

[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', 'Inter', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: var(--text-primary) !important;
}

[data-testid="stMetricLabel"] {
    color: var(--text-secondary) !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

[data-testid="stMetricDelta"] {
    font-weight: 700 !important;
}

[data-testid="stMetricDeltaIcon-Up"] {
    color: var(--success) !important;
}

[data-testid="stMetricDeltaIcon-Down"] {
    color: var(--danger) !important;
}

/* =============================================================================
   FILE UPLOADER
============================================================================= */

[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 2px dashed rgba(99, 102, 241, 0.3) !important;
    border-radius: var(--radius-xl) !important;
    padding: 24px !important;
    transition: all var(--transition-base) !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(99, 102, 241, 0.5) !important;
    background: rgba(99, 102, 241, 0.05) !important;
}

[data-testid="stFileUploader"] label {
    color: var(--text-secondary) !important;
}

/* =============================================================================
   ALERTS & MESSAGES
============================================================================= */

.stAlert {
    border-radius: var(--radius-lg) !important;
    border: 1px solid !important;
}

.stSuccess {
    background: rgba(16, 185, 129, 0.1) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
}

.stError {
    background: rgba(239, 68, 68, 0.1) !important;
    border-color: rgba(239, 68, 68, 0.3) !important;
}

.stWarning {
    background: rgba(245, 158, 11, 0.1) !important;
    border-color: rgba(245, 158, 11, 0.3) !important;
}

.stInfo {
    background: rgba(59, 130, 246, 0.1) !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
}

/* =============================================================================
   PROGRESS BAR
============================================================================= */

.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important;
    border-radius: var(--radius-full) !important;
}

.stProgress > div > div {
    background: rgba(255, 255, 255, 0.1) !important;
    border-radius: var(--radius-full) !important;
}

/* =============================================================================
   DIVIDERS
============================================================================= */

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--glass-border-light), transparent);
    margin: 32px 0;
}

.divider-subtle {
    height: 1px;
    background: var(--glass-border);
    margin: 24px 0;
}

.divider-gradient {
    height: 2px;
    background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    margin: 32px 0;
    border-radius: var(--radius-full);
}

/* =============================================================================
   FOOTER
============================================================================= */

.footer {
    text-align: center;
    padding: 40px 24px;
    margin-top: 60px;
    border-top: 1px solid var(--glass-border);
    color: var(--text-muted);
    font-size: 0.9rem;
}

.footer-brand {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-top: 16px;
}

.footer-link {
    color: var(--text-muted);
    text-decoration: none;
    transition: color var(--transition-fast);
}

.footer-link:hover {
    color: var(--primary-light);
}

/* =============================================================================
   SCROLLBAR
============================================================================= */

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.02);
    border-radius: var(--radius-full);
}

::-webkit-scrollbar-thumb {
    background: rgba(99, 102, 241, 0.3);
    border-radius: var(--radius-full);
    transition: background var(--transition-fast);
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(99, 102, 241, 0.5);
}

/* =============================================================================
   ANIMATIONS
============================================================================= */

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInRight {
    from { opacity: 0; transform: translateX(20px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

@keyframes slideInRight {
    from { transform: translateX(100%); }
    to { transform: translateX(0); }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.animate-fade-in { animation: fadeIn 0.5s ease-out forwards; }
.animate-fade-in-left { animation: fadeInLeft 0.5s ease-out forwards; }
.animate-fade-in-right { animation: fadeInRight 0.5s ease-out forwards; }
.animate-fade-in-up { animation: fadeInUp 0.5s ease-out forwards; }
.animate-scale-in { animation: scaleIn 0.4s ease-out forwards; }

/* Staggered animations */
.stagger-1 { animation-delay: 0.1s; }
.stagger-2 { animation-delay: 0.2s; }
.stagger-3 { animation-delay: 0.3s; }
.stagger-4 { animation-delay: 0.4s; }
.stagger-5 { animation-delay: 0.5s; }

/* Loading skeleton */
.skeleton {
    background: linear-gradient(90deg, var(--bg-card) 25%, var(--bg-card-hover) 50%, var(--bg-card) 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: var(--radius-md);
}

/* =============================================================================
   RESPONSIVE DESIGN
============================================================================= */

@media (max-width: 1200px) {
    .hero-title { font-size: 2.6rem; }
    .kpi-container { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 992px) {
    .hero-title { font-size: 2.2rem; }
    .kpi-container { grid-template-columns: repeat(2, 1fr); }
    .section-title { font-size: 1.3rem; }
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    .hero-header {
        padding: 40px 20px 35px 20px;
        margin: -2rem -1rem 1.5rem -1rem;
    }
    
    .hero-title { font-size: 1.8rem; }
    .hero-subtitle { font-size: 1rem; }
    
    .kpi-container { grid-template-columns: 1fr 1fr; gap: 12px; }
    .kpi-card { padding: 16px; }
    .kpi-value { font-size: 1.5rem; }
    .kpi-label { font-size: 0.7rem; }
    
    .section-header { flex-direction: column; align-items: flex-start; gap: 12px; }
    .section-icon { width: 40px; height: 40px; font-size: 1.2rem; }
    
    .chart-container { padding: 16px; }
    
    .ai-box { padding: 20px; }
    .ai-header { flex-direction: column; text-align: center; }
    
    .stTabs [data-baseweb="tab"] { padding: 10px 14px !important; font-size: 0.8rem !important; }
}

@media (max-width: 480px) {
    .kpi-container { grid-template-columns: 1fr; }
    .hero-badge-container { flex-direction: column; }
}

/* =============================================================================
   UTILITY CLASSES
============================================================================= */

.text-primary { color: var(--text-primary) !important; }
.text-secondary { color: var(--text-secondary) !important; }
.text-muted { color: var(--text-muted) !important; }
.text-success { color: var(--success) !important; }
.text-warning { color: var(--warning) !important; }
.text-danger { color: var(--danger) !important; }

.bg-glass { background: var(--glass) !important; }
.bg-card { background: var(--bg-card) !important; }

.border-glass { border: 1px solid var(--glass-border) !important; }
.border-primary { border-color: var(--primary) !important; }

.rounded-md { border-radius: var(--radius-md) !important; }
.rounded-lg { border-radius: var(--radius-lg) !important; }
.rounded-xl { border-radius: var(--radius-xl) !important; }

.shadow-glow-primary { box-shadow: var(--glow-primary) !important; }
.shadow-glow-success { box-shadow: var(--glow-success) !important; }

.mt-0 { margin-top: 0 !important; }
.mt-1 { margin-top: var(--space-sm) !important; }
.mt-2 { margin-top: var(--space-md) !important; }
.mt-3 { margin-top: var(--space-lg) !important; }
.mt-4 { margin-top: var(--space-xl) !important; }

.mb-0 { margin-bottom: 0 !important; }
.mb-1 { margin-bottom: var(--space-sm) !important; }
.mb-2 { margin-bottom: var(--space-md) !important; }
.mb-3 { margin-bottom: var(--space-lg) !important; }
.mb-4 { margin-bottom: var(--space-xl) !important; }

.p-0 { padding: 0 !important; }
.p-1 { padding: var(--space-sm) !important; }
.p-2 { padding: var(--space-md) !important; }
.p-3 { padding: var(--space-lg) !important; }
.p-4 { padding: var(--space-xl) !important; }

.flex { display: flex !important; }
.flex-col { flex-direction: column !important; }
.items-center { align-items: center !important; }
.justify-center { justify-content: center !important; }
.justify-between { justify-content: space-between !important; }
.gap-1 { gap: var(--space-sm) !important; }
.gap-2 { gap: var(--space-md) !important; }
.gap-3 { gap: var(--space-lg) !important; }

.w-full { width: 100% !important; }
.h-full { height: 100% !important; }

.hidden { display: none !important; }
.visible { visibility: visible !important; }

</style>
""", unsafe_allow_html=True)

# =============================================================================
# UI HELPER COMPONENTS (FIXED HTML - SINGLE LINE)
# =============================================================================

def render_hero_header():
    """Render animated hero header."""
    st.markdown('<div class="hero-header"><div class="hero-title">🚀 UAE Promo Pulse Simulator</div><div class="hero-subtitle">Intelligent Promotional Simulation & Inventory Analytics Platform for UAE Retail</div><div class="hero-badge-container"><div class="hero-badge"><div class="hero-badge-dot"></div><span>Live Dashboard</span></div><div class="hero-badge success">📊 Real-time Analytics</div><div class="hero-badge warning">🎯 AI-Powered</div></div></div>', unsafe_allow_html=True)


def render_section_header(icon, title, subtitle=None):
    """Render premium section header."""
    if subtitle:
        st.markdown(f'<div class="section-header"><div class="section-icon">{icon}</div><div class="section-content"><div class="section-title">{title}</div><div class="section-subtitle">{subtitle}</div></div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="section-header"><div class="section-icon">{icon}</div><div class="section-content"><div class="section-title">{title}</div></div></div>', unsafe_allow_html=True)


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
    st.markdown(f'<div class="ai-box"><div class="ai-header"><div class="ai-avatar">🤖</div><div class="ai-info"><div class="ai-title">AI-Powered Insights</div><div class="ai-subtitle">Based on real-time data analysis</div></div></div><div class="ai-items">{items_html}</div></div>', unsafe_allow_html=True)


def render_chart_container_start(title=None, icon="📊"):
    """Start a chart container."""
    if title:
        st.markdown(f'<div class="chart-container"><div class="chart-title"><span class="chart-title-icon">{icon}</span>{title}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)


def render_chart_container_end():
    """End a chart container."""
    st.markdown('</div>', unsafe_allow_html=True)


def render_chart_title(title, icon="📊"):
    """Render chart title."""
    st.markdown(f'<div class="chart-title"><span class="chart-title-icon">{icon}</span>{title}</div>', unsafe_allow_html=True)


def render_filter_box_start(title="🎛️ Chart Filters"):
    """Start a filter box."""
    st.markdown(f'<div class="filter-box"><div class="filter-title">{title}</div>', unsafe_allow_html=True)


def render_filter_box_end():
    """End a filter box."""
    st.markdown('</div>', unsafe_allow_html=True)


def render_status_card(label, value, status_type=""):
    """Render a status card."""
    st.markdown(f'<div class="status-card"><div class="status-label">{label}</div><div class="status-value {status_type}">{value}</div></div>', unsafe_allow_html=True)


def render_constraint_card(icon, label, status, status_type="pass"):
    """Render constraint card."""
    st.markdown(f'<div class="constraint-card"><span class="constraint-icon">{icon}</span><div class="constraint-content"><div class="constraint-label">{label}</div><div class="constraint-status {status_type}">{status}</div></div></div>', unsafe_allow_html=True)


def render_footer():
    """Render page footer."""
    st.markdown('<div class="footer"><span class="footer-brand">UAE Promo Pulse Simulator</span><br><span style="font-size: 0.85rem; margin-top: 8px; display: block;">Premium Analytics Dashboard | Data Rescue Team</span><span style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; display: block;">© 2024 All Rights Reserved | Built with Streamlit + Plotly</span></div>', unsafe_allow_html=True)


def render_divider():
    """Render gradient divider."""
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


def render_divider_subtle():
    """Render subtle divider."""
    st.markdown('<div class="divider-subtle"></div>', unsafe_allow_html=True)


def render_divider_gradient():
    """Render gradient divider."""
    st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)


def render_file_success(filename, rows, cols):
    """Render file upload success."""
    st.markdown(f'<div class="insight-box success"><div class="insight-header"><span class="insight-icon">✅</span><div class="insight-title">{filename}</div></div><p class="insight-text">{rows:,} rows × {cols} columns loaded successfully</p></div>', unsafe_allow_html=True)


def render_file_error(message):
    """Render file upload error."""
    st.markdown(f'<div class="insight-box danger"><div class="insight-header"><span class="insight-icon">❌</span><div class="insight-title">Invalid File Format</div></div><p class="insight-text">{message}</p></div>', unsafe_allow_html=True)


def render_file_warning(message):
    """Render file warning."""
    st.markdown(f'<div class="insight-box warning"><div class="insight-header"><span class="insight-icon">⚠️</span><div class="insight-title">Warning</div></div><p class="insight-text">{message}</p></div>', unsafe_allow_html=True)


def render_loading_skeleton():
    """Render loading skeleton."""
    st.markdown('<div style="display: flex; flex-direction: column; gap: 12px;"><div class="skeleton" style="height: 40px; width: 60%;"></div><div class="skeleton" style="height: 200px; width: 100%;"></div><div class="skeleton" style="height: 20px; width: 80%;"></div></div>', unsafe_allow_html=True)


def render_empty_state(icon, title, message):
    """Render empty state."""
    st.markdown(f'<div style="text-align: center; padding: 60px 40px;"><div style="font-size: 4rem; margin-bottom: 16px;">{icon}</div><div style="font-size: 1.3rem; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">{title}</div><div style="color: var(--text-muted); font-size: 1rem;">{message}</div></div>', unsafe_allow_html=True)


# =============================================================================
# CHART STYLING UTILITIES
# =============================================================================

def get_chart_colors():
    """Get premium chart color palette."""
    return ['#6366f1', '#ec4899', '#06b6d4', '#10b981', '#f59e0b', '#8b5cf6', '#f43f5e', '#14b8a6', '#f97316', '#84cc16']


def get_chart_color_map():
    """Get color map for categorical data."""
    return {
        'primary': '#6366f1',
        'secondary': '#ec4899',
        'accent': '#06b6d4',
        'success': '#10b981',
        'warning': '#f59e0b',
        'danger': '#ef4444',
        'info': '#3b82f6',
        'purple': '#8b5cf6',
        'pink': '#f43f5e',
        'teal': '#14b8a6'
    }


def apply_chart_style(fig, height=400, show_legend=True):
    """Apply premium styling to Plotly figure."""
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Inter, -apple-system, BlinkMacSystemFont, sans-serif',
            color='#a1a1aa',
            size=12
        ),
        title=dict(
            font=dict(size=16, color='#ffffff', family='Space Grotesk, Inter, sans-serif'),
            x=0,
            xanchor='left'
        ),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='#71717a', size=11),
            title_font=dict(color='#a1a1aa', size=12)
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.05)',
            linecolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='#71717a', size=11),
            title_font=dict(color='#a1a1aa', size=12)
        ),
        hoverlabel=dict(
            bgcolor='#1a1a2e',
            bordercolor='#6366f1',
            font=dict(color='#ffffff', size=13, family='Inter, sans-serif')
        ),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1,
            font=dict(color='#a1a1aa', size=11),
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ) if show_legend else dict(visible=False),
        margin=dict(l=40, r=40, t=60, b=40),
        height=height,
        hovermode='x unified'
    )
    return fig


def create_gauge_chart(value, title, max_value=100, color="primary"):
    """Create a gauge chart."""
    colors = {
        'primary': ['#4f46e5', '#6366f1', '#818cf8'],
        'success': ['#059669', '#10b981', '#34d399'],
        'warning': ['#d97706', '#f59e0b', '#fbbf24'],
        'danger': ['#dc2626', '#ef4444', '#f87171']
    }
    color_scale = colors.get(color, colors['primary'])
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'size': 16, 'color': '#ffffff'}},
        number={'font': {'size': 36, 'color': '#ffffff'}},
        gauge={
            'axis': {'range': [0, max_value], 'tickcolor': '#71717a', 'tickfont': {'color': '#71717a'}},
            'bar': {'color': color_scale[1]},
            'bgcolor': 'rgba(255,255,255,0.05)',
            'borderwidth': 2,
            'bordercolor': 'rgba(255,255,255,0.1)',
            'steps': [
                {'range': [0, max_value * 0.5], 'color': 'rgba(255,255,255,0.02)'},
                {'range': [max_value * 0.5, max_value * 0.8], 'color': 'rgba(255,255,255,0.04)'},
                {'range': [max_value * 0.8, max_value], 'color': 'rgba(255,255,255,0.06)'}
            ],
            'threshold': {
                'line': {'color': color_scale[2], 'width': 4},
                'thickness': 0.8,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#a1a1aa'},
        height=250,
        margin=dict(l=30, r=30, t=50, b=30)
    )
    
    return fig


# =============================================================================
# DATA VALIDATION & LOADING
# =============================================================================

EXPECTED_COLUMNS = {
    'sales': ['transaction_id', 'sku_id', 'store_id', 'quantity_sold', 'unit_price', 'transaction_date'],
    'inventory': ['record_id', 'sku_id', 'store_id', 'stock_level', 'reorder_point', 'reorder_quantity', 'last_updated'],
    'promotions': ['promotion_id', 'sku_id', 'store_id', 'promotion_type', 'discount_percentage', 'start_date', 'end_date'],
    'products': ['sku_id', 'product_name', 'category', 'brand', 'unit_cost', 'supplier_id']
}


def validate_dataframe(df, file_type):
    """Validate DataFrame has required columns."""
    if df is None or df.empty:
        return False, "Empty dataframe"
    
    expected = set(EXPECTED_COLUMNS.get(file_type, []))
    df.columns = df.columns.str.lower().str.strip()
    actual = set(df.columns)
    
    missing = expected - actual
    if missing:
        return False, f"Missing columns: {', '.join(missing)}"
    
    return True, "Valid"


@st.cache_data(ttl=3600)
def load_and_process_data(sales_file, inventory_file, promotions_file, products_file=None):
    """Load and process all data files with caching."""
    try:
        # Load files
        sales_df = pd.read_csv(sales_file)
        inventory_df = pd.read_csv(inventory_file)
        promotions_df = pd.read_csv(promotions_file)
        products_df = pd.read_csv(products_file) if products_file else None
        
        # Normalize column names
        sales_df.columns = sales_df.columns.str.lower().str.strip().str.replace(' ', '_')
        inventory_df.columns = inventory_df.columns.str.lower().str.strip().str.replace(' ', '_')
        promotions_df.columns = promotions_df.columns.str.lower().str.strip().str.replace(' ', '_')
        if products_df is not None:
            products_df.columns = products_df.columns.str.lower().str.strip().str.replace(' ', '_')
        
        # Validate required columns (flexible validation)
        def validate_df(df, name, required_cols):
            actual = set(df.columns)
            missing = set(required_cols) - actual
            if missing:
                return False, f"Missing columns: {', '.join(missing)}"
            return True, "Valid"
        
        # Basic validation
        sales_valid, sales_msg = validate_df(sales_df, 'sales', ['sku_id', 'store_id', 'quantity_sold'])
        inventory_valid, inv_msg = validate_df(inventory_df, 'inventory', ['sku_id', 'store_id', 'stock_level'])
        promo_valid, promo_msg = validate_df(promotions_df, 'promotions', ['sku_id', 'discount_percentage'])
        
        if not sales_valid:
            return None, None, None, None, f"Sales: {sales_msg}"
        if not inventory_valid:
            return None, None, None, None, f"Inventory: {inv_msg}"
        if not promo_valid:
            return None, None, None, None, f"Promotions: {promo_msg}"
        
        # Process sales dates
        date_cols = ['transaction_date', 'date', 'sale_date', 'order_date']
        for col in date_cols:
            if col in sales_df.columns:
                sales_df['transaction_date'] = pd.to_datetime(sales_df[col], errors='coerce')
                break
        
        if 'transaction_date' in sales_df.columns:
            sales_df['date'] = sales_df['transaction_date'].dt.date
            sales_df['month'] = sales_df['transaction_date'].dt.to_period('M').astype(str)
            sales_df['week'] = sales_df['transaction_date'].dt.isocalendar().week
            sales_df['day_of_week'] = sales_df['transaction_date'].dt.day_name()
            sales_df['hour'] = sales_df['transaction_date'].dt.hour
            sales_df['year'] = sales_df['transaction_date'].dt.year
            sales_df['quarter'] = sales_df['transaction_date'].dt.quarter
        
        # Process promotion dates
        if 'start_date' in promotions_df.columns:
            promotions_df['start_date'] = pd.to_datetime(promotions_df['start_date'], errors='coerce')
        if 'end_date' in promotions_df.columns:
            promotions_df['end_date'] = pd.to_datetime(promotions_df['end_date'], errors='coerce')
        
        # Calculate revenue
        if 'quantity_sold' in sales_df.columns and 'unit_price' in sales_df.columns:
            sales_df['revenue'] = sales_df['quantity_sold'] * sales_df['unit_price']
        elif 'quantity_sold' in sales_df.columns:
            sales_df['revenue'] = sales_df['quantity_sold'] * 10  # Default price
        
        # Calculate inventory metrics
        if 'stock_level' in inventory_df.columns:
            if 'reorder_point' not in inventory_df.columns:
                inventory_df['reorder_point'] = inventory_df['stock_level'] * 0.3
            
            inventory_df['stock_status'] = inventory_df.apply(
                lambda x: 'Critical' if x['stock_level'] <= x['reorder_point'] * 0.5
                else 'Low' if x['stock_level'] <= x['reorder_point']
                else 'Healthy', axis=1
            )
            inventory_df['stock_ratio'] = inventory_df['stock_level'] / inventory_df['reorder_point'].replace(0, 1)
        
        # Merge product info if available
        if products_df is not None:
            if 'category' in products_df.columns and 'category' not in sales_df.columns:
                sales_df = sales_df.merge(products_df[['sku_id', 'category', 'brand']].drop_duplicates(), 
                                         on='sku_id', how='left')
            if 'category' in products_df.columns and 'category' not in inventory_df.columns:
                inventory_df = inventory_df.merge(products_df[['sku_id', 'category', 'brand']].drop_duplicates(), 
                                                  on='sku_id', how='left')
            if 'category' in products_df.columns and 'category' not in promotions_df.columns:
                promotions_df = promotions_df.merge(products_df[['sku_id', 'category', 'brand']].drop_duplicates(), 
                                                    on='sku_id', how='left')
        
        return sales_df, inventory_df, promotions_df, products_df, None
        
    except Exception as e:
        return None, None, None, None, str(e)

# =============================================================================
# SAMPLE DATA GENERATOR (COMPREHENSIVE) - FIXED
# =============================================================================

def generate_sample_data():
    """Generate comprehensive sample data for demonstration."""
    np.random.seed(42)
    
    # Configuration
    n_days = 365
    n_skus = 150
    n_stores = 25
    n_sales = 75000
    n_promos = 300
    
    # Generate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=n_days)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate SKUs with categories and brands
    categories = ['Electronics', 'Clothing', 'Food & Beverage', 'Home & Garden', 'Health & Beauty', 'Sports & Outdoors', 'Toys & Games', 'Automotive']
    brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E', 'Premium Brand', 'Value Brand', 'Local Brand']
    
    skus = []
    sku_categories = {}
    sku_brands = {}
    sku_prices = {}
    
    for i in range(1, n_skus + 1):
        sku_id = f'SKU_{str(i).zfill(4)}'
        skus.append(sku_id)
        sku_categories[sku_id] = np.random.choice(categories)
        sku_brands[sku_id] = np.random.choice(brands)
        # Price varies by category
        base_prices = {'Electronics': 200, 'Clothing': 80, 'Food & Beverage': 25, 'Home & Garden': 100, 
                      'Health & Beauty': 50, 'Sports & Outdoors': 120, 'Toys & Games': 40, 'Automotive': 150}
        base = base_prices.get(sku_categories[sku_id], 50)
        sku_prices[sku_id] = round(np.random.uniform(base * 0.5, base * 2), 2)
    
    # Generate stores with regions
    regions = ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman', 'RAK']
    store_types = ['Hypermarket', 'Supermarket', 'Express', 'Online']
    
    stores = []
    store_regions = {}
    store_types_map = {}
    
    for i in range(1, n_stores + 1):
        store_id = f'STORE_{str(i).zfill(3)}'
        stores.append(store_id)
        store_regions[store_id] = np.random.choice(regions, p=[0.35, 0.25, 0.2, 0.1, 0.1])
        store_types_map[store_id] = np.random.choice(store_types, p=[0.2, 0.4, 0.3, 0.1])
    
    # Generate promotion types
    promo_types = ['BOGO', 'Percentage Off', 'Bundle Deal', 'Flash Sale', 'Clearance', 'Seasonal', 'Member Exclusive', 'Buy More Save More']
    
    # ==========================================================================
    # SALES DATA
    # ==========================================================================
    
    # Create seasonal patterns - FIXED: accepts pandas Timestamp
    def get_seasonal_factor(date):
        # Convert to pandas Timestamp if needed
        if isinstance(date, np.datetime64):
            date = pd.Timestamp(date)
        month = date.month
        # Ramadan/Eid boost (varies by year, simplified)
        if month in [3, 4]:  # Approximate Ramadan period
            return 1.4
        # Summer (lower due to holidays)
        elif month in [7, 8]:
            return 0.85
        # Year-end shopping
        elif month in [11, 12]:
            return 1.3
        # Back to school
        elif month == 9:
            return 1.15
        else:
            return 1.0
    
    # Generate sales transactions
    sales_data = {
        'transaction_id': [],
        'sku_id': [],
        'store_id': [],
        'quantity_sold': [],
        'unit_price': [],
        'transaction_date': [],
        'customer_id': [],
        'payment_method': []
    }
    
    payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment', 'Online']
    
    # Pre-convert dates to list of Timestamps for faster random selection
    dates_list = dates.tolist()
    
    for i in range(1, n_sales + 1):
        sku = np.random.choice(skus)
        store = np.random.choice(stores)
        # Use random index to select date
        date_idx = np.random.randint(0, len(dates_list))
        date = dates_list[date_idx]
        
        seasonal = get_seasonal_factor(date)
        
        # Weekday effect
        weekday_factor = 1.2 if date.weekday() >= 4 else 1.0  # Weekend boost
        
        # Store type effect
        store_factor = {'Hypermarket': 1.3, 'Supermarket': 1.0, 'Express': 0.7, 'Online': 1.1}.get(store_types_map[store], 1.0)
        
        base_qty = max(1, int(np.random.exponential(3) * seasonal * weekday_factor * store_factor))
        
        sales_data['transaction_id'].append(f'TXN_{str(i).zfill(7)}')
        sales_data['sku_id'].append(sku)
        sales_data['store_id'].append(store)
        sales_data['quantity_sold'].append(base_qty)
        sales_data['unit_price'].append(sku_prices[sku])
        sales_data['transaction_date'].append(date)
        sales_data['customer_id'].append(f'CUST_{str(np.random.randint(1, 10000)).zfill(5)}')
        sales_data['payment_method'].append(np.random.choice(payment_methods, p=[0.15, 0.35, 0.25, 0.15, 0.1]))
    
    sales_df = pd.DataFrame(sales_data)
    sales_df['transaction_date'] = pd.to_datetime(sales_df['transaction_date'])
    sales_df['revenue'] = sales_df['quantity_sold'] * sales_df['unit_price']
    sales_df['date'] = sales_df['transaction_date'].dt.date
    sales_df['month'] = sales_df['transaction_date'].dt.to_period('M').astype(str)
    sales_df['week'] = sales_df['transaction_date'].dt.isocalendar().week
    sales_df['day_of_week'] = sales_df['transaction_date'].dt.day_name()
    sales_df['hour'] = np.random.choice(range(8, 23), len(sales_df))  # Store hours
    sales_df['year'] = sales_df['transaction_date'].dt.year
    sales_df['quarter'] = sales_df['transaction_date'].dt.quarter
    sales_df['category'] = sales_df['sku_id'].map(sku_categories)
    sales_df['brand'] = sales_df['sku_id'].map(sku_brands)
    sales_df['region'] = sales_df['store_id'].map(store_regions)
    sales_df['store_type'] = sales_df['store_id'].map(store_types_map)
    
    # ==========================================================================
    # INVENTORY DATA
    # ==========================================================================
    
    inventory_data = {
        'record_id': [],
        'sku_id': [],
        'store_id': [],
        'stock_level': [],
        'reorder_point': [],
        'reorder_quantity': [],
        'last_updated': [],
        'warehouse_location': [],
        'supplier_id': []
    }
    
    warehouses = ['WH-Dubai-1', 'WH-Dubai-2', 'WH-AbuDhabi', 'WH-Sharjah', 'WH-Central']
    
    # Get last 30 dates for inventory updates
    recent_dates = dates_list[-30:]
    
    record_id = 1
    for sku in skus:
        for store in stores:
            # Base stock varies by store type
            base_stock = {'Hypermarket': 300, 'Supermarket': 150, 'Express': 50, 'Online': 200}.get(store_types_map[store], 100)
            
            # Category affects reorder points
            cat_factor = {'Electronics': 0.7, 'Food & Beverage': 1.5, 'Clothing': 0.9}.get(sku_categories[sku], 1.0)
            
            stock = max(0, int(np.random.normal(base_stock, base_stock * 0.4)))
            reorder_pt = int(base_stock * 0.3 * cat_factor)
            reorder_qty = int(base_stock * 0.6)
            
            inventory_data['record_id'].append(f'INV_{str(record_id).zfill(6)}')
            inventory_data['sku_id'].append(sku)
            inventory_data['store_id'].append(store)
            inventory_data['stock_level'].append(stock)
            inventory_data['reorder_point'].append(reorder_pt)
            inventory_data['reorder_quantity'].append(reorder_qty)
            inventory_data['last_updated'].append(recent_dates[np.random.randint(0, len(recent_dates))])
            inventory_data['warehouse_location'].append(np.random.choice(warehouses))
            inventory_data['supplier_id'].append(f'SUP_{str(np.random.randint(1, 50)).zfill(3)}')
            record_id += 1
    
    inventory_df = pd.DataFrame(inventory_data)
    inventory_df['last_updated'] = pd.to_datetime(inventory_df['last_updated'])
    inventory_df['stock_status'] = inventory_df.apply(
        lambda x: 'Critical' if x['stock_level'] <= x['reorder_point'] * 0.5
        else 'Low' if x['stock_level'] <= x['reorder_point']
        else 'Healthy', axis=1
    )
    inventory_df['stock_ratio'] = inventory_df['stock_level'] / inventory_df['reorder_point'].replace(0, 1)
    inventory_df['category'] = inventory_df['sku_id'].map(sku_categories)
    inventory_df['brand'] = inventory_df['sku_id'].map(sku_brands)
    inventory_df['region'] = inventory_df['store_id'].map(store_regions)
    inventory_df['store_type'] = inventory_df['store_id'].map(store_types_map)
    
    # Calculate days of stock (based on average daily sales)
    avg_daily_sales = sales_df.groupby(['sku_id', 'store_id'])['quantity_sold'].sum() / n_days
    inventory_df['avg_daily_sales'] = inventory_df.apply(
        lambda x: avg_daily_sales.get((x['sku_id'], x['store_id']), 1), axis=1
    )
    inventory_df['days_of_stock'] = (inventory_df['stock_level'] / inventory_df['avg_daily_sales'].replace(0, 0.1)).round(1)
    inventory_df['days_of_stock'] = inventory_df['days_of_stock'].clip(0, 365)
    
    # ==========================================================================
    # PROMOTIONS DATA
    # ==========================================================================
    
    promotions_data = {
        'promotion_id': [],
        'sku_id': [],
        'store_id': [],
        'promotion_type': [],
        'discount_percentage': [],
        'start_date': [],
        'end_date': [],
        'budget': [],
        'target_sales_lift': [],
        'actual_sales_lift': [],
        'promotion_name': []
    }
    
    promo_names = ['Summer Sale', 'Ramadan Special', 'Eid Offer', 'Back to School', 'Weekend Deal', 
                  'Flash Friday', 'Member Exclusive', 'Clearance Event', 'New Arrival Promo', 'Bundle Bonanza']
    
    # Use dates excluding last 30 days for promotion start dates
    promo_start_dates = dates_list[:-30]
    
    for i in range(1, n_promos + 1):
        sku = np.random.choice(skus)
        store = np.random.choice(stores + ['ALL'])  # Some promos are store-wide
        promo_type = np.random.choice(promo_types)
        
        # Discount varies by type
        if promo_type == 'BOGO':
            discount = 50
        elif promo_type == 'Clearance':
            discount = np.random.choice([40, 50, 60, 70])
        elif promo_type == 'Flash Sale':
            discount = np.random.choice([20, 25, 30, 35])
        else:
            discount = np.random.choice([5, 10, 15, 20, 25, 30])
        
        start_idx = np.random.randint(0, len(promo_start_dates))
        start = promo_start_dates[start_idx]
        duration = np.random.randint(3, 21)
        end = start + timedelta(days=duration)
        
        # Budget based on discount and duration
        budget = discount * duration * np.random.randint(100, 500)
        
        # Target and actual lift
        target_lift = discount * 0.8 + np.random.uniform(-5, 10)
        actual_lift = target_lift * np.random.uniform(0.7, 1.3)
        
        promotions_data['promotion_id'].append(f'PROMO_{str(i).zfill(4)}')
        promotions_data['sku_id'].append(sku)
        promotions_data['store_id'].append(store)
        promotions_data['promotion_type'].append(promo_type)
        promotions_data['discount_percentage'].append(discount)
        promotions_data['start_date'].append(start)
        promotions_data['end_date'].append(end)
        promotions_data['budget'].append(budget)
        promotions_data['target_sales_lift'].append(round(target_lift, 1))
        promotions_data['actual_sales_lift'].append(round(actual_lift, 1))
        promotions_data['promotion_name'].append(np.random.choice(promo_names))
    
    promotions_df = pd.DataFrame(promotions_data)
    promotions_df['start_date'] = pd.to_datetime(promotions_df['start_date'])
    promotions_df['end_date'] = pd.to_datetime(promotions_df['end_date'])
    promotions_df['duration_days'] = (promotions_df['end_date'] - promotions_df['start_date']).dt.days
    promotions_df['category'] = promotions_df['sku_id'].map(sku_categories)
    promotions_df['brand'] = promotions_df['sku_id'].map(sku_brands)
    promotions_df['is_active'] = (promotions_df['start_date'] <= pd.Timestamp.now()) & (promotions_df['end_date'] >= pd.Timestamp.now())
    promotions_df['roi'] = ((promotions_df['actual_sales_lift'] / 100) * promotions_df['budget'] * 2 - promotions_df['budget']) / promotions_df['budget'] * 100
    
    return sales_df, inventory_df, promotions_df

# =============================================================================
# DASHBOARD SECTIONS WITH LOCAL FILTERS
# =============================================================================

def render_overview_kpis(sales_df, inventory_df, promotions_df):
    """Render comprehensive overview KPIs."""
    
    # Calculate metrics
    total_revenue = sales_df['revenue'].sum()
    total_transactions = sales_df['transaction_id'].nunique()
    total_units = sales_df['quantity_sold'].sum()
    total_skus = sales_df['sku_id'].nunique()
    total_stores = sales_df['store_id'].nunique()
    avg_order_value = total_revenue / total_transactions if total_transactions > 0 else 0
    
    # Inventory metrics
    critical_stock = len(inventory_df[inventory_df['stock_status'] == 'Critical'])
    low_stock = len(inventory_df[inventory_df['stock_status'] == 'Low'])
    healthy_stock = len(inventory_df[inventory_df['stock_status'] == 'Healthy'])
    stock_health_pct = (healthy_stock / len(inventory_df) * 100) if len(inventory_df) > 0 else 0
    
    # Promotion metrics
    active_promos = len(promotions_df[promotions_df['is_active']]) if 'is_active' in promotions_df.columns else len(promotions_df)
    avg_discount = promotions_df['discount_percentage'].mean()
    
    # Period comparison (simulate)
    prev_revenue = total_revenue * 0.92
    revenue_change = ((total_revenue - prev_revenue) / prev_revenue * 100) if prev_revenue > 0 else 0
    
    prev_transactions = total_transactions * 0.95
    trans_change = ((total_transactions - prev_transactions) / prev_transactions * 100) if prev_transactions > 0 else 0
    
    kpis = [
        {"icon": "💰", "value": f"${total_revenue:,.0f}", "label": "Total Revenue", "type": "primary", "delta": f"{revenue_change:+.1f}%", "delta_type": "positive" if revenue_change > 0 else "negative"},
        {"icon": "🛒", "value": f"{total_transactions:,}", "label": "Transactions", "type": "success", "delta": f"{trans_change:+.1f}%", "delta_type": "positive" if trans_change > 0 else "negative"},
        {"icon": "📦", "value": f"{total_units:,}", "label": "Units Sold", "type": "accent"},
        {"icon": "💵", "value": f"${avg_order_value:.2f}", "label": "Avg Order Value", "type": "secondary"},
        {"icon": "🏷️", "value": f"{total_skus}", "label": "Active SKUs", "type": "info"},
        {"icon": "🏪", "value": f"{total_stores}", "label": "Stores", "type": "primary"},
        {"icon": "⚠️", "value": f"{critical_stock + low_stock}", "label": "Stock Alerts", "type": "danger" if critical_stock > 50 else "warning"},
        {"icon": "🎯", "value": f"{active_promos}", "label": "Active Promos", "type": "success"},
    ]
    
    render_kpi_row(kpis)


def render_sales_analysis(sales_df):
    """Render comprehensive sales analysis with local filters."""
    render_section_header("📈", "Sales Performance Analytics", "Deep dive into sales metrics with interactive filters")
    
    # =========================================================================
    # LOCAL FILTERS FOR THIS SECTION
    # =========================================================================
    st.markdown("#### 🎛️ Sales Filters")
    
    filter_cols = st.columns([2, 2, 2, 2])
    
    with filter_cols[0]:
        time_granularity = st.selectbox(
            "📅 Time Granularity",
            ["Daily", "Weekly", "Monthly", "Quarterly"],
            key="sales_time_granularity"
        )
    
    with filter_cols[1]:
        if 'category' in sales_df.columns:
            categories = ['All Categories'] + sorted(sales_df['category'].dropna().unique().tolist())
            selected_category = st.selectbox(
                "🏷️ Category",
                categories,
                key="sales_category_filter"
            )
        else:
            selected_category = 'All Categories'
    
    with filter_cols[2]:
        if 'region' in sales_df.columns:
            regions = ['All Regions'] + sorted(sales_df['region'].dropna().unique().tolist())
            selected_region = st.selectbox(
                "🌍 Region",
                regions,
                key="sales_region_filter"
            )
        else:
            selected_region = 'All Regions'
    
    with filter_cols[3]:
        chart_type = st.selectbox(
            "📊 Chart Style",
            ["Area Chart", "Line Chart", "Bar Chart"],
            key="sales_chart_type"
        )
    
    # Second row of filters
    filter_cols2 = st.columns([2, 2, 2, 2])
    
    with filter_cols2[0]:
        if 'brand' in sales_df.columns:
            brands = ['All Brands'] + sorted(sales_df['brand'].dropna().unique().tolist())
            selected_brand = st.selectbox(
                "🏢 Brand",
                brands,
                key="sales_brand_filter"
            )
        else:
            selected_brand = 'All Brands'
    
    with filter_cols2[1]:
        if 'store_type' in sales_df.columns:
            store_types = ['All Store Types'] + sorted(sales_df['store_type'].dropna().unique().tolist())
            selected_store_type = st.selectbox(
                "🏪 Store Type",
                store_types,
                key="sales_store_type_filter"
            )
        else:
            selected_store_type = 'All Store Types'
    
    with filter_cols2[2]:
        if 'month' in sales_df.columns:
            months = sorted(sales_df['month'].unique().tolist())
            date_range = st.select_slider(
                "📆 Date Range",
                options=months,
                value=(months[0], months[-1]),
                key="sales_date_range"
            )
        else:
            date_range = None
    
    with filter_cols2[3]:
        top_n = st.slider("🔝 Top N Items", 5, 20, 10, key="sales_top_n")
    
    st.markdown("")
    
    # =========================================================================
    # FILTER DATA
    # =========================================================================
    filtered_df = sales_df.copy()
    
    if selected_category != 'All Categories' and 'category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    
    if selected_region != 'All Regions' and 'region' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['region'] == selected_region]
    
    if selected_brand != 'All Brands' and 'brand' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['brand'] == selected_brand]
    
    if selected_store_type != 'All Store Types' and 'store_type' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['store_type'] == selected_store_type]
    
    if date_range and 'month' in filtered_df.columns:
        filtered_df = filtered_df[(filtered_df['month'] >= date_range[0]) & (filtered_df['month'] <= date_range[1])]
    
    if filtered_df.empty:
        render_empty_state("📊", "No Data Available", "Try adjusting your filters to see results.")
        return
    
    # =========================================================================
    # SECTION KPIs
    # =========================================================================
    section_revenue = filtered_df['revenue'].sum()
    section_units = filtered_df['quantity_sold'].sum()
    section_transactions = filtered_df['transaction_id'].nunique()
    section_aov = section_revenue / section_transactions if section_transactions > 0 else 0
    
    section_kpis = [
        {"icon": "💰", "value": f"${section_revenue:,.0f}", "label": "Filtered Revenue", "type": "primary"},
        {"icon": "📦", "value": f"{section_units:,}", "label": "Units Sold", "type": "success"},
        {"icon": "🛒", "value": f"{section_transactions:,}", "label": "Transactions", "type": "accent"},
        {"icon": "💵", "value": f"${section_aov:.2f}", "label": "Avg Order Value", "type": "secondary"},
    ]
    render_kpi_row(section_kpis)
    
    render_divider_subtle()
    
    # =========================================================================
    # REVENUE TREND CHART
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title("Revenue Trend Over Time", "💰")
        
        # Aggregate based on granularity
        if time_granularity == "Daily":
            agg_df = filtered_df.groupby('date').agg({'revenue': 'sum', 'quantity_sold': 'sum', 'transaction_id': 'nunique'}).reset_index()
            x_col = 'date'
        elif time_granularity == "Weekly":
            agg_df = filtered_df.groupby('week').agg({'revenue': 'sum', 'quantity_sold': 'sum', 'transaction_id': 'nunique'}).reset_index()
            x_col = 'week'
        elif time_granularity == "Monthly":
            agg_df = filtered_df.groupby('month').agg({'revenue': 'sum', 'quantity_sold': 'sum', 'transaction_id': 'nunique'}).reset_index()
            x_col = 'month'
        else:  # Quarterly
            agg_df = filtered_df.groupby('quarter').agg({'revenue': 'sum', 'quantity_sold': 'sum', 'transaction_id': 'nunique'}).reset_index()
            x_col = 'quarter'
        
        agg_df.columns = [x_col, 'Revenue', 'Units', 'Transactions']
        
        if chart_type == "Area Chart":
            fig = px.area(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'])
            fig.update_traces(fill='tozeroy', fillcolor='rgba(99, 102, 241, 0.3)', line=dict(width=3))
        elif chart_type == "Line Chart":
            fig = px.line(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'], markers=True)
            fig.update_traces(line=dict(width=3), marker=dict(size=8))
        else:
            fig = px.bar(agg_df, x=x_col, y='Revenue', color_discrete_sequence=['#6366f1'])
        
        fig = apply_chart_style(fig, height=380)
        fig.update_layout(xaxis_title=time_granularity, yaxis_title="Revenue ($)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_title("Units Sold Trend", "📦")
        
        if chart_type == "Area Chart":
            fig2 = px.area(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'])
            fig2.update_traces(fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.3)', line=dict(width=3))
        elif chart_type == "Line Chart":
            fig2 = px.line(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'], markers=True)
            fig2.update_traces(line=dict(width=3), marker=dict(size=8))
        else:
            fig2 = px.bar(agg_df, x=x_col, y='Units', color_discrete_sequence=['#10b981'])
        
        fig2 = apply_chart_style(fig2, height=380)
        fig2.update_layout(xaxis_title=time_granularity, yaxis_title="Units")
        st.plotly_chart(fig2, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # CATEGORY & BRAND ANALYSIS
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title("Revenue by Category", "🏷️")
        
        if 'category' in filtered_df.columns:
            cat_df = filtered_df.groupby('category').agg({'revenue': 'sum'}).reset_index()
            cat_df = cat_df.nlargest(top_n, 'revenue')
            cat_df.columns = ['Category', 'Revenue']
            
            fig3 = px.pie(cat_df, values='Revenue', names='Category', 
                         color_discrete_sequence=get_chart_colors(),
                         hole=0.55)
            fig3 = apply_chart_style(fig3, height=380)
            fig3.update_traces(textposition='outside', textinfo='percent+label',
                             textfont=dict(size=11))
            st.plotly_chart(fig3, use_container_width=True)
        else:
            render_empty_state("📊", "Category data not available", "")
    
    with col2:
        render_chart_title("Top Performing Categories", "📊")
        
        if 'category' in filtered_df.columns:
            fig4 = px.bar(cat_df.sort_values('Revenue', ascending=True), 
                         x='Revenue', y='Category', orientation='h',
                         color='Revenue', color_continuous_scale=['#6366f1', '#ec4899'])
            fig4 = apply_chart_style(fig4, height=380, show_legend=False)
            fig4.update_layout(coloraxis_showscale=False, yaxis_title="", xaxis_title="Revenue ($)")
            st.plotly_chart(fig4, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # TOP PRODUCTS & STORES
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title(f"Top {top_n} Products by Revenue", "🏆")
        
        top_products = filtered_df.groupby('sku_id').agg({
            'revenue': 'sum',
            'quantity_sold': 'sum',
            'transaction_id': 'nunique'
        }).reset_index()
        top_products = top_products.nlargest(top_n, 'revenue')
        top_products.columns = ['SKU', 'Revenue', 'Units', 'Transactions']
        
        fig5 = px.bar(top_products.sort_values('Revenue', ascending=True),
                     x='Revenue', y='SKU', orientation='h',
                     color='Units', color_continuous_scale=['#06b6d4', '#8b5cf6'])
        fig5 = apply_chart_style(fig5, height=400, show_legend=False)
        fig5.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        render_chart_title(f"Top {top_n} Stores by Revenue", "🏪")
        
        top_stores = filtered_df.groupby('store_id').agg({
            'revenue': 'sum',
            'quantity_sold': 'sum',
            'transaction_id': 'nunique'
        }).reset_index()
        top_stores = top_stores.nlargest(top_n, 'revenue')
        top_stores.columns = ['Store', 'Revenue', 'Units', 'Transactions']
        
        fig6 = px.bar(top_stores.sort_values('Revenue', ascending=True),
                     x='Revenue', y='Store', orientation='h',
                     color='Transactions', color_continuous_scale=['#f59e0b', '#ef4444'])
        fig6 = apply_chart_style(fig6, height=400, show_legend=False)
        fig6.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig6, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # REGIONAL ANALYSIS
    # =========================================================================
    if 'region' in filtered_df.columns:
        render_chart_title("Regional Performance Comparison", "🌍")
        
        col1, col2 = st.columns(2)
        
        with col1:
            region_df = filtered_df.groupby('region').agg({
                'revenue': 'sum',
                'quantity_sold': 'sum',
                'transaction_id': 'nunique'
            }).reset_index()
            region_df.columns = ['Region', 'Revenue', 'Units', 'Transactions']
            region_df['AOV'] = region_df['Revenue'] / region_df['Transactions']
            
            fig7 = px.bar(region_df, x='Region', y='Revenue',
                         color='Region', color_discrete_sequence=get_chart_colors())
            fig7 = apply_chart_style(fig7, height=350, show_legend=False)
            st.plotly_chart(fig7, use_container_width=True)
        
        with col2:
            fig8 = px.scatter(region_df, x='Transactions', y='Revenue', size='Units',
                            color='Region', hover_name='Region',
                            color_discrete_sequence=get_chart_colors())
            fig8 = apply_chart_style(fig8, height=350)
            fig8.update_traces(marker=dict(line=dict(width=2, color='white')))
            st.plotly_chart(fig8, use_container_width=True)
    
    # =========================================================================
    # INSIGHTS
    # =========================================================================
    st.markdown("")
    
    # Generate insights
    if 'category' in filtered_df.columns:
        top_cat = filtered_df.groupby('category')['revenue'].sum().idxmax()
        top_cat_pct = (filtered_df.groupby('category')['revenue'].sum().max() / section_revenue * 100)
        render_insight_box("🏆", "Top Category", f"{top_cat} leads with {top_cat_pct:.1f}% of total revenue in the selected filters.", "success")
    
    if 'day_of_week' in filtered_df.columns:
        best_day = filtered_df.groupby('day_of_week')['revenue'].sum().idxmax()
        render_insight_box("📅", "Peak Sales Day", f"{best_day} generates the highest revenue. Consider scheduling major promotions on this day.", "primary")
    
    if 'store_type' in filtered_df.columns:
        top_store_type = filtered_df.groupby('store_type')['revenue'].sum().idxmax()
        render_insight_box("🏪", "Best Store Type", f"{top_store_type} stores are the top performers. Focus expansion efforts here.", "accent")


def render_inventory_analysis(inventory_df, sales_df):
    """Render comprehensive inventory analysis with local filters."""
    render_section_header("📦", "Inventory Health Monitor", "Real-time stock levels, risk assessment, and replenishment insights")
    
    # =========================================================================
    # LOCAL FILTERS FOR THIS SECTION
    # =========================================================================
    st.markdown("#### 🎛️ Inventory Filters")
    
    filter_cols = st.columns([2, 2, 2, 2])
    
    with filter_cols[0]:
        status_filter = st.multiselect(
            "🚦 Stock Status",
            options=['Critical', 'Low', 'Healthy'],
            default=['Critical', 'Low', 'Healthy'],
            key="inv_status_filter"
        )
    
    with filter_cols[1]:
        if 'category' in inventory_df.columns:
            inv_categories = ['All Categories'] + sorted(inventory_df['category'].dropna().unique().tolist())
            inv_category = st.selectbox(
                "🏷️ Category",
                inv_categories,
                key="inv_category_filter"
            )
        else:
            inv_category = 'All Categories'
    
    with filter_cols[2]:
        if 'region' in inventory_df.columns:
            inv_regions = ['All Regions'] + sorted(inventory_df['region'].dropna().unique().tolist())
            inv_region = st.selectbox(
                "🌍 Region",
                inv_regions,
                key="inv_region_filter"
            )
        else:
            inv_region = 'All Regions'
    
    with filter_cols[3]:
        if 'store_type' in inventory_df.columns:
            inv_store_types = ['All Store Types'] + sorted(inventory_df['store_type'].dropna().unique().tolist())
            inv_store_type = st.selectbox(
                "🏪 Store Type",
                inv_store_types,
                key="inv_store_type_filter"
            )
        else:
            inv_store_type = 'All Store Types'
    
    # Second row
    filter_cols2 = st.columns([2, 2, 2, 2])
    
    with filter_cols2[0]:
        if 'days_of_stock' in inventory_df.columns:
            dos_range = st.slider(
                "📆 Days of Stock Range",
                0, 60, (0, 60),
                key="inv_dos_range"
            )
        else:
            dos_range = (0, 60)
    
    with filter_cols2[1]:
        if 'store_id' in inventory_df.columns:
            stores = ['All Stores'] + sorted(inventory_df['store_id'].dropna().unique().tolist())[:20]
            selected_store = st.selectbox(
                "🏬 Specific Store",
                stores,
                key="inv_store_filter"
            )
        else:
            selected_store = 'All Stores'
    
    with filter_cols2[2]:
        sort_by = st.selectbox(
            "📊 Sort By",
            ["Stock Level (Low to High)", "Stock Level (High to Low)", "Days of Stock", "Category"],
            key="inv_sort_by"
        )
    
    with filter_cols2[3]:
        n_items_display = st.slider("🔢 Items to Display", 5, 50, 15, key="inv_n_items")
    
    st.markdown("")
    
    # =========================================================================
    # FILTER DATA
    # =========================================================================
    filtered_inv = inventory_df.copy()
    
    if status_filter:
        filtered_inv = filtered_inv[filtered_inv['stock_status'].isin(status_filter)]
    
    if inv_category != 'All Categories' and 'category' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['category'] == inv_category]
    
    if inv_region != 'All Regions' and 'region' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['region'] == inv_region]
    
    if inv_store_type != 'All Store Types' and 'store_type' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['store_type'] == inv_store_type]
    
    if 'days_of_stock' in filtered_inv.columns:
        filtered_inv = filtered_inv[
            (filtered_inv['days_of_stock'] >= dos_range[0]) &
            (filtered_inv['days_of_stock'] <= dos_range[1])
        ]
    
    if selected_store != 'All Stores' and 'store_id' in filtered_inv.columns:
        filtered_inv = filtered_inv[filtered_inv['store_id'] == selected_store]
    
    if filtered_inv.empty:
        render_empty_state("📦", "No Inventory Data", "Adjust your filters to see inventory items.")
        return
    
    # =========================================================================
    # SECTION KPIs
    # =========================================================================
    total_items = len(filtered_inv)
    critical = len(filtered_inv[filtered_inv['stock_status'] == 'Critical'])
    low = len(filtered_inv[filtered_inv['stock_status'] == 'Low'])
    healthy = len(filtered_inv[filtered_inv['stock_status'] == 'Healthy'])
    
    total_stock_value = (filtered_inv['stock_level'] * filtered_inv.get('unit_price', 50)).sum() if 'stock_level' in filtered_inv.columns else 0
    avg_dos = filtered_inv['days_of_stock'].mean() if 'days_of_stock' in filtered_inv.columns else 0
    
    kpis = [
        {"icon": "📊", "value": f"{total_items:,}", "label": "Total Items", "type": "primary"},
        {"icon": "🔴", "value": f"{critical:,}", "label": "Critical Stock", "type": "danger"},
        {"icon": "🟡", "value": f"{low:,}", "label": "Low Stock", "type": "warning"},
        {"icon": "🟢", "value": f"{healthy:,}", "label": "Healthy Stock", "type": "success"},
        {"icon": "📅", "value": f"{avg_dos:.1f}", "label": "Avg Days of Stock", "type": "accent"},
        {"icon": "💰", "value": f"${total_stock_value/1000000:.1f}M", "label": "Stock Value", "type": "secondary"},
    ]
    render_kpi_row(kpis)
    
    render_divider_subtle()
    
    # =========================================================================
    # STOCK STATUS VISUALIZATION
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title("Stock Status Distribution", "🚦")
        
        status_counts = filtered_inv['stock_status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        
        colors_map = {'Critical': '#ef4444', 'Low': '#f59e0b', 'Healthy': '#10b981'}
        fig = px.pie(status_counts, values='Count', names='Status',
                    color='Status', color_discrete_map=colors_map,
                    hole=0.6)
        fig = apply_chart_style(fig, height=350)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        
        # Add center annotation
        fig.add_annotation(
            text=f"{total_items:,}<br>Items",
            x=0.5, y=0.5,
            font=dict(size=18, color='white', family='Inter'),
            showarrow=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_title("Stock Health by Category", "📊")
        
        if 'category' in filtered_inv.columns:
            cat_status = filtered_inv.groupby(['category', 'stock_status']).size().reset_index(name='count')
            
            fig2 = px.bar(cat_status, x='category', y='count', color='stock_status',
                         color_discrete_map=colors_map, barmode='stack')
            fig2 = apply_chart_style(fig2, height=350)
            fig2.update_layout(xaxis_title="", yaxis_title="Items", legend_title="Status")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            render_empty_state("📊", "No category data", "")
    
    render_divider_subtle()
    
    # =========================================================================
    # DAYS OF STOCK ANALYSIS
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title("Days of Stock Distribution", "📆")
        
        if 'days_of_stock' in filtered_inv.columns:
            fig3 = px.histogram(filtered_inv, x='days_of_stock', nbins=30,
                               color_discrete_sequence=['#6366f1'])
            fig3.add_vline(x=7, line_dash="dash", line_color="#ef4444", 
                          annotation_text="Critical (7 days)")
            fig3.add_vline(x=14, line_dash="dash", line_color="#f59e0b",
                          annotation_text="Warning (14 days)")
            fig3 = apply_chart_style(fig3, height=350)
            fig3.update_layout(xaxis_title="Days of Stock", yaxis_title="Count")
            st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        render_chart_title("Stock Level vs Reorder Point", "📈")
        
        sample_inv = filtered_inv.sample(min(200, len(filtered_inv)))
        fig4 = px.scatter(sample_inv, x='reorder_point', y='stock_level',
                         color='stock_status', color_discrete_map=colors_map,
                         hover_data=['sku_id', 'store_id'])
        fig4.add_trace(go.Scatter(x=[0, sample_inv['reorder_point'].max()],
                                  y=[0, sample_inv['reorder_point'].max()],
                                  mode='lines', name='Reorder Line',
                                  line=dict(dash='dash', color='#71717a')))
        fig4 = apply_chart_style(fig4, height=350)
        fig4.update_layout(xaxis_title="Reorder Point", yaxis_title="Stock Level")
        st.plotly_chart(fig4, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # CRITICAL ITEMS TABLE
    # =========================================================================
    render_chart_title(f"🚨 Top {n_items_display} At-Risk Items", "⚠️")
    
    # Sort data
    if sort_by == "Stock Level (Low to High)":
        display_df = filtered_inv.nsmallest(n_items_display, 'stock_level')
    elif sort_by == "Stock Level (High to Low)":
        display_df = filtered_inv.nlargest(n_items_display, 'stock_level')
    elif sort_by == "Days of Stock" and 'days_of_stock' in filtered_inv.columns:
        display_df = filtered_inv.nsmallest(n_items_display, 'days_of_stock')
    else:
        display_df = filtered_inv.head(n_items_display)
    
    # Select columns to display
    display_cols = ['sku_id', 'store_id', 'stock_level', 'reorder_point', 'stock_status']
    if 'days_of_stock' in display_df.columns:
        display_cols.append('days_of_stock')
    if 'category' in display_df.columns:
        display_cols.append('category')
    if 'region' in display_df.columns:
        display_cols.append('region')
    
    available_cols = [c for c in display_cols if c in display_df.columns]
    st.dataframe(display_df[available_cols], use_container_width=True, hide_index=True, height=400)
    
    # =========================================================================
    # INSIGHTS & RECOMMENDATIONS
    # =========================================================================
    st.markdown("")
    
    critical_pct = (critical / total_items * 100) if total_items > 0 else 0
    low_pct = (low / total_items * 100) if total_items > 0 else 0
    
    if critical_pct > 10:
        render_insight_box("🚨", "Critical Alert", f"{critical_pct:.1f}% of inventory is in critical status. Immediate replenishment needed for {critical} items.", "danger")
    elif critical_pct > 5:
        render_insight_box("⚠️", "Stock Warning", f"{critical_pct:.1f}% of inventory is critical. Review replenishment schedule.", "warning")
    else:
        render_insight_box("✅", "Healthy Inventory", f"Only {critical_pct:.1f}% of items are critical. Inventory health is good.", "success")
    
    if 'category' in filtered_inv.columns:
        worst_cat = filtered_inv[filtered_inv['stock_status'] == 'Critical'].groupby('category').size()
        if len(worst_cat) > 0:
            worst_cat_name = worst_cat.idxmax()
            render_insight_box("📦", "Category Focus", f"{worst_cat_name} has the most critical stock items. Prioritize replenishment for this category.", "warning")


def render_promotions_analysis(promotions_df, sales_df):
    """Render comprehensive promotions analysis with local filters."""
    render_section_header("🎯", "Promotional Performance Hub", "Analyze campaign effectiveness and optimize promotional strategies")
    
    # =========================================================================
    # LOCAL FILTERS FOR THIS SECTION
    # =========================================================================
    st.markdown("#### 🎛️ Promotion Filters")
    
    filter_cols = st.columns([2, 2, 2, 2])
    
    with filter_cols[0]:
        if 'promotion_type' in promotions_df.columns:
            promo_types = ['All Types'] + sorted(promotions_df['promotion_type'].dropna().unique().tolist())
            selected_promo_type = st.selectbox(
                "🏷️ Promotion Type",
                promo_types,
                key="promo_type_filter"
            )
        else:
            selected_promo_type = 'All Types'
    
    with filter_cols[1]:
        if 'category' in promotions_df.columns:
            promo_categories = ['All Categories'] + sorted(promotions_df['category'].dropna().unique().tolist())
            promo_category = st.selectbox(
                "📦 Category",
                promo_categories,
                key="promo_category_filter"
            )
        else:
            promo_category = 'All Categories'
    
    with filter_cols[2]:
        if 'discount_percentage' in promotions_df.columns:
            min_disc = int(promotions_df['discount_percentage'].min())
            max_disc = int(promotions_df['discount_percentage'].max())
            discount_range = st.slider(
                "💸 Discount Range (%)",
                min_disc, max_disc, (min_disc, max_disc),
                key="promo_discount_range"
            )
        else:
            discount_range = (0, 100)
    
    with filter_cols[3]:
        view_mode = st.selectbox(
            "📊 Analysis View",
            ["Overview", "Performance Analysis", "Timeline", "Comparison"],
            key="promo_view_mode"
        )
    
    # Second row
    filter_cols2 = st.columns([2, 2, 2, 2])
    
    with filter_cols2[0]:
        if 'brand' in promotions_df.columns:
            promo_brands = ['All Brands'] + sorted(promotions_df['brand'].dropna().unique().tolist())
            promo_brand = st.selectbox(
                "🏢 Brand",
                promo_brands,
                key="promo_brand_filter"
            )
        else:
            promo_brand = 'All Brands'
    
    with filter_cols2[1]:
        if 'is_active' in promotions_df.columns:
            status_options = ['All', 'Active Only', 'Completed Only']
            promo_status = st.selectbox(
                "🚦 Status",
                status_options,
                key="promo_status_filter"
            )
        else:
            promo_status = 'All'
    
    with filter_cols2[2]:
        if 'duration_days' in promotions_df.columns:
            duration_range = st.slider(
                "📅 Duration (Days)",
                1, 30, (1, 30),
                key="promo_duration_range"
            )
        else:
            duration_range = (1, 30)
    
    with filter_cols2[3]:
        top_n_promos = st.slider("🔝 Top N Promotions", 5, 20, 10, key="promo_top_n")
    
    st.markdown("")
    
    # =========================================================================
    # FILTER DATA
    # =========================================================================
    filtered_promo = promotions_df.copy()
    
    if selected_promo_type != 'All Types' and 'promotion_type' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['promotion_type'] == selected_promo_type]
    
    if promo_category != 'All Categories' and 'category' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['category'] == promo_category]
    
    if 'discount_percentage' in filtered_promo.columns:
        filtered_promo = filtered_promo[
            (filtered_promo['discount_percentage'] >= discount_range[0]) &
            (filtered_promo['discount_percentage'] <= discount_range[1])
        ]
    
    if promo_brand != 'All Brands' and 'brand' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['brand'] == promo_brand]
    
    if promo_status == 'Active Only' and 'is_active' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['is_active'] == True]
    elif promo_status == 'Completed Only' and 'is_active' in filtered_promo.columns:
        filtered_promo = filtered_promo[filtered_promo['is_active'] == False]
    
    if 'duration_days' in filtered_promo.columns:
        filtered_promo = filtered_promo[
            (filtered_promo['duration_days'] >= duration_range[0]) &
            (filtered_promo['duration_days'] <= duration_range[1])
        ]
    
    if filtered_promo.empty:
        render_empty_state("🎯", "No Promotions Found", "Adjust your filters to see promotional campaigns.")
        return
    
    # =========================================================================
    # SECTION KPIs
    # =========================================================================
    total_promos = len(filtered_promo)
    avg_discount = filtered_promo['discount_percentage'].mean() if 'discount_percentage' in filtered_promo.columns else 0
    unique_skus = filtered_promo['sku_id'].nunique() if 'sku_id' in filtered_promo.columns else 0
    total_budget = filtered_promo['budget'].sum() if 'budget' in filtered_promo.columns else 0
    avg_lift = filtered_promo['actual_sales_lift'].mean() if 'actual_sales_lift' in filtered_promo.columns else 0
    avg_roi = filtered_promo['roi'].mean() if 'roi' in filtered_promo.columns else 0
    
    kpis = [
        {"icon": "🎯", "value": f"{total_promos:,}", "label": "Total Promotions", "type": "primary"},
        {"icon": "💸", "value": f"{avg_discount:.1f}%", "label": "Avg Discount", "type": "warning"},
        {"icon": "📦", "value": f"{unique_skus:,}", "label": "SKUs Promoted", "type": "accent"},
        {"icon": "💰", "value": f"${total_budget:,.0f}", "label": "Total Budget", "type": "secondary"},
        {"icon": "📈", "value": f"{avg_lift:.1f}%", "label": "Avg Sales Lift", "type": "success"},
        {"icon": "💹", "value": f"{avg_roi:.1f}%", "label": "Avg ROI", "type": "primary" if avg_roi > 0 else "danger"},
    ]
    render_kpi_row(kpis)
    
    render_divider_subtle()
    
    # =========================================================================
    # VIEW-SPECIFIC CHARTS
    # =========================================================================
    
    if view_mode == "Overview":
        col1, col2 = st.columns(2)
        
        with col1:
            render_chart_title("Promotions by Type", "📊")
            if 'promotion_type' in filtered_promo.columns:
                type_counts = filtered_promo['promotion_type'].value_counts().reset_index()
                type_counts.columns = ['Type', 'Count']
                
                fig = px.bar(type_counts, x='Type', y='Count',
                            color='Type', color_discrete_sequence=get_chart_colors())
                fig = apply_chart_style(fig, height=350, show_legend=False)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_chart_title("Discount Distribution", "💸")
            if 'discount_percentage' in filtered_promo.columns:
                fig2 = px.histogram(filtered_promo, x='discount_percentage', nbins=15,
                                   color_discrete_sequence=['#10b981'])
                fig2 = apply_chart_style(fig2, height=350)
                fig2.update_layout(xaxis_title="Discount %", yaxis_title="Count")
                st.plotly_chart(fig2, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_chart_title("Budget by Category", "💰")
            if 'category' in filtered_promo.columns and 'budget' in filtered_promo.columns:
                cat_budget = filtered_promo.groupby('category')['budget'].sum().reset_index()
                cat_budget.columns = ['Category', 'Budget']
                
                fig3 = px.pie(cat_budget, values='Budget', names='Category',
                             color_discrete_sequence=get_chart_colors(), hole=0.5)
                fig3 = apply_chart_style(fig3, height=350)
                st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            render_chart_title("Promotions by Category", "📦")
            if 'category' in filtered_promo.columns:
                cat_counts = filtered_promo['category'].value_counts().reset_index()
                cat_counts.columns = ['Category', 'Count']
                
                fig4 = px.bar(cat_counts.sort_values('Count', ascending=True),
                             x='Count', y='Category', orientation='h',
                             color='Count', color_continuous_scale=['#6366f1', '#ec4899'])
                fig4 = apply_chart_style(fig4, height=350, show_legend=False)
                fig4.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig4, use_container_width=True)
    
    elif view_mode == "Performance Analysis":
        col1, col2 = st.columns(2)
        
        with col1:
            render_chart_title("Sales Lift by Promotion Type", "📈")
            if 'promotion_type' in filtered_promo.columns and 'actual_sales_lift' in filtered_promo.columns:
                lift_by_type = filtered_promo.groupby('promotion_type')['actual_sales_lift'].mean().reset_index()
                lift_by_type.columns = ['Type', 'Sales Lift']
                
                fig = px.bar(lift_by_type.sort_values('Sales Lift', ascending=True),
                            x='Sales Lift', y='Type', orientation='h',
                            color='Sales Lift', color_continuous_scale=['#ef4444', '#10b981'])
                fig = apply_chart_style(fig, height=350, show_legend=False)
                fig.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_chart_title("ROI by Promotion Type", "💹")
            if 'promotion_type' in filtered_promo.columns and 'roi' in filtered_promo.columns:
                roi_by_type = filtered_promo.groupby('promotion_type')['roi'].mean().reset_index()
                roi_by_type.columns = ['Type', 'ROI']
                
                fig2 = px.bar(roi_by_type.sort_values('ROI', ascending=True),
                             x='ROI', y='Type', orientation='h',
                             color='ROI', color_continuous_scale=['#ef4444', '#10b981'])
                fig2 = apply_chart_style(fig2, height=350, show_legend=False)
                fig2.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig2, use_container_width=True)
        
        render_chart_title("Discount vs Sales Lift Analysis", "🔍")
        if 'discount_percentage' in filtered_promo.columns and 'actual_sales_lift' in filtered_promo.columns:
            fig3 = px.scatter(filtered_promo, x='discount_percentage', y='actual_sales_lift',
                            color='promotion_type' if 'promotion_type' in filtered_promo.columns else None,
                            size='budget' if 'budget' in filtered_promo.columns else None,
                            hover_data=['promotion_id'],
                            color_discrete_sequence=get_chart_colors())
            fig3.add_trace(go.Scatter(x=[0, 70], y=[0, 70], mode='lines',
                                     name='1:1 Line', line=dict(dash='dash', color='#71717a')))
            fig3 = apply_chart_style(fig3, height=400)
            fig3.update_layout(xaxis_title="Discount %", yaxis_title="Sales Lift %")
            st.plotly_chart(fig3, use_container_width=True)
    
    elif view_mode == "Timeline":
        render_chart_title("Promotion Timeline", "📅")
        if 'start_date' in filtered_promo.columns:
            promo_timeline = filtered_promo.groupby(filtered_promo['start_date'].dt.to_period('M').astype(str)).size().reset_index()
            promo_timeline.columns = ['Month', 'Promotions']
            
            fig = px.line(promo_timeline, x='Month', y='Promotions', markers=True,
                         color_discrete_sequence=['#6366f1'])
            fig.update_traces(line=dict(width=3), marker=dict(size=10))
            fig = apply_chart_style(fig, height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        render_chart_title("Budget Allocation Over Time", "💰")
        if 'start_date' in filtered_promo.columns and 'budget' in filtered_promo.columns:
            budget_timeline = filtered_promo.groupby(filtered_promo['start_date'].dt.to_period('M').astype(str))['budget'].sum().reset_index()
            budget_timeline.columns = ['Month', 'Budget']
            
            fig2 = px.area(budget_timeline, x='Month', y='Budget',
                          color_discrete_sequence=['#10b981'])
            fig2.update_traces(fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.3)')
            fig2 = apply_chart_style(fig2, height=350)
            st.plotly_chart(fig2, use_container_width=True)
    
    else:  # Comparison
        render_chart_title("Promotion Type Comparison", "⚖️")
        if 'promotion_type' in filtered_promo.columns:
            fig = px.box(filtered_promo, x='promotion_type', y='discount_percentage',
                        color='promotion_type', color_discrete_sequence=get_chart_colors())
            fig = apply_chart_style(fig, height=400, show_legend=False)
            fig.update_layout(xaxis_title="", yaxis_title="Discount %")
            st.plotly_chart(fig, use_container_width=True)
        
        if 'promotion_type' in filtered_promo.columns and 'actual_sales_lift' in filtered_promo.columns:
            render_chart_title("Sales Lift Distribution by Type", "📊")
            fig2 = px.violin(filtered_promo, x='promotion_type', y='actual_sales_lift',
                           color='promotion_type', color_discrete_sequence=get_chart_colors(),
                           box=True)
            fig2 = apply_chart_style(fig2, height=400, show_legend=False)
            st.plotly_chart(fig2, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # TOP PROMOTIONS TABLE
    # =========================================================================
    render_chart_title(f"Top {top_n_promos} Performing Promotions", "🏆")
    
    if 'actual_sales_lift' in filtered_promo.columns:
        top_promos = filtered_promo.nlargest(top_n_promos, 'actual_sales_lift')
    else:
        top_promos = filtered_promo.head(top_n_promos)
    
    display_cols = ['promotion_id', 'promotion_type', 'discount_percentage']
    if 'actual_sales_lift' in top_promos.columns:
        display_cols.append('actual_sales_lift')
    if 'roi' in top_promos.columns:
        display_cols.append('roi')
    if 'category' in top_promos.columns:
        display_cols.append('category')
    
    available_cols = [c for c in display_cols if c in top_promos.columns]
    st.dataframe(top_promos[available_cols], use_container_width=True, hide_index=True)
    
    # =========================================================================
    # INSIGHTS
    # =========================================================================
    st.markdown("")
    
    if 'promotion_type' in filtered_promo.columns and 'actual_sales_lift' in filtered_promo.columns:
        best_type = filtered_promo.groupby('promotion_type')['actual_sales_lift'].mean().idxmax()
        best_lift = filtered_promo.groupby('promotion_type')['actual_sales_lift'].mean().max()
        render_insight_box("🏆", "Best Promotion Type", f"{best_type} delivers the highest average sales lift of {best_lift:.1f}%.", "success")
    
    if 'roi' in filtered_promo.columns:
        positive_roi_pct = (filtered_promo['roi'] > 0).mean() * 100
        render_insight_box("💹", "ROI Performance", f"{positive_roi_pct:.1f}% of promotions delivered positive ROI.", "primary" if positive_roi_pct > 70 else "warning")

# =============================================================================
# WHAT-IF PROMOTION SIMULATOR
# =============================================================================

def render_promo_simulator(sales_df, inventory_df, promotions_df):
    """Render the comprehensive What-If Promotion Simulator."""
    render_section_header("🧪", "What-If Promotion Simulator", "Simulate promotional scenarios and predict outcomes with AI-powered insights")
    
    # Introduction
    render_insight_box(
        "💡",
        "How to Use",
        "Configure your promotional parameters on the left, then click 'Run Simulation' to see projected outcomes. The simulator uses historical data patterns and elasticity models to forecast results.",
        "primary"
    )
    
    st.markdown("")
    
    # =========================================================================
    # SIMULATOR LAYOUT
    # =========================================================================
    col_params, col_results = st.columns([1, 2])
    
    with col_params:
        st.markdown("### ⚙️ Simulation Parameters")
        st.markdown("")
        
        # Product Selection
        st.markdown("**📦 Product Selection**")
        
        if 'category' in sales_df.columns:
            sim_category = st.selectbox(
                "Category",
                sorted(sales_df['category'].unique()),
                key="sim_category"
            )
        else:
            sim_category = "General"
        
        if 'brand' in sales_df.columns:
            category_brands = sales_df[sales_df['category'] == sim_category]['brand'].unique() if 'category' in sales_df.columns else sales_df['brand'].unique()
            sim_brand = st.selectbox(
                "Brand",
                ['All Brands'] + sorted(category_brands.tolist()),
                key="sim_brand"
            )
        else:
            sim_brand = "All Brands"
        
        if 'sku_id' in sales_df.columns:
            if sim_brand != 'All Brands' and 'brand' in sales_df.columns:
                available_skus = sales_df[(sales_df['category'] == sim_category) & (sales_df['brand'] == sim_brand)]['sku_id'].unique()
            elif 'category' in sales_df.columns:
                available_skus = sales_df[sales_df['category'] == sim_category]['sku_id'].unique()
            else:
                available_skus = sales_df['sku_id'].unique()
            
            sim_sku = st.selectbox(
                "Specific SKU (Optional)",
                ['All SKUs in Category'] + sorted(available_skus.tolist())[:50],
                key="sim_sku"
            )
        else:
            sim_sku = "All SKUs in Category"
        
        st.markdown("")
        st.markdown("**💸 Discount Settings**")
        
        # Discount slider
        sim_discount = st.slider(
            "Discount Percentage",
            min_value=5,
            max_value=70,
            value=20,
            step=5,
            key="sim_discount",
            help="Higher discounts typically drive more volume but reduce margin"
        )
        
        # Visual discount indicator
        if sim_discount <= 15:
            discount_label = "Conservative"
            discount_color = "#10b981"
        elif sim_discount <= 30:
            discount_label = "Moderate"
            discount_color = "#f59e0b"
        elif sim_discount <= 50:
            discount_label = "Aggressive"
            discount_color = "#f97316"
        else:
            discount_label = "Deep Discount"
            discount_color = "#ef4444"
        
        st.markdown(f'<div style="text-align: center; padding: 8px; background: {discount_color}20; border: 1px solid {discount_color}40; border-radius: 8px; margin-bottom: 16px;"><span style="color: {discount_color}; font-weight: 600;">{sim_discount}% - {discount_label}</span></div>', unsafe_allow_html=True)
        
        st.markdown("")
        st.markdown("**📅 Campaign Duration**")
        
        # Duration
        sim_duration = st.slider(
            "Duration (days)",
            min_value=1,
            max_value=30,
            value=7,
            key="sim_duration"
        )
        
        # Duration insights
        if sim_duration <= 3:
            duration_tip = "Flash sale - high urgency, limited reach"
        elif sim_duration <= 7:
            duration_tip = "Standard promotion - good balance"
        elif sim_duration <= 14:
            duration_tip = "Extended campaign - wider reach"
        else:
            duration_tip = "Long-term promotion - may reduce urgency"
        
        st.caption(f"💡 {duration_tip}")
        
        st.markdown("")
        st.markdown("**🎯 Promotion Type**")
        
        # Promotion type
        sim_promo_type = st.selectbox(
            "Type",
            ["Percentage Off", "BOGO", "Bundle Deal", "Flash Sale", "Clearance", "Member Exclusive"],
            key="sim_promo_type"
        )
        
        st.markdown("")
        st.markdown("**🏪 Target Scope**")
        
        # Store selection
        if 'region' in sales_df.columns:
            regions = ['All Regions'] + sorted(sales_df['region'].unique().tolist())
            sim_region = st.selectbox(
                "Target Region",
                regions,
                key="sim_region"
            )
        else:
            sim_region = "All Regions"
        
        if 'store_type' in sales_df.columns:
            store_types = ['All Store Types'] + sorted(sales_df['store_type'].unique().tolist())
            sim_store_type = st.selectbox(
                "Store Type",
                store_types,
                key="sim_store_type"
            )
        else:
            sim_store_type = "All Store Types"
        
        st.markdown("")
        st.markdown("**👥 Target Audience**")
        
        sim_audience = st.multiselect(
            "Customer Segments",
            ["All Customers", "Premium Members", "New Customers", "Lapsed Customers", "High-Value Customers"],
            default=["All Customers"],
            key="sim_audience"
        )
        
        st.markdown("")
        st.markdown("**💰 Budget Constraints**")
        
        sim_budget = st.number_input(
            "Maximum Budget ($)",
            min_value=1000,
            max_value=1000000,
            value=50000,
            step=5000,
            key="sim_budget"
        )
        
        st.markdown("")
        
        # Run simulation button
        run_simulation = st.button("🚀 Run Simulation", type="primary", use_container_width=True, key="run_sim_btn")
        
        # Reset button
        if st.button("🔄 Reset Parameters", use_container_width=True, key="reset_sim_btn"):
            st.session_state['simulation_run'] = False
            st.rerun()
    
    # =========================================================================
    # RESULTS PANEL
    # =========================================================================
    with col_results:
        if run_simulation or st.session_state.get('simulation_run', False):
            st.session_state['simulation_run'] = True
            
            # Progress indicator
            with st.spinner("🔄 Running simulation..."):
                import time
                time.sleep(0.5)  # Brief delay for UX
            
            st.markdown("### 📊 Simulation Results")
            st.markdown("")
            
            # =====================================================================
            # CALCULATE SIMULATION RESULTS
            # =====================================================================
            
            # Filter base data for simulation
            sim_sales = sales_df.copy()
            if 'category' in sim_sales.columns and sim_category:
                sim_sales = sim_sales[sim_sales['category'] == sim_category]
            if sim_brand != 'All Brands' and 'brand' in sim_sales.columns:
                sim_sales = sim_sales[sim_sales['brand'] == sim_brand]
            if sim_sku != 'All SKUs in Category' and 'sku_id' in sim_sales.columns:
                sim_sales = sim_sales[sim_sales['sku_id'] == sim_sku]
            if sim_region != 'All Regions' and 'region' in sim_sales.columns:
                sim_sales = sim_sales[sim_sales['region'] == sim_region]
            if sim_store_type != 'All Store Types' and 'store_type' in sim_sales.columns:
                sim_sales = sim_sales[sim_sales['store_type'] == sim_store_type]
            
            # Calculate base metrics
            if len(sim_sales) > 0:
                total_days = (sim_sales['transaction_date'].max() - sim_sales['transaction_date'].min()).days
                total_days = max(total_days, 1)
                
                base_daily_revenue = sim_sales['revenue'].sum() / total_days
                base_daily_units = sim_sales['quantity_sold'].sum() / total_days
                base_avg_price = sim_sales['unit_price'].mean()
            else:
                base_daily_revenue = 10000
                base_daily_units = 100
                base_avg_price = 100
            
            # Price elasticity model
            # Elasticity varies by category
            category_elasticity = {
                'Electronics': -1.8,
                'Clothing': -2.2,
                'Food & Beverage': -1.2,
                'Home & Garden': -1.5,
                'Health & Beauty': -1.6,
                'Sports & Outdoors': -1.7,
                'Toys & Games': -2.0,
                'Automotive': -1.3
            }
            base_elasticity = category_elasticity.get(sim_category, -1.5)
            
            # Adjust elasticity for promotion type
            type_multiplier = {
                "Percentage Off": 1.0,
                "BOGO": 1.4,
                "Bundle Deal": 1.2,
                "Flash Sale": 1.5,
                "Clearance": 1.1,
                "Member Exclusive": 0.9
            }
            adjusted_elasticity = base_elasticity * type_multiplier.get(sim_promo_type, 1.0)
            
            # Calculate lift
            price_change_pct = -sim_discount / 100
            volume_lift = abs(adjusted_elasticity) * sim_discount / 100
            
            # Duration effects
            if sim_duration <= 3:
                duration_factor = 1.3  # Urgency boost
            elif sim_duration <= 7:
                duration_factor = 1.0
            elif sim_duration <= 14:
                duration_factor = 0.9  # Some fatigue
            else:
                duration_factor = 0.8  # Promotion fatigue
            
            # Audience factor
            audience_factor = 1.0
            if "Premium Members" in sim_audience:
                audience_factor *= 1.15
            if "High-Value Customers" in sim_audience:
                audience_factor *= 1.1
            if len(sim_audience) > 2:
                audience_factor *= 1.05
            
            # Final calculations
            final_lift = volume_lift * duration_factor * audience_factor
            
            # Projected metrics
            projected_daily_units = base_daily_units * (1 + final_lift)
            discounted_price = base_avg_price * (1 - sim_discount / 100)
            projected_daily_revenue = projected_daily_units * discounted_price
            
            # Campaign totals
            projected_total_units = projected_daily_units * sim_duration
            projected_total_revenue = projected_daily_revenue * sim_duration
            baseline_revenue = base_daily_revenue * sim_duration
            
            # Incremental metrics
            incremental_units = projected_total_units - (base_daily_units * sim_duration)
            incremental_revenue = projected_total_revenue - baseline_revenue
            
            # Cost and ROI
            discount_cost = (base_avg_price * sim_discount / 100) * projected_total_units
            estimated_cogs = projected_total_revenue * 0.6  # Assume 40% margin
            gross_profit = projected_total_revenue - estimated_cogs
            net_impact = gross_profit - discount_cost
            
            roi = ((projected_total_revenue - baseline_revenue) / sim_budget * 100) if sim_budget > 0 else 0
            
            # Confidence score
            confidence = min(95, 70 + (len(sim_sales) / 1000) * 5)
            
            # =====================================================================
            # DISPLAY RESULTS
            # =====================================================================
            
            # Primary KPIs
            result_kpis = [
                {"icon": "📈", "value": f"+{final_lift*100:.1f}%", "label": "Sales Lift", "type": "success" if final_lift > 0.1 else "warning"},
                {"icon": "📦", "value": f"{projected_total_units:,.0f}", "label": "Projected Units", "type": "primary"},
                {"icon": "💰", "value": f"${projected_total_revenue:,.0f}", "label": "Projected Revenue", "type": "accent"},
                {"icon": "📊", "value": f"${incremental_revenue:+,.0f}", "label": "Incremental Rev", "type": "success" if incremental_revenue > 0 else "danger"},
            ]
            render_kpi_row(result_kpis)
            
            st.markdown("")
            
            # Secondary metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                render_status_card("ROI", f"{roi:+.1f}%", "success" if roi > 0 else "danger")
            with col2:
                render_status_card("Discount Cost", f"${discount_cost:,.0f}", "warning")
            with col3:
                render_status_card("Net Impact", f"${net_impact:+,.0f}", "success" if net_impact > 0 else "danger")
            with col4:
                render_status_card("Confidence", f"{confidence:.0f}%", "success" if confidence > 80 else "warning")
            
            render_divider_subtle()
            
            # =====================================================================
            # PROJECTION CHARTS
            # =====================================================================
            
            col1, col2 = st.columns(2)
            
            with col1:
                render_chart_title("Revenue Projection", "📈")
                
                days = list(range(1, sim_duration + 1))
                baseline_cumulative = [baseline_revenue / sim_duration * d for d in days]
                projected_cumulative = [projected_total_revenue / sim_duration * d for d in days]
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=days, y=baseline_cumulative, name='Baseline',
                    line=dict(color='#71717a', dash='dash', width=2),
                    fill='tozeroy', fillcolor='rgba(113, 113, 122, 0.1)'
                ))
                fig.add_trace(go.Scatter(
                    x=days, y=projected_cumulative, name='With Promotion',
                    line=dict(color='#6366f1', width=3),
                    fill='tozeroy', fillcolor='rgba(99, 102, 241, 0.2)'
                ))
                fig = apply_chart_style(fig, height=320)
                fig.update_layout(xaxis_title="Campaign Day", yaxis_title="Cumulative Revenue ($)")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                render_chart_title("Units Projection", "📦")
                
                baseline_units_cum = [base_daily_units * d for d in days]
                projected_units_cum = [projected_daily_units * d for d in days]
                
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=days, y=baseline_units_cum, name='Baseline',
                    line=dict(color='#71717a', dash='dash', width=2),
                    fill='tozeroy', fillcolor='rgba(113, 113, 122, 0.1)'
                ))
                fig2.add_trace(go.Scatter(
                    x=days, y=projected_units_cum, name='With Promotion',
                    line=dict(color='#10b981', width=3),
                    fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.2)'
                ))
                fig2 = apply_chart_style(fig2, height=320)
                fig2.update_layout(xaxis_title="Campaign Day", yaxis_title="Cumulative Units")
                st.plotly_chart(fig2, use_container_width=True)
            
            # =====================================================================
            # SENSITIVITY ANALYSIS
            # =====================================================================
            
            render_chart_title("Sensitivity Analysis: Discount vs Revenue Impact", "🔍")
            
            discount_range = list(range(5, 75, 5))
            revenue_impacts = []
            roi_impacts = []
            
            for disc in discount_range:
                temp_lift = abs(adjusted_elasticity) * disc / 100 * duration_factor * audience_factor
                temp_units = base_daily_units * (1 + temp_lift) * sim_duration
                temp_price = base_avg_price * (1 - disc / 100)
                temp_revenue = temp_units * temp_price
                temp_impact = temp_revenue - baseline_revenue
                revenue_impacts.append(temp_impact)
                roi_impacts.append((temp_impact / sim_budget * 100) if sim_budget > 0 else 0)
            
            sens_df = pd.DataFrame({
                'Discount': discount_range,
                'Revenue Impact': revenue_impacts,
                'ROI': roi_impacts
            })
            
            fig3 = make_subplots(specs=[[{"secondary_y": True}]])
            fig3.add_trace(
                go.Bar(x=sens_df['Discount'], y=sens_df['Revenue Impact'], name='Revenue Impact',
                      marker_color=['#10b981' if x > 0 else '#ef4444' for x in sens_df['Revenue Impact']]),
                secondary_y=False
            )
            fig3.add_trace(
                go.Scatter(x=sens_df['Discount'], y=sens_df['ROI'], name='ROI %',
                          line=dict(color='#f59e0b', width=3), mode='lines+markers'),
                secondary_y=True
            )
            fig3.add_vline(x=sim_discount, line_dash="dash", line_color="#6366f1",
                          annotation_text=f"Current: {sim_discount}%")
            fig3 = apply_chart_style(fig3, height=350)
            fig3.update_layout(
                xaxis_title="Discount %",
                yaxis_title="Revenue Impact ($)",
                yaxis2_title="ROI %"
            )
            st.plotly_chart(fig3, use_container_width=True)
            
            # =====================================================================
            # AI RECOMMENDATIONS
            # =====================================================================
            
            recommendations = []
            
            # Discount recommendation
            optimal_discount_idx = sens_df['Revenue Impact'].idxmax()
            optimal_discount = sens_df.loc[optimal_discount_idx, 'Discount']
            if abs(optimal_discount - sim_discount) > 5:
                recommendations.append({
                    "icon": "🎯",
                    "text": f"Consider adjusting discount to {optimal_discount}% for maximum revenue impact (${sens_df.loc[optimal_discount_idx, 'Revenue Impact']:+,.0f})"
                })
            
            # Duration recommendation
            if sim_duration < 5 and sim_discount > 30:
                recommendations.append({
                    "icon": "⏰",
                    "text": f"For {sim_discount}% discount, consider extending to 7 days for better reach and ROI"
                })
            elif sim_duration > 14:
                recommendations.append({
                    "icon": "📅",
                    "text": "Long campaigns may reduce urgency. Consider splitting into multiple shorter promotions"
                })
            
            # Promo type recommendation
            if sim_promo_type == "Percentage Off" and sim_discount >= 40:
                recommendations.append({
                    "icon": "💡",
                    "text": "At high discount levels, BOGO or Bundle deals often perform better than straight percentage off"
                })
            
            # ROI warning
            if roi < 0:
                recommendations.append({
                    "icon": "⚠️",
                    "text": f"Current configuration shows negative ROI ({roi:.1f}%). Consider reducing discount or budget"
                })
            elif roi > 100:
                recommendations.append({
                    "icon": "✅",
                    "text": f"Excellent projected ROI of {roi:.1f}%! This promotion looks very promising"
                })
            
            # Category-specific
            if sim_category in ['Food & Beverage', 'Health & Beauty']:
                recommendations.append({
                    "icon": "📦",
                    "text": f"{sim_category} has lower price elasticity. Consider focusing on volume-based promotions"
                })
            
            # Inventory check
            if 'category' in inventory_df.columns:
                cat_inventory = inventory_df[inventory_df['category'] == sim_category] if 'category' in inventory_df.columns else inventory_df
                critical_items = len(cat_inventory[cat_inventory['stock_status'] == 'Critical'])
                if critical_items > 10:
                    recommendations.append({
                        "icon": "🚨",
                        "text": f"Warning: {critical_items} items in {sim_category} have critical stock levels. Ensure inventory before promotion"
                    })
            
            # Add general recommendation
            recommendations.append({
                "icon": "📊",
                "text": f"Based on {len(sim_sales):,} historical transactions, confidence level is {confidence:.0f}%"
            })
            
            render_ai_recommendations(recommendations)
            
            # =====================================================================
            # EXPORT OPTION
            # =====================================================================
            
            st.markdown("")
            
            with st.expander("📋 Detailed Simulation Report"):
                st.markdown("### Simulation Summary")
                
                summary_data = {
                    "Parameter": [
                        "Category", "Brand", "Discount", "Duration", "Promotion Type",
                        "Target Region", "Store Type", "Budget"
                    ],
                    "Value": [
                        sim_category, sim_brand, f"{sim_discount}%", f"{sim_duration} days", sim_promo_type,
                        sim_region, sim_store_type, f"${sim_budget:,}"
                    ]
                }
                st.table(pd.DataFrame(summary_data))
                
                st.markdown("### Projected Outcomes")
                
                outcomes_data = {
                    "Metric": [
                        "Baseline Revenue", "Projected Revenue", "Incremental Revenue",
                        "Baseline Units", "Projected Units", "Incremental Units",
                        "Sales Lift", "ROI", "Discount Cost", "Net Impact"
                    ],
                    "Value": [
                        f"${baseline_revenue:,.0f}", f"${projected_total_revenue:,.0f}", f"${incremental_revenue:+,.0f}",
                        f"{base_daily_units * sim_duration:,.0f}", f"{projected_total_units:,.0f}", f"{incremental_units:+,.0f}",
                        f"+{final_lift*100:.1f}%", f"{roi:+.1f}%", f"${discount_cost:,.0f}", f"${net_impact:+,.0f}"
                    ]
                }
                st.table(pd.DataFrame(outcomes_data))
        
        else:
            # Placeholder when simulation hasn't run
            st.markdown("### 📊 Simulation Results")
            st.markdown("")
            
            render_empty_state(
                "🎯",
                "Ready to Simulate",
                "Configure your promotion parameters on the left and click 'Run Simulation' to see projected outcomes."
            )
            
            # Quick tips
            st.markdown("")
            st.markdown("#### 💡 Quick Tips")
            
            tips = [
                {"icon": "📈", "text": "Higher discounts drive more volume but may reduce overall profit margin"},
                {"icon": "⏰", "text": "Flash sales (1-3 days) create urgency; longer campaigns reach more customers"},
                {"icon": "🎯", "text": "BOGO and Bundle deals often outperform simple percentage discounts"},
                {"icon": "📊", "text": "Use sensitivity analysis to find the optimal discount level"},
            ]
            render_ai_recommendations(tips)


def render_store_performance(sales_df, inventory_df):
    """Render comprehensive store performance analysis."""
    render_section_header("🏪", "Store Performance Analysis", "Compare and benchmark store performance across regions")
    
    # =========================================================================
    # LOCAL FILTERS
    # =========================================================================
    st.markdown("#### 🎛️ Store Filters")
    
    filter_cols = st.columns([2, 2, 2, 2])
    
    with filter_cols[0]:
        metric_type = st.selectbox(
            "📊 Performance Metric",
            ["Revenue", "Units Sold", "Transactions", "Avg Order Value", "Revenue per Sqft"],
            key="store_metric"
        )
    
    with filter_cols[1]:
        if 'region' in sales_df.columns:
            regions = ['All Regions'] + sorted(sales_df['region'].unique().tolist())
            store_region = st.selectbox(
                "🌍 Region",
                regions,
                key="store_region_filter"
            )
        else:
            store_region = 'All Regions'
    
    with filter_cols[2]:
        if 'store_type' in sales_df.columns:
            store_types = ['All Types'] + sorted(sales_df['store_type'].unique().tolist())
            store_type_filter = st.selectbox(
                "🏬 Store Type",
                store_types,
                key="store_type_filter_perf"
            )
        else:
            store_type_filter = 'All Types'
    
    with filter_cols[3]:
        if 'month' in sales_df.columns:
            months = ['All Time'] + sorted(sales_df['month'].unique().tolist())
            store_time_period = st.selectbox(
                "📅 Time Period",
                months,
                key="store_time_period"
            )
        else:
            store_time_period = 'All Time'
    
    filter_cols2 = st.columns([2, 2, 2, 2])
    
    with filter_cols2[0]:
        top_n_stores = st.slider("🔝 Top N Stores", 5, 25, 10, key="store_top_n")
    
    with filter_cols2[1]:
        comparison_mode = st.selectbox(
            "📊 Comparison Mode",
            ["Absolute Values", "Per Transaction", "Growth Rate"],
            key="store_comparison_mode"
        )
    
    with filter_cols2[2]:
        if 'category' in sales_df.columns:
            store_category = st.selectbox(
                "🏷️ Category Focus",
                ['All Categories'] + sorted(sales_df['category'].unique().tolist()),
                key="store_category_filter"
            )
        else:
            store_category = 'All Categories'
    
    st.markdown("")
    
    # =========================================================================
    # FILTER DATA
    # =========================================================================
    filtered_sales = sales_df.copy()
    
    if store_region != 'All Regions' and 'region' in filtered_sales.columns:
        filtered_sales = filtered_sales[filtered_sales['region'] == store_region]
    
    if store_type_filter != 'All Types' and 'store_type' in filtered_sales.columns:
        filtered_sales = filtered_sales[filtered_sales['store_type'] == store_type_filter]
    
    if store_time_period != 'All Time' and 'month' in filtered_sales.columns:
        filtered_sales = filtered_sales[filtered_sales['month'] == store_time_period]
    
    if store_category != 'All Categories' and 'category' in filtered_sales.columns:
        filtered_sales = filtered_sales[filtered_sales['category'] == store_category]
    
    if filtered_sales.empty:
        render_empty_state("🏪", "No Store Data", "Adjust filters to see store performance.")
        return
    
    # =========================================================================
    # CALCULATE STORE METRICS
    # =========================================================================
    store_metrics = filtered_sales.groupby('store_id').agg({
        'revenue': 'sum',
        'quantity_sold': 'sum',
        'transaction_id': 'nunique',
        'unit_price': 'mean'
    }).reset_index()
    store_metrics.columns = ['Store', 'Revenue', 'Units', 'Transactions', 'Avg Price']
    store_metrics['AOV'] = store_metrics['Revenue'] / store_metrics['Transactions'].replace(0, 1)
    store_metrics['Units per Transaction'] = store_metrics['Units'] / store_metrics['Transactions'].replace(0, 1)
    
    # Add store attributes
    if 'region' in sales_df.columns:
        store_regions = sales_df.groupby('store_id')['region'].first()
        store_metrics['Region'] = store_metrics['Store'].map(store_regions)
    
    if 'store_type' in sales_df.columns:
        store_types_map = sales_df.groupby('store_id')['store_type'].first()
        store_metrics['Type'] = store_metrics['Store'].map(store_types_map)
    
    # Select metric for ranking
    metric_map = {
        "Revenue": "Revenue",
        "Units Sold": "Units",
        "Transactions": "Transactions",
        "Avg Order Value": "AOV",
        "Revenue per Sqft": "Revenue"  # Simplified
    }
    selected_metric = metric_map[metric_type]
    
    # =========================================================================
    # SECTION KPIs
    # =========================================================================
    total_stores = store_metrics['Store'].nunique()
    total_revenue = store_metrics['Revenue'].sum()
    avg_store_revenue = store_metrics['Revenue'].mean()
    top_store_revenue = store_metrics['Revenue'].max()
    avg_aov = store_metrics['AOV'].mean()
    
    kpis = [
        {"icon": "🏪", "value": f"{total_stores}", "label": "Total Stores", "type": "primary"},
        {"icon": "💰", "value": f"${total_revenue:,.0f}", "label": "Total Revenue", "type": "success"},
        {"icon": "📊", "value": f"${avg_store_revenue:,.0f}", "label": "Avg Store Revenue", "type": "accent"},
        {"icon": "🏆", "value": f"${top_store_revenue:,.0f}", "label": "Top Store Revenue", "type": "secondary"},
        {"icon": "💵", "value": f"${avg_aov:.2f}", "label": "Avg AOV", "type": "primary"},
    ]
    render_kpi_row(kpis)
    
    render_divider_subtle()
    
    # =========================================================================
    # STORE RANKING CHART
    # =========================================================================
    col1, col2 = st.columns(2)
    
    with col1:
        render_chart_title(f"Top {top_n_stores} Stores by {metric_type}", "🏆")
        
        top_stores = store_metrics.nlargest(top_n_stores, selected_metric)
        
        fig = px.bar(
            top_stores.sort_values(selected_metric, ascending=True),
            x=selected_metric,
            y='Store',
            orientation='h',
            color=selected_metric,
            color_continuous_scale=['#6366f1', '#ec4899'],
            hover_data=['Transactions', 'AOV'] if 'Transactions' in top_stores.columns else None
        )
        fig = apply_chart_style(fig, height=400, show_legend=False)
        fig.update_layout(coloraxis_showscale=False, yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        render_chart_title("Store Performance Distribution", "📊")
        
        fig2 = px.scatter(
            store_metrics,
            x='Transactions',
            y='Revenue',
            size='Units',
            color='AOV',
            hover_name='Store',
            color_continuous_scale=['#f59e0b', '#10b981']
        )
        fig2 = apply_chart_style(fig2, height=400)
        fig2.update_traces(marker=dict(line=dict(width=1, color='white')))
        st.plotly_chart(fig2, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # REGIONAL ANALYSIS
    # =========================================================================
    if 'Region' in store_metrics.columns:
        render_chart_title("Performance by Region", "🌍")
        
        col1, col2 = st.columns(2)
        
        with col1:
            region_perf = store_metrics.groupby('Region').agg({
                'Revenue': 'sum',
                'Units': 'sum',
                'Transactions': 'sum',
                'Store': 'count'
            }).reset_index()
            region_perf.columns = ['Region', 'Revenue', 'Units', 'Transactions', 'Store Count']
            region_perf['Revenue per Store'] = region_perf['Revenue'] / region_perf['Store Count']
            
            fig3 = px.bar(region_perf, x='Region', y='Revenue',
                         color='Region', color_discrete_sequence=get_chart_colors())
            fig3 = apply_chart_style(fig3, height=350, show_legend=False)
            fig3.update_layout(xaxis_title="")
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            fig4 = px.pie(region_perf, values='Revenue', names='Region',
                         color_discrete_sequence=get_chart_colors(), hole=0.5)
            fig4 = apply_chart_style(fig4, height=350)
            st.plotly_chart(fig4, use_container_width=True)
    
    # =========================================================================
    # STORE TYPE ANALYSIS
    # =========================================================================
    if 'Type' in store_metrics.columns:
        render_chart_title("Performance by Store Type", "🏬")
        
        col1, col2 = st.columns(2)
        
        with col1:
            type_perf = store_metrics.groupby('Type').agg({
                'Revenue': 'mean',
                'Units': 'mean',
                'Transactions': 'mean',
                'AOV': 'mean'
            }).reset_index()
            type_perf.columns = ['Type', 'Avg Revenue', 'Avg Units', 'Avg Transactions', 'Avg AOV']
            
            fig5 = px.bar(type_perf, x='Type', y='Avg Revenue',
                         color='Avg AOV', color_continuous_scale=['#6366f1', '#10b981'])
            fig5 = apply_chart_style(fig5, height=350, show_legend=False)
            fig5.update_layout(coloraxis_showscale=False)
            st.plotly_chart(fig5, use_container_width=True)
        
        with col2:
            fig6 = px.scatter(type_perf, x='Avg Transactions', y='Avg Revenue',
                            size='Avg Units', color='Type',
                            color_discrete_sequence=get_chart_colors())
            fig6 = apply_chart_style(fig6, height=350)
            st.plotly_chart(fig6, use_container_width=True)
    
    render_divider_subtle()
    
    # =========================================================================
    # STORE COMPARISON TABLE
    # =========================================================================
    render_chart_title("Store Performance Details", "📋")
    
    display_cols = ['Store', 'Revenue', 'Units', 'Transactions', 'AOV']
    if 'Region' in store_metrics.columns:
        display_cols.append('Region')
    if 'Type' in store_metrics.columns:
        display_cols.append('Type')
    
    display_df = store_metrics[display_cols].nlargest(top_n_stores, 'Revenue').copy()
    display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"${x:,.0f}")
    display_df['Units'] = display_df['Units'].apply(lambda x: f"{x:,}")
    display_df['Transactions'] = display_df['Transactions'].apply(lambda x: f"{x:,}")
    display_df['AOV'] = display_df['AOV'].apply(lambda x: f"${x:.2f}")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # =========================================================================
    # INSIGHTS
    # =========================================================================
    st.markdown("")
    
    top_store = store_metrics.loc[store_metrics['Revenue'].idxmax()]
    bottom_store = store_metrics.loc[store_metrics['Revenue'].idxmin()]
    
    render_insight_box("🏆", "Top Performer", f"{top_store['Store']} leads with ${top_store['Revenue']:,.0f} in revenue and {top_store['Transactions']:,.0f} transactions.", "success")
    
    revenue_gap = top_store['Revenue'] - bottom_store['Revenue']
    render_insight_box("📊", "Performance Gap", f"Revenue gap between top and bottom performers is ${revenue_gap:,.0f}. Consider best practice sharing.", "warning")
    
    if 'Region' in store_metrics.columns:
        best_region = store_metrics.groupby('Region')['Revenue'].sum().idxmax()
        render_insight_box("🌍", "Regional Leader", f"{best_region} region generates the highest total revenue. Consider expansion opportunities.", "primary")


def render_time_analysis(sales_df):
    """Render comprehensive time-based analysis."""
    render_section_header("⏰", "Time-Based Analytics", "Discover temporal patterns, trends, and seasonality")
    
    # =========================================================================
    # LOCAL FILTERS
    # =========================================================================
    st.markdown("#### 🎛️ Time Analysis Filters")
    
    filter_cols = st.columns([2, 2, 2, 2])
    
    with filter_cols[0]:
        analysis_type = st.selectbox(
            "📊 Analysis Type",
            ["Day of Week", "Hourly Pattern", "Monthly Trend", "Quarterly Comparison", "Year over Year", "Seasonality"],
            key="time_analysis_type"
        )
    
    with filter_cols[1]:
        if 'category' in sales_df.columns:
            time_category = st.selectbox(
                "🏷️ Category",
                ['All Categories'] + sorted(sales_df['category'].unique().tolist()),
                key="time_category"
            )
        else:
            time_category = 'All Categories'
    
    with filter_cols[2]:
        if 'region' in sales_df.columns:
            time_region = st.selectbox(
                "🌍 Region",
                ['All Regions'] + sorted(sales_df['region'].unique().tolist()),
                key="time_region"
            )
        else:
            time_region = 'All Regions'
    
    with filter_cols[3]:
        time_metric = st.selectbox(
            "📈 Metric",
            ["Revenue", "Units Sold", "Transactions", "Avg Order Value"],
            key="time_metric"
        )
    
    st.markdown("")
    
    # =========================================================================
    # FILTER DATA
    # =========================================================================
    filtered_df = sales_df.copy()
    
    if time_category != 'All Categories' and 'category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['category'] == time_category]
    
    if time_region != 'All Regions' and 'region' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['region'] == time_region]
    
    if filtered_df.empty:
        render_empty_state("⏰", "No Data for Analysis", "Adjust filters to see time patterns.")
        return
    
    # Metric mapping
    metric_col_map = {
        "Revenue": "revenue",
        "Units Sold": "quantity_sold",
        "Transactions": "transaction_id",
        "Avg Order Value": "revenue"
    }
    metric_col = metric_col_map[time_metric]
    
    # =========================================================================
    # DAY OF WEEK ANALYSIS
    # =========================================================================
    if analysis_type == "Day of Week":
        render_chart_title("Sales by Day of Week", "📅")
        
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        if time_metric == "Transactions":
            dow_data = filtered_df.groupby('day_of_week')[metric_col].nunique().reset_index()
        elif time_metric == "Avg Order Value":
            dow_data = filtered_df.groupby('day_of_week').apply(
                lambda x: x['revenue'].sum() / x['transaction_id'].nunique()
            ).reset_index()
            dow_data.columns = ['day_of_week', 'value']
        else:
            dow_data = filtered_df.groupby('day_of_week')[metric_col].sum().reset_index()
        
        dow_data.columns = ['Day', 'Value'] if len(dow_data.columns) == 2 else ['Day', 'Value']
        dow_data['Day'] = pd.Categorical(dow_data['Day'], categories=day_order, ordered=True)
        dow_data = dow_data.sort_values('Day')
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(dow_data, x='Day', y='Value',
                        color='Value', color_continuous_scale=['#6366f1', '#ec4899'])
            fig = apply_chart_style(fig, height=380, show_legend=False)
            fig.update_layout(coloraxis_showscale=False, xaxis_title="", yaxis_title=time_metric)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Radar chart
            fig2 = go.Figure()
            fig2.add_trace(go.Scatterpolar(
                r=dow_data['Value'].tolist() + [dow_data['Value'].iloc[0]],
                theta=dow_data['Day'].tolist() + [dow_data['Day'].iloc[0]],
                fill='toself',
                fillcolor='rgba(99, 102, 241, 0.3)',
                line=dict(color='#6366f1', width=3),
                name=time_metric
            ))
            fig2.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, gridcolor='rgba(255,255,255,0.1)'),
                    angularaxis=dict(gridcolor='rgba(255,255,255,0.1)')
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a1a1aa'),
                height=380,
                showlegend=False
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Insights
        best_day = dow_data.loc[dow_data['Value'].idxmax(), 'Day']
        worst_day = dow_data.loc[dow_data['Value'].idxmin(), 'Day']
        weekend_avg = dow_data[dow_data['Day'].isin(['Friday', 'Saturday', 'Sunday'])]['Value'].mean()
        weekday_avg = dow_data[~dow_data['Day'].isin(['Friday', 'Saturday', 'Sunday'])]['Value'].mean()
        
        render_insight_box("🏆", "Peak Day", f"{best_day} generates the highest {time_metric.lower()}. Schedule key promotions and ensure adequate staffing.", "success")
        render_insight_box("📉", "Opportunity Day", f"{worst_day} shows lowest performance. Consider targeted promotions to boost traffic.", "warning")
        
        weekend_diff = ((weekend_avg - weekday_avg) / weekday_avg * 100) if weekday_avg > 0 else 0
        if weekend_diff > 0:
            render_insight_box("📊", "Weekend Effect", f"Weekend {time_metric.lower()} is {weekend_diff:.1f}% higher than weekdays.", "primary")
        else:
            render_insight_box("📊", "Weekday Strength", f"Weekday {time_metric.lower()} is {abs(weekend_diff):.1f}% higher than weekends.", "primary")
    
    # =========================================================================
    # HOURLY PATTERN
    # =========================================================================
    elif analysis_type == "Hourly Pattern":
        render_chart_title("Hourly Sales Pattern", "🕐")
        
        if 'hour' in filtered_df.columns:
            if time_metric == "Transactions":
                hourly_data = filtered_df.groupby('hour')[metric_col].nunique().reset_index()
            elif time_metric == "Avg Order Value":
                hourly_data = filtered_df.groupby('hour').apply(
                    lambda x: x['revenue'].sum() / max(x['transaction_id'].nunique(), 1)
                ).reset_index()
                hourly_data.columns = ['hour', 'value']
            else:
                hourly_data = filtered_df.groupby('hour')[metric_col].sum().reset_index()
            
            hourly_data.columns = ['Hour', 'Value']
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(hourly_data, x='Hour', y='Value', markers=True,
                             color_discrete_sequence=['#6366f1'])
                fig.update_traces(line=dict(width=3), marker=dict(size=8))
                
                # Add peak hour highlighting
                peak_hour = hourly_data.loc[hourly_data['Value'].idxmax(), 'Hour']
                fig.add_vrect(x0=peak_hour-0.5, x1=peak_hour+0.5, 
                             fillcolor="rgba(16, 185, 129, 0.2)", 
                             layer="below", line_width=0)
                
                fig = apply_chart_style(fig, height=380)
                fig.update_layout(xaxis_title="Hour of Day", yaxis_title=time_metric)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Heatmap style
                fig2 = px.bar(hourly_data, x='Hour', y='Value',
                             color='Value', color_continuous_scale=['#1a1a2e', '#6366f1', '#ec4899'])
                fig2 = apply_chart_style(fig2, height=380, show_legend=False)
                fig2.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig2, use_container_width=True)
            
            # Insights
            peak_hour = hourly_data.loc[hourly_data['Value'].idxmax(), 'Hour']
            morning_avg = hourly_data[(hourly_data['Hour'] >= 8) & (hourly_data['Hour'] < 12)]['Value'].mean()
            afternoon_avg = hourly_data[(hourly_data['Hour'] >= 12) & (hourly_data['Hour'] < 17)]['Value'].mean()
            evening_avg = hourly_data[(hourly_data['Hour'] >= 17) & (hourly_data['Hour'] < 21)]['Value'].mean()
            
            render_insight_box("🕐", "Peak Hour", f"{peak_hour}:00 shows highest activity. Ensure resources are optimized during this time.", "success")
            
            if afternoon_avg > morning_avg and afternoon_avg > evening_avg:
                render_insight_box("☀️", "Afternoon Rush", "Afternoon hours (12-5 PM) show strongest performance.", "primary")
            elif evening_avg > morning_avg:
                render_insight_box("🌙", "Evening Peak", "Evening hours (5-9 PM) drive significant traffic.", "primary")
        else:
            render_empty_state("🕐", "Hourly Data Not Available", "Hour information not present in the dataset.")
    
    # =========================================================================
    # MONTHLY TREND
    # =========================================================================
    elif analysis_type == "Monthly Trend":
        render_chart_title("Monthly Performance Trend", "📈")
        
        if time_metric == "Transactions":
            monthly_data = filtered_df.groupby('month')[metric_col].nunique().reset_index()
        elif time_metric == "Avg Order Value":
            monthly_data = filtered_df.groupby('month').apply(
                lambda x: x['revenue'].sum() / max(x['transaction_id'].nunique(), 1)
            ).reset_index()
            monthly_data.columns = ['month', 'value']
        else:
            monthly_data = filtered_df.groupby('month')[metric_col].sum().reset_index()
        
        monthly_data.columns = ['Month', 'Value']
        monthly_data = monthly_data.sort_values('Month')
        
        # Calculate moving average
        monthly_data['MA_3'] = monthly_data['Value'].rolling(window=3, min_periods=1).mean()
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=monthly_data['Month'], y=monthly_data['Value'],
                name=time_metric, marker_color='#6366f1',
                opacity=0.7
            ))
            fig.add_trace(go.Scatter(
                x=monthly_data['Month'], y=monthly_data['MA_3'],
                name='3-Month MA', line=dict(color='#ec4899', width=3),
                mode='lines'
            ))
            fig = apply_chart_style(fig, height=400)
            fig.update_layout(xaxis_title="", yaxis_title=time_metric, barmode='overlay')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Month-over-month changes
            monthly_data['MoM_Change'] = monthly_data['Value'].pct_change() * 100
            
            st.markdown("#### Month-over-Month")
            for _, row in monthly_data.tail(5).iterrows():
                if pd.notna(row['MoM_Change']):
                    change = row['MoM_Change']
                    color = "#10b981" if change > 0 else "#ef4444"
                    st.markdown(f'<div style="display: flex; justify-content: space-between; padding: 8px 12px; background: rgba(255,255,255,0.03); border-radius: 8px; margin: 6px 0;"><span style="color: #a1a1aa;">{row["Month"]}</span><span style="color: {color}; font-weight: 600;">{change:+.1f}%</span></div>', unsafe_allow_html=True)
        
        # Insights
        if len(monthly_data) >= 3:
            trend = monthly_data['Value'].iloc[-3:].mean() - monthly_data['Value'].iloc[:3].mean()
            trend_direction = "upward" if trend > 0 else "downward"
            render_insight_box("📈" if trend > 0 else "📉", "Trend Analysis", f"Overall {trend_direction} trend detected. Recent 3-month average is ${abs(trend):,.0f} {'higher' if trend > 0 else 'lower'} than initial period.", "success" if trend > 0 else "warning")
    
    # =========================================================================
    # QUARTERLY COMPARISON
    # =========================================================================
    elif analysis_type == "Quarterly Comparison":
        render_chart_title("Quarterly Performance", "📊")
        
        if 'quarter' in filtered_df.columns:
            if time_metric == "Transactions":
                quarterly_data = filtered_df.groupby('quarter')[metric_col].nunique().reset_index()
            elif time_metric == "Avg Order Value":
                quarterly_data = filtered_df.groupby('quarter').apply(
                    lambda x: x['revenue'].sum() / max(x['transaction_id'].nunique(), 1)
                ).reset_index()
                quarterly_data.columns = ['quarter', 'value']
            else:
                quarterly_data = filtered_df.groupby('quarter')[metric_col].sum().reset_index()
            
            quarterly_data.columns = ['Quarter', 'Value']
            quarterly_data['Quarter'] = quarterly_data['Quarter'].apply(lambda x: f'Q{x}')
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.bar(quarterly_data, x='Quarter', y='Value',
                            color='Quarter', color_discrete_sequence=get_chart_colors())
                fig = apply_chart_style(fig, height=350, show_legend=False)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig2 = px.pie(quarterly_data, values='Value', names='Quarter',
                             color_discrete_sequence=get_chart_colors(), hole=0.5)
                fig2 = apply_chart_style(fig2, height=350)
                st.plotly_chart(fig2, use_container_width=True)
            
            best_quarter = quarterly_data.loc[quarterly_data['Value'].idxmax(), 'Quarter']
            render_insight_box("🏆", "Best Quarter", f"{best_quarter} shows highest {time_metric.lower()}. Plan major campaigns around this period.", "success")
    
    # =========================================================================
    # SEASONALITY ANALYSIS
    # =========================================================================
    elif analysis_type == "Seasonality":
        render_chart_title("Seasonality Analysis", "🌡️")
        
        if 'month' in filtered_df.columns:
            # Extract month number for seasonality
            filtered_df['month_num'] = pd.to_datetime(filtered_df['transaction_date']).dt.month
            
            if time_metric == "Transactions":
                seasonal_data = filtered_df.groupby('month_num')[metric_col].nunique().reset_index()
            else:
                seasonal_data = filtered_df.groupby('month_num')[metric_col].sum().reset_index()
            
            seasonal_data.columns = ['Month', 'Value']
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            seasonal_data['Month_Name'] = seasonal_data['Month'].apply(lambda x: month_names[x-1] if x <= 12 else 'Unknown')
            
            # Calculate seasonal index
            avg_value = seasonal_data['Value'].mean()
            seasonal_data['Seasonal_Index'] = (seasonal_data['Value'] / avg_value * 100).round(1)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(seasonal_data, x='Month_Name', y='Value', markers=True,
                             color_discrete_sequence=['#6366f1'])
                fig.update_traces(fill='tozeroy', fillcolor='rgba(99, 102, 241, 0.2)', line=dict(width=3))
                fig.add_hline(y=avg_value, line_dash="dash", line_color="#71717a",
                             annotation_text="Average")
                fig = apply_chart_style(fig, height=380)
                fig.update_layout(xaxis_title="", yaxis_title=time_metric)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Seasonal index chart
                colors = ['#10b981' if x >= 100 else '#ef4444' for x in seasonal_data['Seasonal_Index']]
                fig2 = px.bar(seasonal_data, x='Month_Name', y='Seasonal_Index',
                             color_discrete_sequence=['#6366f1'])
                fig2.update_traces(marker_color=colors)
                fig2.add_hline(y=100, line_dash="dash", line_color="#71717a",
                              annotation_text="Baseline (100)")
                fig2 = apply_chart_style(fig2, height=380, show_legend=False)
                fig2.update_layout(xaxis_title="", yaxis_title="Seasonal Index")
                st.plotly_chart(fig2, use_container_width=True)
            
            # Peak and low seasons
            peak_months = seasonal_data[seasonal_data['Seasonal_Index'] >= 110]['Month_Name'].tolist()
            low_months = seasonal_data[seasonal_data['Seasonal_Index'] <= 90]['Month_Name'].tolist()
            
            if peak_months:
                render_insight_box("📈", "Peak Season", f"High season months: {', '.join(peak_months)}. Maximize inventory and promotional efforts.", "success")
            if low_months:
                render_insight_box("📉", "Low Season", f"Low season months: {', '.join(low_months)}. Consider targeted promotions to boost sales.", "warning")


# =============================================================================
# SIDEBAR CONFIGURATION
# =============================================================================

def render_sidebar():
    """Render sidebar with data upload and navigation."""
    with st.sidebar:
        # Logo/Brand
        st.markdown('<div style="text-align: center; padding: 20px 0;"><span style="font-size: 2.5rem;">🚀</span><div style="font-size: 1.3rem; font-weight: 700; color: white; margin-top: 8px;">UAE Promo Pulse</div><div style="font-size: 0.8rem; color: #71717a;">Promotional Analytics Platform</div></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Data source selection
        st.markdown("### 📂 Data Source")
        
        data_source = st.radio(
            "Select data source:",
            ["📊 Sample Data (Demo)", "📁 Upload Your Files"],
            label_visibility="collapsed",
            key="sidebar_data_source_selector"
        )
        
        st.markdown("---")
        
        if data_source == "📁 Upload Your Files":
            st.markdown("### 📤 Upload Data Files")
            st.caption("Upload CSV files with the required columns")
            
            # 4 FILE UPLOADERS
            sales_file = st.file_uploader(
                "📈 Sales Data",
                type=['csv'],
                key='sidebar_sales_upload',
                help="Required: transaction_id, sku_id, store_id, quantity_sold, unit_price, transaction_date"
            )
            
            inventory_file = st.file_uploader(
                "📦 Inventory Data",
                type=['csv'],
                key='sidebar_inventory_upload',
                help="Required: record_id, sku_id, store_id, stock_level, reorder_point, reorder_quantity"
            )
            
            promotions_file = st.file_uploader(
                "🎯 Promotions Data",
                type=['csv'],
                key='sidebar_promotions_upload',
                help="Required: promotion_id, sku_id, store_id, promotion_type, discount_percentage, start_date, end_date"
            )
            
            products_file = st.file_uploader(
                "🏷️ Products/SKU Data",
                type=['csv'],
                key='sidebar_products_upload',
                help="Required: sku_id, product_name, category, brand, unit_cost"
            )
            
            # Check minimum required files (3 core + 1 optional)
            if sales_file and inventory_file and promotions_file:
                with st.spinner("Loading and validating data..."):
                    sales_df, inventory_df, promotions_df, products_df, error = load_and_process_data(
                        sales_file, inventory_file, promotions_file, products_file
                    )
                
                if error:
                    st.error(f"❌ Error: {error}")
                    # Footer
                    st.markdown("---")
                    st.markdown('<div style="text-align: center; color: #71717a; font-size: 0.75rem; padding: 10px 0;"><div>Version 2.0 Premium</div><div>© 2024 Data Rescue Team</div></div>', unsafe_allow_html=True)
                    return None, None, None, None
                
                st.success("✅ All files loaded successfully!")
                
                # Data summary
                with st.expander("📊 Data Summary", expanded=False):
                    st.markdown(f"**Sales:** {len(sales_df):,} records")
                    st.markdown(f"**Inventory:** {len(inventory_df):,} records")
                    st.markdown(f"**Promotions:** {len(promotions_df):,} records")
                    if products_df is not None:
                        st.markdown(f"**Products:** {len(products_df):,} records")
                
                # Footer
                st.markdown("---")
                st.markdown('<div style="text-align: center; color: #71717a; font-size: 0.75rem; padding: 10px 0;"><div>Version 2.0 Premium</div><div>© 2024 Data Rescue Team</div></div>', unsafe_allow_html=True)
                
                return sales_df, inventory_df, promotions_df, products_df
            
            else:
                st.info("📌 Please upload at least Sales, Inventory, and Promotions files")
                
                with st.expander("📋 Expected Data Schema"):
                    st.markdown("**Sales Data (Required):**")
                    st.code("transaction_id, sku_id, store_id, quantity_sold, unit_price, transaction_date")
                    
                    st.markdown("**Inventory Data (Required):**")
                    st.code("record_id, sku_id, store_id, stock_level, reorder_point, reorder_quantity, last_updated")
                    
                    st.markdown("**Promotions Data (Required):**")
                    st.code("promotion_id, sku_id, store_id, promotion_type, discount_percentage, start_date, end_date")
                    
                    st.markdown("**Products Data (Optional):**")
                    st.code("sku_id, product_name, category, brand, unit_cost, supplier_id")
                
                # Footer
                st.markdown("---")
                st.markdown('<div style="text-align: center; color: #71717a; font-size: 0.75rem; padding: 10px 0;"><div>Version 2.0 Premium</div><div>© 2024 Data Rescue Team</div></div>', unsafe_allow_html=True)
                
                return None, None, None, None
        
        else:
            # Use sample data
            st.markdown("### ℹ️ Sample Data")
            st.caption("Using demonstration dataset with synthetic UAE retail data")
            
            with st.spinner("Generating sample data..."):
                sales_df, inventory_df, promotions_df = generate_sample_data()
                products_df = None  # Sample data generates products info within sales_df
            
            # Data summary
            with st.expander("📊 Sample Data Info", expanded=False):
                st.markdown(f"**Sales:** {len(sales_df):,} transactions")
                st.markdown(f"**Inventory:** {len(inventory_df):,} records")
                st.markdown(f"**Promotions:** {len(promotions_df):,} campaigns")
                st.markdown(f"**SKUs:** {sales_df['sku_id'].nunique():,}")
                st.markdown(f"**Stores:** {sales_df['store_id'].nunique():,}")
                st.markdown(f"**Categories:** {sales_df['category'].nunique()}")
                st.markdown(f"**Regions:** {sales_df['region'].nunique()}")
            
            # Footer
            st.markdown("---")
            st.markdown('<div style="text-align: center; color: #71717a; font-size: 0.75rem; padding: 10px 0;"><div>Version 2.0 Premium</div><div>© 2024 Data Rescue Team</div></div>', unsafe_allow_html=True)
            
            return sales_df, inventory_df, promotions_df, products_df
# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point."""
    
    # Initialize session state
    if 'simulation_run' not in st.session_state:
        st.session_state['simulation_run'] = False
    
    # Load premium CSS
    load_premium_css()
    
    # Render sidebar and get data (now returns 4 values)
    data = render_sidebar()
    
    # Check if data is available
    if data is None or data[0] is None:
        # Show welcome screen
        render_hero_header()
        
        st.markdown("")
        
        render_insight_box(
            "👋",
            "Welcome to UAE Promo Pulse Simulator",
            "This premium analytics dashboard helps you analyze sales performance, monitor inventory health, evaluate promotional effectiveness, and simulate what-if scenarios. Select 'Sample Data' in the sidebar to explore with demo data, or upload your own CSV files.",
            "primary"
        )
        
        # Feature highlights
        st.markdown("")
        st.markdown("### ✨ Key Features")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            render_insight_box("📈", "Sales Analytics", "Deep dive into revenue trends, category performance, and regional insights.", "success")
        
        with col2:
            render_insight_box("📦", "Inventory Health", "Monitor stock levels, identify stockout risks, and optimize replenishment.", "warning")
        
        with col3:
            render_insight_box("🧹", "Data Cleaning", "Clean, validate, and transform your data with automated tools.", "accent")
        
        with col4:
            render_insight_box("🧪", "What-If Simulator", "Simulate promotions and predict outcomes with AI recommendations.", "primary")
        
        render_footer()
        return
    
    # Unpack data (4 values now)
    sales_df, inventory_df, promotions_df, products_df = data
    
    # Render main dashboard
    render_hero_header()
    
    # Overview KPIs
    render_overview_kpis(sales_df, inventory_df, promotions_df)
    
    render_divider()
    
    # Main navigation tabs - NOW INCLUDES DATA CLEANING
    tabs = st.tabs([
        "🧹 Data Cleaning",
        "📈 Sales Analytics",
        "📦 Inventory Health",
        "🎯 Promotions",
        "🧪 What-If Simulator",
        "🏪 Store Performance",
        "⏰ Time Analysis"
    ])
    
    with tabs[0]:
        render_data_cleaning(sales_df, inventory_df, promotions_df, products_df)
    
    with tabs[1]:
        render_sales_analysis(sales_df)
    
    with tabs[2]:
        render_inventory_analysis(inventory_df, sales_df)
    
    with tabs[3]:
        render_promotions_analysis(promotions_df, sales_df)
    
    with tabs[4]:
        render_promo_simulator(sales_df, inventory_df, promotions_df)
    
    with tabs[5]:
        render_store_performance(sales_df, inventory_df)
    
    with tabs[6]:
        render_time_analysis(sales_df)
    
    # Footer
    render_footer()


# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()

# =============================================================================
# DATA CLEANING & QUALITY SECTION
# =============================================================================

def render_data_cleaning(sales_df, inventory_df, promotions_df, products_df=None):
    """Render comprehensive data cleaning and quality analysis."""
    render_section_header("🧹", "Data Cleaning & Quality", "Analyze data quality, handle missing values, detect outliers, and clean your datasets")
    
    # =========================================================================
    # DATA SOURCE SELECTOR
    # =========================================================================
    st.markdown("#### 🎛️ Select Dataset to Analyze")
    
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        available_datasets = ["Sales Data", "Inventory Data", "Promotions Data"]
        if products_df is not None:
            available_datasets.append("Products Data")
        
        selected_dataset = st.selectbox(
            "📊 Dataset",
            available_datasets,
            key="dc_dataset_selector"
        )
    
    with col2:
        cleaning_action = st.selectbox(
            "🔧 Analysis Type",
            ["Data Overview", "Missing Values", "Duplicates", "Outliers", "Data Types", "Value Distribution", "Auto Clean"],
            key="dc_analysis_type"
        )
    
    with col3:
        export_cleaned = st.checkbox("📥 Enable Export", key="dc_export_checkbox")
    
    st.markdown("")
    
    # Select the appropriate dataframe
    if selected_dataset == "Sales Data":
        df = sales_df.copy()
        df_name = "sales"
    elif selected_dataset == "Inventory Data":
        df = inventory_df.copy()
        df_name = "inventory"
    elif selected_dataset == "Promotions Data":
        df = promotions_df.copy()
        df_name = "promotions"
    elif products_df is not None:
        df = products_df.copy()
        df_name = "products"
    else:
        df = sales_df.copy()
        df_name = "sales"
    
    if df.empty:
        render_empty_state("📊", "No Data Available", "The selected dataset is empty.")
        return
    
    # =========================================================================
    # DATA QUALITY SCORE
    # =========================================================================
    
    # Calculate quality metrics
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    completeness = ((total_cells - missing_cells) / total_cells * 100) if total_cells > 0 else 0
    uniqueness = ((len(df) - duplicate_rows) / len(df) * 100) if len(df) > 0 else 0
    
    # Overall quality score
    quality_score = (completeness * 0.5 + uniqueness * 0.3 + 20)
    quality_score = min(100, quality_score)
    
    # Quality KPIs
    quality_kpis = [
        {"icon": "📊", "value": f"{len(df):,}", "label": "Total Rows", "type": "primary"},
        {"icon": "📋", "value": f"{len(df.columns)}", "label": "Columns", "type": "accent"},
        {"icon": "❓", "value": f"{missing_cells:,}", "label": "Missing Values", "type": "warning" if missing_cells > 0 else "success"},
        {"icon": "👥", "value": f"{duplicate_rows:,}", "label": "Duplicates", "type": "danger" if duplicate_rows > 0 else "success"},
        {"icon": "✅", "value": f"{completeness:.1f}%", "label": "Completeness", "type": "success" if completeness > 95 else "warning"},
        {"icon": "⭐", "value": f"{quality_score:.0f}/100", "label": "Quality Score", "type": "success" if quality_score > 80 else "warning"},
    ]
    render_kpi_row(quality_kpis)
    
    render_divider_subtle()
    
    # Store for cleaning operations
    cleaned_df = df.copy()
    cleaning_log = []
    
    # =========================================================================
    # DATA OVERVIEW
    # =========================================================================
    if cleaning_action == "Data Overview":
        render_chart_title("📋 Dataset Overview", "📊")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Column Information")
            
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Non-Null': df.count().values,
                'Null': df.isnull().sum().values,
                'Unique': df.nunique().values
            })
            col_info['Null %'] = (col_info['Null'] / len(df) * 100).round(2)
            
            st.dataframe(col_info, use_container_width=True, hide_index=True, height=400)
        
        with col2:
            st.markdown("##### Data Sample (First 10 Rows)")
            st.dataframe(df.head(10), use_container_width=True, height=400)
        
        # Column type distribution
        st.markdown("")
        render_chart_title("Data Type Distribution", "📊")
        
        type_counts = df.dtypes.astype(str).value_counts().reset_index()
        type_counts.columns = ['Data Type', 'Count']
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.pie(type_counts, values='Count', names='Data Type',
                        color_discrete_sequence=get_chart_colors(), hole=0.5)
            fig = apply_chart_style(fig, height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Memory usage
            memory_usage = df.memory_usage(deep=True)
            total_memory = memory_usage.sum()
            
            st.markdown("##### Memory Usage")
            st.markdown(f'<div style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 12px; padding: 16px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.85rem;">Total Memory</div><div style="color: #6366f1; font-size: 1.5rem; font-weight: 700;">{total_memory / 1024 / 1024:.2f} MB</div></div>', unsafe_allow_html=True)
            
            st.markdown("")
            st.markdown("##### Quick Stats for Numeric Columns")
            
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                st.dataframe(df[numeric_cols].describe().round(2), use_container_width=True)
            else:
                st.info("No numeric columns in this dataset.")
    
    # =========================================================================
    # MISSING VALUES ANALYSIS
    # =========================================================================
    elif cleaning_action == "Missing Values":
        render_chart_title("❓ Missing Values Analysis", "🔍")
        
        # Missing values summary
        missing_df = pd.DataFrame({
            'Column': df.columns,
            'Missing': df.isnull().sum().values,
            'Present': df.count().values,
            'Missing %': (df.isnull().sum().values / len(df) * 100).round(2)
        })
        missing_df = missing_df.sort_values('Missing', ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Bar chart of missing values
            missing_with_values = missing_df[missing_df['Missing'] > 0]
            if len(missing_with_values) > 0:
                fig = px.bar(missing_with_values, 
                            x='Column', y='Missing',
                            color='Missing %',
                            color_continuous_scale=['#10b981', '#f59e0b', '#ef4444'])
                fig = apply_chart_style(fig, height=350, show_legend=False)
                fig.update_layout(xaxis_title="", yaxis_title="Missing Count", coloraxis_showscale=False)
                st.plotly_chart(fig, use_container_width=True)
            else:
                render_insight_box("✅", "No Missing Values", "All columns have complete data!", "success")
        
        with col2:
            # Missing pattern heatmap (sample)
            sample_size = min(100, len(df))
            sample_df = df.sample(sample_size, random_state=42) if len(df) > sample_size else df
            
            missing_matrix = sample_df.isnull().astype(int)
            
            if missing_matrix.sum().sum() > 0:
                fig2 = px.imshow(missing_matrix.T, 
                               labels=dict(x="Row", y="Column", color="Missing"),
                               color_continuous_scale=['#1a1a2e', '#ef4444'],
                               aspect='auto')
                fig2 = apply_chart_style(fig2, height=350)
                fig2.update_layout(coloraxis_showscale=False)
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.markdown("")
                render_insight_box("📊", "Missing Pattern", "No missing values to display in heatmap.", "primary")
        
        # Missing values table
        st.markdown("##### Missing Values by Column")
        st.dataframe(missing_df, use_container_width=True, hide_index=True)
        
        render_divider_subtle()
        
        # Handle missing values
        st.markdown("### 🔧 Handle Missing Values")
        
        cols_with_missing = missing_df[missing_df['Missing'] > 0]['Column'].tolist()
        
        if cols_with_missing:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                target_col = st.selectbox(
                    "Select Column",
                    cols_with_missing,
                    key="dc_missing_target_col"
                )
            
            with col2:
                fill_method = st.selectbox(
                    "Fill Method",
                    ["Drop Rows", "Fill with Mean", "Fill with Median", "Fill with Mode", "Fill with Zero", "Fill with Custom", "Forward Fill", "Backward Fill"],
                    key="dc_fill_method"
                )
            
            with col3:
                custom_value = ""
                if fill_method == "Fill with Custom":
                    custom_value = st.text_input("Custom Value", key="dc_custom_fill_value")
            
            if st.button("🔄 Apply Fix", key="dc_apply_missing_fix"):
                original_missing = cleaned_df[target_col].isnull().sum()
                
                if fill_method == "Drop Rows":
                    cleaned_df = cleaned_df.dropna(subset=[target_col])
                    cleaning_log.append(f"Dropped {original_missing} rows with missing {target_col}")
                elif fill_method == "Fill with Mean":
                    if pd.api.types.is_numeric_dtype(cleaned_df[target_col]):
                        fill_val = cleaned_df[target_col].mean()
                        cleaned_df[target_col] = cleaned_df[target_col].fillna(fill_val)
                        cleaning_log.append(f"Filled {target_col} with mean: {fill_val:.2f}")
                    else:
                        st.error("Mean can only be calculated for numeric columns")
                elif fill_method == "Fill with Median":
                    if pd.api.types.is_numeric_dtype(cleaned_df[target_col]):
                        fill_val = cleaned_df[target_col].median()
                        cleaned_df[target_col] = cleaned_df[target_col].fillna(fill_val)
                        cleaning_log.append(f"Filled {target_col} with median: {fill_val:.2f}")
                    else:
                        st.error("Median can only be calculated for numeric columns")
                elif fill_method == "Fill with Mode":
                    mode_series = cleaned_df[target_col].mode()
                    if len(mode_series) > 0:
                        fill_val = mode_series.iloc[0]
                        cleaned_df[target_col] = cleaned_df[target_col].fillna(fill_val)
                        cleaning_log.append(f"Filled {target_col} with mode: {fill_val}")
                elif fill_method == "Fill with Zero":
                    cleaned_df[target_col] = cleaned_df[target_col].fillna(0)
                    cleaning_log.append(f"Filled {target_col} with 0")
                elif fill_method == "Fill with Custom" and custom_value:
                    cleaned_df[target_col] = cleaned_df[target_col].fillna(custom_value)
                    cleaning_log.append(f"Filled {target_col} with: {custom_value}")
                elif fill_method == "Forward Fill":
                    cleaned_df[target_col] = cleaned_df[target_col].ffill()
                    cleaning_log.append(f"Forward filled {target_col}")
                elif fill_method == "Backward Fill":
                    cleaned_df[target_col] = cleaned_df[target_col].bfill()
                    cleaning_log.append(f"Backward filled {target_col}")
                
                if cleaning_log:
                    st.success(f"✅ {cleaning_log[-1]}")
        else:
            render_insight_box("✅", "No Missing Values", "This dataset has no missing values. Great data quality!", "success")
    
    # =========================================================================
    # DUPLICATES ANALYSIS
    # =========================================================================
    elif cleaning_action == "Duplicates":
        render_chart_title("👥 Duplicate Analysis", "🔍")
        
        # Find duplicates
        duplicate_count = df.duplicated().sum()
        duplicate_rows = df[df.duplicated(keep=False)]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            color = "#ef4444" if duplicate_count > 0 else "#10b981"
            st.markdown(f'<div style="background: {color}20; border: 1px solid {color}40; border-radius: 12px; padding: 16px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.85rem;">Total Duplicates</div><div style="color: {color}; font-size: 1.5rem; font-weight: 700;">{duplicate_count:,}</div></div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 16px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.85rem;">Unique Rows</div><div style="color: #10b981; font-size: 1.5rem; font-weight: 700;">{len(df) - duplicate_count:,}</div></div>', unsafe_allow_html=True)
        
        with col3:
            dup_pct = (duplicate_count / len(df) * 100) if len(df) > 0 else 0
            color = "#f59e0b" if dup_pct > 5 else "#10b981"
            st.markdown(f'<div style="background: {color}20; border: 1px solid {color}40; border-radius: 12px; padding: 16px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.85rem;">Duplicate %</div><div style="color: {color}; font-size: 1.5rem; font-weight: 700;">{dup_pct:.2f}%</div></div>', unsafe_allow_html=True)
        
        st.markdown("")
        
        # Subset duplicate check
        st.markdown("##### Check Duplicates by Specific Columns")
        
        col1, col2 = st.columns(2)
        
        with col1:
            default_cols = df.columns[:3].tolist() if len(df.columns) >= 3 else df.columns.tolist()
            subset_cols = st.multiselect(
                "Select columns to check",
                df.columns.tolist(),
                default=default_cols,
                key="dc_dup_subset_cols"
            )
        
        with col2:
            if subset_cols:
                subset_dups = df.duplicated(subset=subset_cols).sum()
                st.metric("Duplicates in Selected Columns", f"{subset_dups:,}")
        
        if duplicate_count > 0:
            st.markdown("##### Sample Duplicate Rows")
            st.dataframe(duplicate_rows.head(20), use_container_width=True, height=300)
            
            render_divider_subtle()
            
            # Remove duplicates
            st.markdown("### 🔧 Remove Duplicates")
            
            col1, col2 = st.columns(2)
            
            with col1:
                keep_option = st.selectbox(
                    "Keep which occurrence?",
                    ["First", "Last", "None (Remove All)"],
                    key="dc_dup_keep"
                )
            
            with col2:
                dup_subset = st.multiselect(
                    "Based on columns (empty = all columns)",
                    df.columns.tolist(),
                    key="dc_dup_remove_subset"
                )
            
            if st.button("🗑️ Remove Duplicates", key="dc_remove_dups"):
                keep_val = 'first' if keep_option == "First" else ('last' if keep_option == "Last" else False)
                subset_val = dup_subset if dup_subset else None
                
                original_len = len(cleaned_df)
                cleaned_df = cleaned_df.drop_duplicates(subset=subset_val, keep=keep_val)
                removed = original_len - len(cleaned_df)
                
                cleaning_log.append(f"Removed {removed} duplicate rows")
                st.success(f"✅ Removed {removed} duplicate rows")
        else:
            render_insight_box("✅", "No Duplicates Found", "This dataset has no duplicate rows.", "success")
    
    # =========================================================================
    # OUTLIERS ANALYSIS
    # =========================================================================
    elif cleaning_action == "Outliers":
        render_chart_title("📈 Outlier Detection", "🔍")
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if not numeric_cols:
            render_empty_state("📊", "No Numeric Columns", "Outlier detection requires numeric columns.")
            return
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            outlier_col = st.selectbox(
                "Select Column",
                numeric_cols,
                key="dc_outlier_col"
            )
        
        with col2:
            outlier_method = st.selectbox(
                "Detection Method",
                ["IQR (Interquartile Range)", "Z-Score", "Percentile"],
                key="dc_outlier_method"
            )
        
        with col3:
            if outlier_method == "IQR (Interquartile Range)":
                iqr_multiplier = st.slider("IQR Multiplier", 1.0, 3.0, 1.5, 0.1, key="dc_iqr_mult")
            elif outlier_method == "Z-Score":
                z_threshold = st.slider("Z-Score Threshold", 1.0, 4.0, 3.0, 0.1, key="dc_z_thresh")
            else:
                lower_pct = st.slider("Lower Percentile", 0, 10, 1, key="dc_lower_pct")
                upper_pct = st.slider("Upper Percentile", 90, 100, 99, key="dc_upper_pct")
        
        # Calculate outliers
        col_data = df[outlier_col].dropna()
        
        if len(col_data) == 0:
            st.warning("No valid data in selected column.")
            return
        
        if outlier_method == "IQR (Interquartile Range)":
            Q1 = col_data.quantile(0.25)
            Q3 = col_data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - iqr_multiplier * IQR
            upper_bound = Q3 + iqr_multiplier * IQR
        elif outlier_method == "Z-Score":
            mean = col_data.mean()
            std = col_data.std()
            if std == 0:
                lower_bound = mean
                upper_bound = mean
            else:
                lower_bound = mean - z_threshold * std
                upper_bound = mean + z_threshold * std
        else:
            lower_bound = col_data.quantile(lower_pct / 100)
            upper_bound = col_data.quantile(upper_pct / 100)
        
        outliers = df[(df[outlier_col] < lower_bound) | (df[outlier_col] > upper_bound)]
        outlier_count = len(outliers)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            # Box plot
            fig = px.box(df, y=outlier_col, color_discrete_sequence=['#6366f1'])
            fig.add_hline(y=lower_bound, line_dash="dash", line_color="#ef4444",
                         annotation_text=f"Lower: {lower_bound:.2f}")
            fig.add_hline(y=upper_bound, line_dash="dash", line_color="#ef4444",
                         annotation_text=f"Upper: {upper_bound:.2f}")
            fig = apply_chart_style(fig, height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Histogram with outlier bounds
            fig2 = px.histogram(df, x=outlier_col, nbins=50, color_discrete_sequence=['#6366f1'])
            fig2.add_vline(x=lower_bound, line_dash="dash", line_color="#ef4444")
            fig2.add_vline(x=upper_bound, line_dash="dash", line_color="#ef4444")
            fig2 = apply_chart_style(fig2, height=350)
            st.plotly_chart(fig2, use_container_width=True)
        
        # Outlier stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            color = "#ef4444" if outlier_count > 0 else "#10b981"
            st.markdown(f'<div style="background: {color}20; border: 1px solid {color}40; border-radius: 8px; padding: 12px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.75rem;">Outliers Found</div><div style="color: {color}; font-size: 1.2rem; font-weight: 700;">{outlier_count:,}</div></div>', unsafe_allow_html=True)
        with col2:
            outlier_pct = (outlier_count / len(df) * 100) if len(df) > 0 else 0
            st.markdown(f'<div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 12px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.75rem;">Outlier %</div><div style="color: #f59e0b; font-size: 1.2rem; font-weight: 700;">{outlier_pct:.2f}%</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 8px; padding: 12px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.75rem;">Lower Bound</div><div style="color: #6366f1; font-size: 1.2rem; font-weight: 700;">{lower_bound:.2f}</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 8px; padding: 12px; text-align: center;"><div style="color: #a1a1aa; font-size: 0.75rem;">Upper Bound</div><div style="color: #6366f1; font-size: 1.2rem; font-weight: 700;">{upper_bound:.2f}</div></div>', unsafe_allow_html=True)
        
        if outlier_count > 0:
            st.markdown("")
            st.markdown("##### Outlier Rows Sample")
            st.dataframe(outliers.head(20), use_container_width=True, height=250)
            
            render_divider_subtle()
            
            # Handle outliers
            st.markdown("### 🔧 Handle Outliers")
            
            outlier_action = st.selectbox(
                "Select Action",
                ["Remove Outliers", "Cap/Clip Values", "Replace with Mean", "Replace with Median"],
                key="dc_outlier_action"
            )
            
            if st.button("🔄 Apply Outlier Fix", key="dc_apply_outlier_fix"):
                if outlier_action == "Remove Outliers":
                    original_len = len(cleaned_df)
                    cleaned_df = cleaned_df[(cleaned_df[outlier_col] >= lower_bound) & (cleaned_df[outlier_col] <= upper_bound)]
                    removed = original_len - len(cleaned_df)
                    cleaning_log.append(f"Removed {removed} outlier rows from {outlier_col}")
                elif outlier_action == "Cap/Clip Values":
                    cleaned_df[outlier_col] = cleaned_df[outlier_col].clip(lower_bound, upper_bound)
                    cleaning_log.append(f"Capped {outlier_col} to [{lower_bound:.2f}, {upper_bound:.2f}]")
                elif outlier_action == "Replace with Mean":
                    mean_val = cleaned_df[outlier_col].mean()
                    mask = (cleaned_df[outlier_col] < lower_bound) | (cleaned_df[outlier_col] > upper_bound)
                    cleaned_df.loc[mask, outlier_col] = mean_val
                    cleaning_log.append(f"Replaced outliers in {outlier_col} with mean: {mean_val:.2f}")
                elif outlier_action == "Replace with Median":
                    median_val = cleaned_df[outlier_col].median()
                    mask = (cleaned_df[outlier_col] < lower_bound) | (cleaned_df[outlier_col] > upper_bound)
                    cleaned_df.loc[mask, outlier_col] = median_val
                    cleaning_log.append(f"Replaced outliers in {outlier_col} with median: {median_val:.2f}")
                
                st.success(f"✅ {cleaning_log[-1]}")
        else:
            render_insight_box("✅", "No Outliers Detected", f"No outliers found in {outlier_col} using {outlier_method}.", "success")
    
    # =========================================================================
    # DATA TYPES ANALYSIS
    # =========================================================================
    elif cleaning_action == "Data Types":
        render_chart_title("🔤 Data Type Analysis", "🔍")
        
        # Current types
        type_info = pd.DataFrame({
            'Column': df.columns,
            'Current Type': df.dtypes.astype(str),
            'Sample Value': [str(df[col].iloc[0]) if len(df) > 0 else 'N/A' for col in df.columns],
            'Unique Values': df.nunique().values
        })
        
        st.markdown("##### Current Data Types")
        st.dataframe(type_info, use_container_width=True, hide_index=True)
        
        render_divider_subtle()
        
        # Convert types
        st.markdown("### 🔧 Convert Data Types")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            convert_col = st.selectbox(
                "Select Column",
                df.columns.tolist(),
                key="dc_convert_col"
            )
        
        with col2:
            target_type = st.selectbox(
                "Convert To",
                ["string", "integer", "float", "datetime", "category", "boolean"],
                key="dc_target_type"
            )
        
        with col3:
            date_format = ""
            if target_type == "datetime":
                date_format = st.text_input("Date Format (optional)", placeholder="%Y-%m-%d", key="dc_date_format")
        
        if st.button("🔄 Convert Type", key="dc_convert_type"):
            try:
                if target_type == "string":
                    cleaned_df[convert_col] = cleaned_df[convert_col].astype(str)
                    cleaning_log.append(f"Converted {convert_col} to string")
                elif target_type == "integer":
                    cleaned_df[convert_col] = pd.to_numeric(cleaned_df[convert_col], errors='coerce').astype('Int64')
                    cleaning_log.append(f"Converted {convert_col} to integer")
                elif target_type == "float":
                    cleaned_df[convert_col] = pd.to_numeric(cleaned_df[convert_col], errors='coerce')
                    cleaning_log.append(f"Converted {convert_col} to float")
                elif target_type == "datetime":
                    if date_format:
                        cleaned_df[convert_col] = pd.to_datetime(cleaned_df[convert_col], format=date_format, errors='coerce')
                    else:
                        cleaned_df[convert_col] = pd.to_datetime(cleaned_df[convert_col], errors='coerce')
                    cleaning_log.append(f"Converted {convert_col} to datetime")
                elif target_type == "category":
                    cleaned_df[convert_col] = cleaned_df[convert_col].astype('category')
                    cleaning_log.append(f"Converted {convert_col} to category")
                elif target_type == "boolean":
                    cleaned_df[convert_col] = cleaned_df[convert_col].astype(bool)
                    cleaning_log.append(f"Converted {convert_col} to boolean")
                
                st.success(f"✅ {cleaning_log[-1]}")
            except Exception as e:
                st.error(f"❌ Conversion failed: {str(e)}")
    
    # =========================================================================
    # VALUE DISTRIBUTION
    # =========================================================================
    elif cleaning_action == "Value Distribution":
        render_chart_title("📊 Value Distribution Analysis", "🔍")
        
        col1, col2 = st.columns(2)
        
        with col1:
            dist_col = st.selectbox(
                "Select Column",
                df.columns.tolist(),
                key="dc_dist_col"
            )
        
        with col2:
            chart_type = st.selectbox(
                "Chart Type",
                ["Histogram", "Bar Chart", "Box Plot", "Violin Plot"],
                key="dc_dist_chart_type"
            )
        
        col_data = df[dist_col].dropna()
        
        if len(col_data) == 0:
            st.warning("No valid data in selected column.")
            return
        
        col1, col2 = st.columns(2)
        
        with col1:
            if pd.api.types.is_numeric_dtype(col_data):
                if chart_type == "Histogram":
                    fig = px.histogram(df, x=dist_col, nbins=30, color_discrete_sequence=['#6366f1'])
                elif chart_type == "Box Plot":
                    fig = px.box(df, y=dist_col, color_discrete_sequence=['#6366f1'])
                elif chart_type == "Violin Plot":
                    fig = px.violin(df, y=dist_col, color_discrete_sequence=['#6366f1'], box=True)
                else:
                    fig = px.histogram(df, x=dist_col, nbins=30, color_discrete_sequence=['#6366f1'])
            else:
                value_counts = col_data.value_counts().head(20).reset_index()
                value_counts.columns = [dist_col, 'Count']
                fig = px.bar(value_counts, x=dist_col, y='Count', color_discrete_sequence=['#6366f1'])
            
            fig = apply_chart_style(fig, height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Statistics
            st.markdown("##### Column Statistics")
            
            if pd.api.types.is_numeric_dtype(col_data):
                stats = col_data.describe()
                stats_df = pd.DataFrame({
                    'Statistic': stats.index,
                    'Value': stats.values.round(4)
                })
                st.dataframe(stats_df, use_container_width=True, hide_index=True)
            else:
                value_counts = col_data.value_counts().head(15).reset_index()
                value_counts.columns = ['Value', 'Count']
                value_counts['Percentage'] = (value_counts['Count'] / len(col_data) * 100).round(2)
                st.dataframe(value_counts, use_container_width=True, hide_index=True)
    
    # =========================================================================
    # AUTO CLEAN
    # =========================================================================
    elif cleaning_action == "Auto Clean":
        render_chart_title("🤖 Automated Data Cleaning", "⚡")
        
        st.markdown("##### Select Cleaning Operations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            auto_remove_dups = st.checkbox("Remove duplicate rows", value=True, key="dc_auto_dups")
            auto_fill_numeric = st.checkbox("Fill numeric missing with median", value=True, key="dc_auto_numeric")
            auto_fill_categorical = st.checkbox("Fill categorical missing with mode", value=True, key="dc_auto_cat")
        
        with col2:
            auto_trim_strings = st.checkbox("Trim whitespace from strings", value=True, key="dc_auto_trim")
            auto_lowercase_cols = st.checkbox("Lowercase column names", value=True, key="dc_auto_lower")
            auto_remove_empty_cols = st.checkbox("Remove columns with >50% missing", value=False, key="dc_auto_empty")
        
        st.markdown("")
        
        if st.button("🚀 Run Auto Clean", type="primary", key="dc_run_auto_clean"):
            with st.spinner("Cleaning data..."):
                operations = []
                
                # Remove duplicates
                if auto_remove_dups:
                    original = len(cleaned_df)
                    cleaned_df = cleaned_df.drop_duplicates()
                    removed = original - len(cleaned_df)
                    if removed > 0:
                        operations.append(f"✓ Removed {removed} duplicate rows")
                
                # Fill numeric missing
                if auto_fill_numeric:
                    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
                    for col in numeric_cols:
                        missing = cleaned_df[col].isnull().sum()
                        if missing > 0:
                            median_val = cleaned_df[col].median()
                            cleaned_df[col] = cleaned_df[col].fillna(median_val)
                            operations.append(f"✓ Filled {missing} missing in '{col}' with median ({median_val:.2f})")
                
                # Fill categorical missing
                if auto_fill_categorical:
                    cat_cols = cleaned_df.select_dtypes(include=['object', 'category']).columns
                    for col in cat_cols:
                        missing = cleaned_df[col].isnull().sum()
                        if missing > 0:
                            mode_series = cleaned_df[col].mode()
                            if len(mode_series) > 0:
                                mode_val = mode_series.iloc[0]
                                cleaned_df[col] = cleaned_df[col].fillna(mode_val)
                                operations.append(f"✓ Filled {missing} missing in '{col}' with mode ({mode_val})")
                
                # Trim whitespace
                if auto_trim_strings:
                    string_cols = cleaned_df.select_dtypes(include=['object']).columns
                    for col in string_cols:
                        cleaned_df[col] = cleaned_df[col].astype(str).str.strip()
                    if len(string_cols) > 0:
                        operations.append(f"✓ Trimmed whitespace from {len(string_cols)} string columns")
                
                # Lowercase column names
                if auto_lowercase_cols:
                    cleaned_df.columns = cleaned_df.columns.str.lower().str.replace(' ', '_')
                    operations.append("✓ Standardized column names (lowercase, underscores)")
                
                # Remove empty columns
                if auto_remove_empty_cols:
                    empty_threshold = 0.5
                    cols_to_drop = [col for col in cleaned_df.columns if cleaned_df[col].isnull().mean() > empty_threshold]
                    if cols_to_drop:
                        cleaned_df = cleaned_df.drop(columns=cols_to_drop)
                        operations.append(f"✓ Removed {len(cols_to_drop)} columns with >50% missing")
                
                cleaning_log.extend(operations)
            
            # Show results
            st.success("✅ Auto cleaning complete!")
            
            if operations:
                st.markdown("##### Operations Performed")
                for op in operations:
                    st.markdown(f"• {op}")
            
            # Before/After comparison
            st.markdown("")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("##### 📊 Before Cleaning")
                st.metric("Rows", f"{len(df):,}")
                st.metric("Columns", f"{len(df.columns)}")
                st.metric("Missing Values", f"{df.isnull().sum().sum():,}")
            
            with col2:
                st.markdown("##### ✨ After Cleaning")
                rows_diff = len(cleaned_df) - len(df)
                cols_diff = len(cleaned_df.columns) - len(df.columns)
                missing_diff = cleaned_df.isnull().sum().sum() - df.isnull().sum().sum()
                
                st.metric("Rows", f"{len(cleaned_df):,}", delta=f"{rows_diff:,}" if rows_diff != 0 else None)
                st.metric("Columns", f"{len(cleaned_df.columns)}", delta=f"{cols_diff}" if cols_diff != 0 else None)
                st.metric("Missing Values", f"{cleaned_df.isnull().sum().sum():,}", delta=f"{missing_diff:,}" if missing_diff != 0 else None)
    
    # =========================================================================
    # CLEANING LOG & EXPORT
    # =========================================================================
    render_divider_subtle()
    
    if cleaning_log:
        st.markdown("### 📋 Cleaning Log")
        for i, log in enumerate(cleaning_log, 1):
            st.markdown(f"{i}. {log}")
    
    # Export option
    if export_cleaned:
        st.markdown("### 📥 Export Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            csv = cleaned_df.to_csv(index=False)
            st.download_button(
                label=f"📥 Download {df_name.title()} Data as CSV",
                data=csv,
                file_name=f"{df_name}_data_export.csv",
                mime="text/csv",
                key="dc_download_csv"
            )
        
        with col2:
            st.info(f"Dataset: {len(cleaned_df):,} rows × {len(cleaned_df.columns)} columns")
    
    # Return cleaned data
    return cleaned_df, cleaning_log, None, None

# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()



