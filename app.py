import streamlit as st
import pandas as pd
import random

# إعداد الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# عرض الشعار في المنتصف
# --- كود وضع الشعار في المنتصف بالضبط ---
col1, col2, col3 = st.columns([1, 1, 1]) # تقسيم الشاشة لـ 3 أجزاء متساوية
with col2: # وضع الصورة في الجزء الأوسط
    try:
        st.image("logo.png", use_container_width=True) 
    except:
        pass
# ---------------------------------------
        # هنا الكود بينادي على الصورة اللي إنت رفعتها
        st.image("logo.png", width=150)
    except:
        st.write("Logo loading...")

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)

st.divider()

# قائمة المراحل
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select Grade / اختر المرحلة الدراسية:", stages)

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"

try:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
    df = pd.read_csv(url)
    
    if not df.empty:
        for index, row in df.iterrows():
            with st.container(border=True):
                st.subheader(f"📖 {row.iloc[0]}")
                st.info(f"**Lesson:** {row.iloc[1]}")
                st.warning(f"**Homework:** {row.iloc[2]}")
                if len(row) > 3 and pd.notna(row.iloc[3]):
                    st.success(f"**Notes:** {row.iloc[3]}")
    else:
        st.info("No data available yet. / لا توجد بيانات حالياً.")
except:
    st.error(f"Please check sheet name: {stage}")
