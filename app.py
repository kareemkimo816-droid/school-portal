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

# 3. قاموس الـ GID (غير الأرقام دي بالأرقام اللي تظهر عندك في المتصفح لكل صفحة)
gid_map = {
    "kg1": "0",          # الرقم اللي بعد gid= في صفحة kg1
    "kg2": "559030275",    # الرقم اللي بعد gid= في صفحة kg2
    "Grade1": "1142208249", # الرقم اللي بعد gid= في صفحة Grade1
    "Grade2": "194133386", # وهكذا لباقي المراحل...
}

# 4. اختيار المرحلة
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", ["Choose Grade / اختر المرحلة"] + list(gid_map.keys()))

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    selected_gid = gid_map[stage]
    
    try:
        # الرابط السحري: استخدام GID مع التصدير المباشر لضمان (الفصل + ظهور 28/2)
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={selected_gid}&v={random.randint(1,999999)}"
        
        # قراءة البيانات بالكامل
        df = pd.read_csv(url, dtype=str)

        # تنظيف: استبعاد الصفوف الفارغة
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            # ترتيب عكسي: الأحدث فوق والقديم (28/2) تحت
            df_display = df.iloc[::-1]

            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {h_work}")
        else:
            st.warning(f"No data found for {stage}.")
    except Exception as e:
        st.error("Error connecting to Google Sheets. تأكد من أرقام الـ GID.")

st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
