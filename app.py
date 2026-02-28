import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. الشعار (Logo)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # تأكد إن ملف الصورة اسمه logo.png وموجود بجانب app.py
        st.image("logo.png", use_container_width=True)
    except:
        st.error("⚠️ Logo file (logo.png) not found!")

# 3. العناوين الرئيسية (Material Cover)
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Material Cover / المنهج المغطى</h3>", unsafe_allow_html=True)
st.divider()

# 4. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة", "kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        # الرابط الذكي لكسر الكاش وجلب كل الصفوف (القديم والجديد)
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,999999)}"
        
        df = pd.read_csv(url)

        # تنظيف: حذف الصفوف الفاضية تماماً
        df = df.dropna(how='all')
        # التأكد من وجود بيانات في العمود الأول (المادة)
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            # --- الحل السحري لظهور الكل ---
            # بنعرض الشيت بالعكس (آخر سطر كتبته يظهر فوق)
            # وبدون تجميع (عشان مادة ما تمسحش مادة)
            df_reversed = df.iloc[::-1]

            for index, row in df_reversed.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                # عرض كل سطر في كارت (Expander) مستقل
                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {h_work}")
                    if notes and str(notes).lower() != "nan" and notes.strip() != "":
                        st.info(f"**💡 Notes:** {notes}")
        else:
            st.warning("No data found for this grade.")
    except Exception as e:
        st.error("Error connecting to Google Sheets. Please refresh.")

st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
