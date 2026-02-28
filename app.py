import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. الشعار في المنتصف
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 3. العناوين الرئيسية
st.markdown("<h1 style='text-align: center;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 4. اختيار المرحلة (تركناها بتنسيق Streamlit الأصلي عشان السهم يشتغل)
stages = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage == "Choose Grade / اختر المرحلة":
    st.info("👋 Welcome! Please select a grade above.")
else:
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
        df = pd.read_csv(url)
        
        if not df.empty:
            for index, row in df.iterrows():
                # جلب البيانات
                subject_name = row.iloc[0]
                lesson = row.iloc[1]
                homework = row.iloc[2]
                notes = row.iloc[3] if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"

                # عرض البيانات باستخدام Expander (بيفتح ويقفل وشكله شيك جداً)
                # العنوان فيه التاريخ أولاً ثم السهم ثم المادة
                with st.expander(f"📅 {upload_date}  ⬅️  {subject_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {homework}")
                    if notes:
                        st.markdown(f"**💡 Notes:** {notes}")
        else:
            st.warning("No data found for this grade.")
    except:
        st.error("Connection error. Please refresh the page.")

# 5. حقوق الملكية (مستر كريم مجدي)
st.divider()
st.markdown("<div style='text-align: center;'><b>Copyright © 2026: Mr. Kareem Magdy</b><br>Fadl Modern Language School - All Rights Reserved</div>", unsafe_allow_html=True)
