import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫", layout="centered")

# 2. الشعار والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: 
        st.image("logo.png", use_container_width=True)
    except: 
        pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
st.divider()

# 3. قاموس الـ GID اللي حضرتك بعته
gid_map = {
    "kg1": "0",
    "kg2": "559030275",
    "Grade1": "1142208249",
    "Grade2": "194133386",
    "Grade3": "100632757",
    "Grade4": "1689139431",
    "Grade5": "285063318",
    "Grade6": "11126465",
    "Grade7": "1536369128",
    "Grade8": "1668133231",
    "Grade9": "1978952219",
    "Grade10": "239983167",
    "Grade11": "70337667"
}

# 4. اختيار المرحلة
stages = ["Choose Grade / اختر المرحلة"] + list(gid_map.keys())
stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", stages)

if stage != "Choose Grade / اختر المرحلة":
    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    selected_gid = gid_map[stage]
    
    try:
        # الرابط السحري اللي بيسحب الصفحة كاملة بناءً على الـ GID
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={selected_gid}&v={random.randint(1,999999)}"
        
        # قراءة البيانات
        df = pd.read_csv(url, dtype=str)

        # تنظيف: استبعاد الصفوف الفارغة في أول عمود (المادة)
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            # ترتيب عكسي: الأحدث فوق والقديم تحت
            df_display = df.iloc[::-1]

            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                with st.expander(f"📅 {u_date}  ⬅️  {sub_name}", expanded=True):
                    st.markdown(f"**📖 Lesson:** {lesson}")
                    st.markdown(f"**📝 Homework:** {h_work}")
                    if notes and notes.lower() != "nan" and notes.strip() != "":
                        st.info(f"**💡 Notes:** {notes}")
        else:
            st.warning(f"No data found for {stage} / لا توجد بيانات لهذه المرحلة حالياً")
            
    except Exception as e:
        st.error("Connection Error! برجاء التأكد من اتصال الإنترنت أو صلاحيات الشيت.")

# 5. التذييل
st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
