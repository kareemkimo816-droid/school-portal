import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 1. قاموس الـ GID (استبدل الأرقام دي بالأرقام الحقيقية من رابط الشيت عندك)
# افتح كل Tab في المتصفح وانسخ الرقم اللي بعد gid= في الرابط فوق
gid_map = {
    "kg1": "0",          # غالباً أول صفحة بتكون 0
    "kg2": "12345678",   # غير الرقم ده للرقم الحقيقي لصفحة kg2
    "Grade1": "98765432", # وهكذا لبقية المراحل
    "Grade2": "11223344",
    # أضف بقية المراحل هنا بنفس الطريقة
}

# 2. الشعار والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.divider()

# 3. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة"] + list(gid_map.keys())
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    selected_gid = gid_map[stage]
    
    try:
        # الرابط السحري: نستخدم GID مع طلب التصدير لضمان (الفصل + ظهور كل البيانات)
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={selected_gid}&v={random.randint(1,999999)}"
        
        df = pd.read_csv(url, dtype=str)
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            df_display = df.iloc[::-1]
            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.write(f"**📖 Lesson:** {lesson}")
                    st.write(f"**📝 Homework:** {h_work}")
        else:
            st.warning("No data found.")
    except Exception as e:
        st.error("Error connecting to Google Sheets.")

st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
