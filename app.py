import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫", layout="centered")

# --- 🎨 كود التنسيق المطور (إطارات كحلي + خطوط واضحة) ---
st.markdown("""
    <style>
    /* تنسيق شريط الأخبار */
    .announcement-bar {
        background-color: #FFEB3B; 
        padding: 12px;
        border-radius: 10px;
        border-right: 8px solid #1E3A8A;
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        font-size: 19px;
        margin-bottom: 25px;
        direction: rtl;
    }
    /* تكبير وتلوين العناوين فوق المربعات */
    .stSelectbox label p, .stTextInput label p {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #1E3A8A !important;
    }
    /* 🔹 تمييز مربعات الاختيار والبحث بإطار أزرق غامق 🔹 */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: #F8FAFC !important;
        border: 3px solid #1E3A8A !important; /* إطار أزرق غامق وسميك */
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ⚡ دالة ذكية لتحديد الإيموجي واللون لكل مادة ---
def get_subject_style(subject):
    sub = subject.lower()
    if "arabic" in sub or "عربي" in sub: return "📜", "#059669"
    elif "english" in sub or "انجليزي" in sub: return "🔤", "#2563EB"
    elif "math" in sub or "ماث" in sub or "رياضيات" in sub: return "🔢", "#DC2626"
    elif "science" in sub or "ساينس" in sub or "علوم" in sub: return "🧪", "#7C3AED"
    elif "social" in sub or "دراسات" in sub: return "🌍", "#92400E"
    elif "religion" in sub or "دين" in sub: return "🕌", "#047857"
    elif "computer" in sub or "حاسب" in sub or "ict" in sub: return "💻", "#475569"
    elif "art" in sub or "رسم" in sub: return "🎨", "#DB2777"
    elif "french" in sub or "فرنساوي" in sub: return "🗼", "#1E3A8A"
    else: return "📚", "#1E3A8A"

# --- 📣 سحب الخبر من جوجل شيت (خانة F1 في شيت kg1) ---
@st.cache_data(ttl=60)
def load_sheet_data(url):
    return pd.read_csv(url, dtype=str)

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
news_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0"

try:
    news_df = load_sheet_data(news_url)
    school_news = news_df.columns[5] if len(news_df.columns) > 5 else None
    if school_news and "Unnamed" not in school_news:
        st.markdown(f'<div class="announcement-bar">📢 {school_news}</div>', unsafe_allow_html=True)
except:
    pass

# 2. الشعار والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0px;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; margin-top: 0px;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
st.divider()

# 3. القاموس واختيار المرحلة
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
                    # جلب التنسيق والإيموجي
                    emoji, color = get_subject_style(sub_name)
                    
                    header_text = f"{emoji} {u_date}  |  **{sub_name.upper()}**"
                    with st.expander(header_text, expanded=True):
                        # بانر داخلي ملون باسم المادة والايومجي
                        st.markdown(f"""
                            <div style="background-color:{color}; padding:8px; border-radius:5px; margin-bottom:15px;">
                                <h3 style="color:white; text
