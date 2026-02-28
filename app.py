import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫", layout="centered")

# 2. تنسيق الألوان والخلفية (CSS)
st.markdown(
    """
    <style>
    /* لون الخلفية السماوي */
    .stApp {
        background-color: #E3F2FD;
    }
    /* تنسيق العناوين */
    h1, h4 {
        color: #1E3A8A !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    /* تنسيق حاوية المواد */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. عرض الشعار في المنتصف بالضبط
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.write(" ") # مساحة فارغة في حال عدم وجود الصورة

# 4. العناوين الرئيسية
st.markdown("<h1>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)
st.divider()

# 5. اختيار المرحلة الدراسية
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select Grade / اختر المرحلة الدراسية:", stages)

# رابط الشيت الخاص بك
sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"

# 6. جلب البيانات وعرضها (التاريخ أولاً ثم المادة)
try:
    # إضافة رقم عشوائي لمنع التخزين المؤقت (Cache) وتحديث البيانات فوراً
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
    df = pd.read_csv(url)
    
    if not df.empty:
        for index, row in df.iterrows():
            with st.container(border=True):
                # قراءة البيانات من الأعمدة
                subject_name = row.iloc[0]
                # نفترض أن التاريخ في العمود الخامس (الترتيب رقم 4 في البرمجة)
                upload_date = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else "2026-02-28"
                
                # عرض التاريخ في البداية بخط واضح
                st.markdown(f"📅 **{upload_date}** — <span style='color: #1E3A8A; font-size: 18px; font-weight: bold;'>{subject_name}</span>", unsafe_allow_html=True)
                
                # تفاصيل المادة
                st.info(f"**Lesson:** {row.iloc[1]}")
                st.warning(f"**Homework:** {row.iloc[2]}")
                
                # ملاحظات إضافية (العمود الرابع)
                if len(row) > 3 and pd.notna(row.iloc[3]):
                    st.success(f"**Notes:** {row.iloc[3]}")
    else:
        st.info("No data available yet for this grade.")

except Exception as e:
    st.error(f"Error loading data. Please check sheet name: {stage}")

# 7. حقوق الملكية بالإنجليزية (مستر كريم مجدي)
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #1E3A8A; padding: 20px; line-height: 1.6;'>
        <p style='font-size: 16px; font-weight: bold; margin-bottom: 5px;'>
            Copyright © 2026: Mr. Kareem Magdy
        </p>
        <p style='font-size: 14px; opacity: 0.8;'>
            Fadl Modern Language School - All Rights Reserved
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
