import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫", layout="centered")

# --- 🎨 كود CSS المطور (للعرض والطباعة) ---
st.markdown("""
    <style>
    /* 1. تنسيق العناوين والمربعات في الموقع */
    .stSelectbox label p, .stTextInput label p {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #1E3A8A !important;
    }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: #F8FAFC !important;
        border: 2px solid #1E3A8A !important;
        border-radius: 12px !important;
    }

    /* 2. سحر التنسيق عند الطباعة (Print Mode) */
    @media print {
        /* إخفاء العناصر غير الضرورية في الورقة */
        header, .stSelectbox, .stTextInput, .stDivider, [data-testid="stSidebar"], button {
            display: none !important;
        }
        /* جعل الصفحة بعرض الورقة بالكامل */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
        }
        /* إجبار المربعات (Expanders) على الظهور مفتوحة في الطباعة */
        .streamlit-expanderContent {
            display: block !important;
            height: auto !important;
            visibility: visible !important;
        }
        .streamlit-expanderHeader {
            background-color: #eee !important;
            color: black !important;
            border: 1px solid #ccc !important;
        }
        /* تنسيق النصوص لتكون واضحة في الحبر الأسود */
        h1, h3, p, span {
            color: black !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الشعار والعناوين (ستختفي في الطباعة)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try: st.image("logo.png", use_container_width=True)
    except: pass

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Weekly Follow-up</h3>", unsafe_allow_html=True)
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
    
    # زرار تعليمي لولي الأمر
    st.info("💡 للطباعة: اضغط (Ctrl + P) من الكمبيوتر، أو اختار 'Print' من متصفح الموبايل.")

    sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_map[stage]}&v={random.randint(1,999999)}"
        df = pd.read_csv(url, dtype=str)
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
                    # تنسيق العرض
                    header_text = f"📘 {u_date} | {sub_name.upper()}"
                    with st.expander(header_text, expanded=True):
                        st.markdown(f"### {sub_name.upper()}")
                        st.markdown(f"**📖 Lesson:** {lesson}")
                        st.markdown(f"**📝 Homework:** {h_work}")
                        if notes and notes.lower() != "nan" and notes.strip() != "":
                            st.warning(f"💡 {notes}")
        else:
            st.warning("No data found.")
    except Exception as e:
        st.error("Error loading data!")

# 4. التذييل
st.divider()
st.markdown("<div style='text-align: center; color: #1E3A8A;'><b>Copyright © 2026: Mr. Kareem Magdy</b></div>", unsafe_allow_html=True)
