import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود التنسيق الشامل (ألوان وتوسيط إجباري)
st.markdown(
    """
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #E3F2FD !important;
    }

    /* توسيط أي صورة داخل الصفحة */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* توسيط العناوين */
    .main-title {
        text-align: center !important;
        color: #1E3A8A !important;
        width: 100%;
        display: block;
        margin-top: 10px;
    }
    .sub-title {
        text-align: center !important;
        color: #1E3A8A !important;
        width: 100%;
        display: block;
        font-size: 1.1rem;
        margin-top: -10px;
    }

    /* تنسيق قائمة الاختيار للموبايل */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 2px solid #1E3A8A !important;
    }

    /* تنسيق كروت المواد */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 15px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. عرض الشعار في المنتصف (استخدام أعمدة متوازنة)
col1, col2, col3 = st.columns([1, 2, 1]) # جعل العمود الأوسط أكبر قليلاً للشعار
with col
