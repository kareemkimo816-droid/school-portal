import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة - وضعناها في البداية لضمان استقرار الواجهة
st.set_page_config(page_title="Fadl School", page_icon="🏫", layout="centered")

# 2. تنسيق بسيط جداً لا يتعارض مع القائمة المنسدلة
st.markdown(
    """
    <style>
    /* خلفية سماوية هادئة */
    .stApp { background-color: #E3F2FD; }
    
    /* توسيط العناوين */
    .text-center { text-align: center !important; color: #1E3A8A; }
    
    /* تنسيق الكروت (المواد) */
    .subject-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 15px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. الشعار (استخدام الطريقة التقليدية لضمان التوسيط)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 4. العناوين
st.markdown("<h1 class='text-center'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='text-center'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 5. اختيار المرحلة الدراسية (بدون أي CSS خارجي يلمسها)
stages = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]

# وضعنا القائمة داخل حاوية فارغة لضمان استقلالها
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
                # استخدام HTML بسيط داخل الكارد لضمان ظهور الألوان في الموبايل
                upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                subject = row.iloc[0]
                lesson = row.iloc[1]
                homework = row.iloc[2]
                notes = row.iloc[3] if len(row) > 3 and pd.notna(row.iloc[3]) else ""

                st.markdown(f"""
                <div class="subject-card">
                    <span style="color:#1E3A8A; font-weight:bold;">📅 {upload_date}</span>
                    <h3 style="color:#1E3A8A; margin:5px 0;">{subject}</h3>
                    <p style="color:black; margin:5px 0;"><b>📖 Lesson:</b> {lesson}</p>
                    <p style="color:black; margin:5px 0;"><b>📝 Homework:</b> {homework}</p>
                    <p style="color:green; margin:5px 0;">{f'<b>💡 Notes:</b> {notes}' if notes else ''}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No data found.")
    except:
        st.error("Error connecting to data.")

# 6. الحقوق (مستر كريم مجدي)
st.divider()
st.markdown("<p class='text-center'><b>Copyright © 2026: Mr. Kareem Magdy</b><br>Fadl Modern Language School</p>", unsafe_allow_html=True)
