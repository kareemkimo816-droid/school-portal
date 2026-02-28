import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود التنسيق الشامل (توسيط إجباري وألوان واضحة للموبايل)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E3F2FD !important;
    }
    /* توسيط الشعار */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
    }
    /* توسيط العناوين */
    .main-title {
        text-align: center !important;
        color: #1E3A8A !important;
        width: 100%;
        display: block;
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
    /* كروت المواد */
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

# 3. عرض الشعار في المنتصف
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 4. العناوين (توسيط إجباري)
st.markdown("<h1 class='main-title'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)

st.divider()

# 5. اختيار المرحلة
stages_options = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select your grade / اختر المرحلة الدراسية:", stages_options)

if stage == "Choose Grade / اختر المرحلة":
    st.info("👋 Welcome! Please select a grade above.")
else:
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
        df = pd.read_csv(url)
        
        if not df.empty:
            for index, row in df.iterrows():
                with st.container(border=True):
                    subject_name = row.iloc[0]
                    # التاريخ في العمود الخامس (E)
                    upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                    
                    st.markdown(f"<div style='background-color:#1E3A8A; color:white; padding:4px 10px; border-radius:10px; display:inline-block; font-size:14px;'>📅 {upload_date}</div>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='color:#1E3A8A; margin-top:10px;'>{subject_name}</h3>", unsafe_allow_html=True)
                    
                    st.markdown(f"
