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
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
st.divider()

# 3. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة", "kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        # التعديل النهائي: طلب البيانات كـ CSV مع تحديد نطاق واسع جداً A1:E100
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&range=A1:E100&v={random.randint(1,999999)}"
        
        # قراءة البيانات وإجبار البرنامج على اعتبار كل شيء نص (String)
        df = pd.read_csv(url, dtype=str)

        # أهم خطوة: تنظيف أي صفوف فاضية تماماً والتركيز على الصفوف اللي فيها "تاريخ" أو "مادة"
        df = df[df.iloc[:, 0].notna() | df.iloc[:, 4].notna()].copy()

        if not df.empty:
            # عرض البيانات بالترتيب العكسي (الأحدث فوق)
            # ده هيخلي 5/3 و 1/3 يظهروا وبعدهم 28/2 وكل اللي تحتهم
            df_display = df.iloc[::-1]

            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else "General"
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "---"

                # إذا كان السطر فيه أي معلومة، اعرضه
                if sub_name != "nan" or u_date != "---":
                    with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                        st.markdown(f"**📖 Lesson:** {lesson}")
                        st.markdown(f"**📝 Homework:** {h_work}")
                        if notes and notes.lower() != "nan" and notes.strip() != "":
                            st.info(f"**💡 Notes:** {notes}")
        else:
            st.warning(f"No data found for {stage}.")
    except Exception as e:
        st.error("تأكد من أن البيانات مكتوبة بشكل صحيح في الشيت.")

st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
