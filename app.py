import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود التنسيق (تم إصلاح توافق السهم والموبايل)
st.markdown(
    """
    <style>
    /* خلفية التطبيق */
    .stApp { background-color: #E3F2FD !important; }
    
    /* توسيط الشعار والعناوين */
    [data-testid="stImage"] { display: flex !important; justify-content: center !important; }
    .main-title { text-align: center !important; color: #1E3A8A !important; width: 100%; display: block; }
    .sub-title { text-align: center !important; color: #1E3A8A !important; width: 100%; display: block; font-size: 1.1rem; margin-top: -10px; }

    /* تحسين شكل القائمة المنسدلة لتعمل بسلاسة على الموبايل */
    div[data-baseweb="select"] {
        background-color: white !important;
        border-radius: 8px !important;
        border: 1px solid #1E3A8A !important;
    }
    
    /* إجبار لون النص داخل القائمة ليكون أسود واضح */
    div[data-testid="stSelectbox"] label {
        color: #1E3A8A !important;
        font-weight: bold;
    }

    /* كروت المواد */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 15px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1) !important;
        margin-bottom: 15px !important;
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

# 4. العناوين
st.markdown("<h1 class='main-title'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 5. اختيار المرحلة الدراسية
stages_options = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
# ملاحظة: تم ترك الـ selectbox بدون تعقيدات CSS داخلية لضمان عمل السهم
stage = st.selectbox("Select your grade / اختر المرحلة الدراسية:", stages_options)

if stage == "Choose Grade / اختر المرحلة":
    st.info("👋 Welcome! Please select a grade above to view lessons.")
else:
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
        df = pd.read_csv(url)
        
        if not df.empty:
            for index, row in df.iterrows():
                with st.container(border=True):
                    # البيانات
                    subject_name = row.iloc[0]
                    upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                    
                    st.markdown(f"<div style='background-color:#1E3A8A; color:white; padding:4px 10px; border-radius:10px; display:inline-block; font-size:14px;'>📅 {upload_date}</div>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='color:#1E3A8A; margin-top:10px;'>{subject_name}</h3>", unsafe_allow_html=True)
                    
                    st.markdown(f"<p style='color:black;'><b>📖 Lesson:</b> {row.iloc[1]}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color:black;'><b>📝 Homework:</b> {row.iloc[2]}</p>", unsafe_allow_html=True)
                    
                    if len(row) > 3 and pd.notna(row.iloc[3]):
                        st.markdown(f"<p style='color:#155724; background-color:#d4edda; padding:5px; border-radius:5px;'><b>💡 Notes:</b> {row.iloc[3]}</p>", unsafe_allow_html=True)
        else:
            st.warning("No data found for this grade.")
    except Exception as e:
        st.error("Connection error. Please refresh.")

# 6. حقوق الملكية
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #1E3A8A; padding: 20px;'>
        <p style='font-size: 16px; font-weight: bold;'>Copyright © 2026: Mr. Kareem Magdy</p>
        <p style='font-size: 12px;'>Fadl Modern Language School - All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
