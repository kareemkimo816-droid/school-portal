import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود السيطرة الكاملة على الألوان (يجبر الموبايل على الوضوح)
st.markdown(
    """
    <style>
    /* 1. خلفية التطبيق */
    .stApp {
        background-color: #E3F2FD !important;
    }

    /* 2. إجبار قائمة الاختيار (Selectbox) على اللون الأبيض والخط الأسود */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 2px solid #1E3A8A !important;
    }
    
    /* 3. إجبار الكلام داخل القائمة المنسدلة على الوضوح */
    ul[role="listbox"] {
        background-color: white !important;
    }
    li[role="option"] {
        color: black !important;
        background-color: white !important;
    }

    /* 4. تنسيق مربعات المواد (Cards) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 15px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1) !important;
    }

    /* 5. توحيد لون الخطوط في الصفحة كلها للأسود أو الأزرق الغامق */
    h1, h4, label, p, span {
        color: #002147 !important;
    }
    
    /* 6. شكل التاريخ (الكبسولة الزرقاء) */
    .date-badge {
        background-color: #1E3A8A;
        color: white !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. الشعار
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 4. اختيار المرحلة (بإضافة ليبل واضح)
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
                    upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                    
                    # عرض البيانات بتنسيق عالي التباين (High Contrast)
                    st.markdown(f"<div class='date-badge'>📅 {upload_date}</div>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='color:#1E3A8A; margin-top:0;'>{subject_name}</h3>", unsafe_allow_html=True)
                    
                    st.markdown(f"<p style='color:black; font-size:16px;'><b>📖 Lesson:</b> {row.iloc[1]}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color:black; font-size:16px;'><b>📝 Homework:</b> {row.iloc[2]}</p>", unsafe_allow_html=True)
                    
                    if len(row) > 3 and pd.notna(row.iloc[3]):
                        st.markdown(f"<p style='color:#155724; background-color:#d4edda; padding:5px; border-radius:5px;'><b>💡 Notes:</b> {row.iloc[3]}</p>", unsafe_allow_html=True)
        else:
            st.warning("No data found.")
    except:
        st.error("Connection error. Please refresh.")

# 5. الحقوق (مستر كريم مجدي 2026)
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
