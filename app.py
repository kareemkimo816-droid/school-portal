import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. الشعار
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
        # إضافة رقم عشوائي ضخم لإجبار جوجل على إرسال أحدث نسخة من البيانات
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000000)}"
        
        # قراءة الشيت بالكامل بدون أي فلاتر
        df = pd.read_csv(url)

        # حذف الصفوف الفاضية تماماً فقط
        df = df.dropna(how='all')

        if not df.empty:
            # ترتيب عكسي (من أسفل الشيت لأعلاه)
            # عشان 1/3 (اللي تحت) تظهر هي الأولى فوق
            df_display = df.iloc[::-1]

            for index, row in df_display.iterrows():
                # قراءة الأعمدة بالترتيب A, B, C, D, E
                sub_name = str(row.iloc[0]) if pd.notna(row.iloc[0]) else "General"
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                # عرض كل "سطر" في الشيت كـ كارت مستقل تماماً
                # ده بيمنع تداخل البيانات أو اختفائها
                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {h_work}")
                    if notes and str(notes).lower() != "nan" and notes.strip() != "":
                        st.info(f"**💡 Notes:** {notes}")
        else:
            st.warning("No data found for this grade.")
    except Exception as e:
        st.error("Error! Please check your internet or sheet name.")

st.divider()
st.markdown("<div style='text-align: center;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
