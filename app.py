import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود تنسيق الألوان القوي (يجبر الموبايل على إظهار الألوان بوضوح)
st.markdown(
    """
    <style>
    /* خلفية التطبيق كاملة */
    .stApp {
        background-color: #E3F2FD !important;
    }
    /* تنسيق المربعات (البطاقات) الخاصة بالمواد */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important; /* أبيض صريح */
        border: 2px solid #1E3A8A !important; /* إطار أزرق */
        border-radius: 15px !important;
        padding: 15px !important;
    }
    /* توحيد لون كل النصوص لتكون واضحة جداً */
    h1, h2, h3, h4, p, span, div {
        color: #002147 !important; /* أزرق غامق جداً يقترب للأسود */
    }
    /* تنسيق خاص للتاريخ */
    .date-style {
        background-color: #1E3A8A;
        color: white !important;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. عرض الشعار
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 4. اختيار المرحلة
stages_options = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Please select your grade:", stages_options)

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
                    # التاريخ والاسم
                    subject_name = row.iloc[0]
                    upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                    
                    # عرض التاريخ بشكل مميز داخل "كبسولة" زرقاء
                    st.markdown(f"<span class='date-style'>📅 {upload_date}</span> — <b style='font-size:18px;'>{subject_name}</b>", unsafe_allow_html=True)
                    
                    # الدروس والواجبات بلون أسود صريح للقراءة السهلة
                    st.markdown(f"<p style='color:black;'><b>📖 Lesson:</b> {row.iloc[1]}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color:black;'><b>📝 Homework:</b> {row.iloc[2]}</p>", unsafe_allow_html=True)
                    
                    if len(row) > 3 and pd.notna(row.iloc[3]):
                        st.markdown(f"<p style='color:green;'><b>💡 Notes:</b> {row.iloc[3]}</p>", unsafe_allow_html=True)
        else:
            st.warning("No data found.")
    except:
        st.error("Connection error.")

# 5. حقوق الملكية (مستر كريم مجدي)
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
