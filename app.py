import streamlit as st
import pandas as pd
import random

# 1. إعداد الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. عرض الشعار في المنتصف (بدون أخطاء)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except Exception as e:
        st.write(" ") # لو الصورة مش موجودة يسيب مساحة فاضية بدل الخطأ

# 3. العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)

st.divider()

# 4. قائمة المراحل ورابط الشيت
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select Grade / اختر المرحلة الدراسية:", stages)

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"

# 5. جلب البيانات وعرضها
try:
    # إضافة رقم عشوائي لتحديث البيانات فوراً
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
    df = pd.read_csv(url)
    
    if not df.empty:
        for index, row in df.iterrows():
            with st.container(border=True):
                # عرض المادة
                st.subheader(f"📖 {row.iloc[0]}")
                # المنهج
                st.info(f"**Lesson:** {row.iloc[1]}")
                # الواجب
                st.warning(f"**Homework:** {row.iloc[2]}")
                # الملاحظات (العمود الرابع)
                if len(row) > 3 and pd.notna(row.iloc[3]):
                    st.success(f"**Notes:** {row.iloc[3]}")
    else:
        st.info("No data available yet. / لا توجد بيانات حالياً.")

except Exception as e:
    st.error(f"Please check sheet name: {stage}. (Make sure it matches exactly in Google Sheets)")
