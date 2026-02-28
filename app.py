import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. الشعار والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.divider()

# 3. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة"] + ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        # جلب البيانات مع مانع التخزين المؤقت لضمان رؤية التعديلات فوراً
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,999999)}"
        
        # قراءة الشيت بالكامل وحذف الصفوف اللي مفيهاش مادة (العمود A)
        df = pd.read_csv(url)
        df = df[df.iloc[:, 0].notna()] 

        if not df.empty:
            # تنظيف أسماء المواد
            df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip()
            
            # الحصول على قائمة المواد الفريدة (عربي، دين، الخ)
            unique_subjects = df.iloc[:, 0].unique()

            for sub in unique_subjects:
                st.markdown(f"### 📘 {sub}")
                
                # جلب كل صفوف المادة دي (القديم والحديث)
                sub_data = df[df.iloc[:, 0] == sub]
                
                # ترتيب عكسي: يخلي آخر صف كتبته في الشيت يظهر هو الأول في الموقع
                sub_data_display = sub_data.iloc[::-1]

                for index, row in sub_data_display.iterrows():
                    # قراءة البيانات نصياً لضمان عدم الاختفاء
                    lesson = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                    h_work = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                    notes  = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                    u_date = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                    with st.expander(f"📅 {u_date}", expanded=True):
                        st.markdown(f"**📖 Lesson:** {lesson}")
                        st.markdown(f"**📝 Homework:** {h_work}")
                        if notes and str(notes).lower() != "nan" and notes.strip() != "":
                            st.info(f"**💡 Notes:** {notes}")
                st.markdown("---")
        else:
            st.warning("No data found for this grade.")
    except Exception as e:
        st.error("Connection error. Please refresh the page.")

st.divider()
st.markdown("<div style='text-align: center;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
