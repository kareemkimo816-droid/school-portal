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

if stage == "Choose Grade / اختر المرحلة":
    st.info("👋 Welcome! Please select a grade above.")
else:
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,10000)}"
        df = pd.read_csv(url)
        
        if not df.empty:
            # تنظيف البيانات والتأكد من وجود أسماء للمواد
            df.columns = ['Subject', 'Lesson', 'Homework', 'Notes', 'Date']
            df['Subject'] = df['Subject'].fillna('General')
            
            # الحصول على قائمة المواد الفريدة (مثل: Arabic, English, Math)
            unique_subjects = df['Subject'].unique()

            for sub in unique_subjects:
                # إنشاء "عنوان كبير" لكل مادة
                st.markdown(f"### 📘 {sub}")
                
                # جلب كل الصفوف الخاصة بهذه المادة فقط وعكسها (ليظهر الأحدث فوق)
                sub_data = df[df['Subject'] == sub].iloc[::-1]

                for index, row in sub_data.iterrows():
                    u_date = str(row['Date']) if pd.notna(row['Date']) else "No Date"
                    lesson = str(row['Lesson']) if pd.notna(row['Lesson']) else "---"
                    h_work = str(row['Homework']) if pd.notna(row['Homework']) else "---"
                    notes = str(row['Notes']) if pd.notna(row['Notes']) else ""

                    # عرض التواريخ داخل المادة في صناديق (Expander)
                    with st.expander(f"📅 {u_date}", expanded=False):
                        st.markdown(f"**📖 Lesson:** {lesson}")
                        st.markdown(f"**📝 Homework:** {h_work}")
                        if notes:
                            st.info(f"**💡 Notes:** {notes}")
                st.divider() # خط فاصل بين كل مادة والتانية
        else:
            st.warning("No data found.")
    except Exception as e:
        st.error("Error loading data. Please check your Sheet columns.")

# 4. الحقوق
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
