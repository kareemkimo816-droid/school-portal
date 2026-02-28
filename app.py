import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫", layout="centered")

# --- ⚡ دالة سريعة لتحميل البيانات من جوجل شيت ---
@st.cache_data(ttl=60) # تحديث كل دقيقة واحدة لضمان سرعة ظهور الأخبار الجديدة
def load_sheet_data(url):
    return pd.read_csv(url, dtype=str)

# --- 🎨 تنسيق CSS لشريط الأخبار ---
st.markdown("""
    <style>
    .announcement-bar {
        background-color: #FFEB3B; 
        padding: 12px;
        border-radius: 10px;
        border-right: 8px solid #FBC02D;
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        font-size: 19px;
        margin-bottom: 25px;
        direction: rtl;
    }
    .stSelectbox label p, .stTextInput label p {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #1E3A8A !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 📣 سحب الخبر من جوجل شيت (من خانة معينة) ---
sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
# هنسحب أول شيت (kg1 مثلاً) عشان نجيب منها الخبر
news_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0"

try:
    news_df = load_sheet_data(news_url)
    # هيفترض إن الخبر مكتوب في العمود السادس (F) أول صف
    school_news = news_df.columns[5] if len(news_df.columns) > 5 else "مرحباً بكم في مدرسة فضل"
    
    if school_news and "Unnamed" not in school_news:
        st.markdown(f'<div class="announcement-bar">📢 {school_news}</div>', unsafe_allow_html=True)
except:
    pass # لو حصل مشكلة في سحب الخبر مبيظهرش حاجة عشان ميعطلش الموقع

# 2. الشعار والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0px;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; margin-top: 0px;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
st.divider()

# 3. اختيار المرحلة والبحث
gid_map = {
    "kg1": "0", "kg2": "559030275", "Grade1": "1142208249", "Grade2": "194133386",
    "Grade3": "100632757", "Grade4": "1689139431", "Grade5": "285063318",
    "Grade6": "11126465", "Grade7": "1536369128", "Grade8": "1668133231",
    "Grade9": "1978952219", "Grade10": "239983167", "Grade11": "70337667"
}

stage = st.selectbox("👇 Select Grade / اختر المرحلة الدراسية:", ["Choose Grade / اختر المرحلة"] + list(gid_map.keys()))

if stage != "Choose Grade / اختر المرحلة":
    search_query = st.text_input("🔍 Search Subject or Date / ابحث بالمادة أو التاريخ:", key="search_bar").strip().lower()
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_map[stage]}&v={random.randint(1,999999)}"
    try:
        df = load_sheet_data(url)
        df = df[df.iloc[:, 0].notna()].copy()

        if not df.empty:
            df_display = df.iloc[::-1]
            for index, row in df_display.iterrows():
                sub_name = str(row.iloc[0]).strip()
                lesson   = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "---"
                h_work   = str(row.iloc[2]) if pd.notna(row.iloc[2]) else "---"
                notes    = str(row.iloc[3]) if len(row) > 3 and pd.notna(row.iloc[3]) else ""
                u_date   = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else "No Date"

                if search_query in sub_name.lower() or search_query in u_date.lower():
                    header_text = f"📅 {u_date} | 📘 **{sub_name.upper()}**"
                    with st.expander(header_text, expanded=True):
                        st.markdown(f"**📖 Lesson:** {lesson}")
                        st.markdown(f"**📝 Homework:** {h_work}")
                        if notes and notes.lower() != "nan" and notes.strip() != "":
                            st.info(f"💡 **Notes:** {notes}")
    except Exception as e:
        st.error("Error loading data!")

# 4. التذييل
st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
