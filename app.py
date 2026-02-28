import streamlit as st
import pandas as pd
import random

# إعداد الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# العنوان
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏫 Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)

st.divider()

# تأكد أن هذه الأسماء هي نفس أسماء الشيتات عندك تحت في الإكسيل
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select Grade / اختر المرحلة الدراسية:", stages)

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"

try:
    # إضافة رقم عشوائي للرابط لإجبار الموقع على تحديث البيانات (Cache Busting)
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
    df = pd.read_csv(url)
    
    if not df.empty:
        for index, row in df.iterrows():
            with st.container(border=True):
                # عرض المادة (العمود الأول)
                st.subheader(f"📖 {row.iloc[0]}")
                # المنهج (العمود الثاني)
                st.info(f"**Lesson:** {row.iloc[1]}")
                # الواجب (العمود الثالث)
                st.warning(f"**Homework:** {row.iloc[2]}")
                # الملاحظات (العمود الرابع إذا وجد)
                if len(row) > 3 and pd.notna(row.iloc[3]):
                    st.success(f"**Notes:** {row.iloc[3]}")
    else:
        st.info("No data available for this grade yet. / لا توجد بيانات مسجلة حالياً.")

except Exception as e:
    st.error(f"Please make sure the sheet name '{stage}' exists in your Google Sheets.")
