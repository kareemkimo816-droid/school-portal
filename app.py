import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. الشعار (Logo)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 3. العناوين (Weekly Follow-up)
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
st.divider()

# 4. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة", "kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        # --- التعديل السحري هنا لفصل المراحل ---
        # نستخدم رابط gviz مع تحديد اسم الـ sheet بدقة لضمان عدم تداخل البيانات
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,999999)}"
        
        # قراءة البيانات
        df = pd.read_csv(url)

        # تنظيف: حذف الصفوف اللي مفيهاش اسم مادة (العمود A)
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            # ترتيب عكسي: الأحدث في الشيت يظهر هو الأول في الموقع
            # ده بيضمن إن 1/3 تظهر فوق و 28/2 تظهر تحتها دايماً في نفس الصفحة
            df_display = df.iloc[::-1]

            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                # عرض كل سطر (تاريخ) في كارت مستقل
                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {h_work}")
                    if notes and str(notes).lower() != "nan" and notes.strip() != "":
                        st.info(f"**💡 Notes:** {notes}")
        else:
            st.warning(f"No data found for {stage}. تأكد من وجود بيانات في شيت {stage}.")
    except Exception as e:
        st.error(f"Error! تأكد من أن اسم التبويب في جوجل شيت هو '{stage}' بالظبط.")

st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
