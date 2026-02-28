import streamlit as st
import pandas as pd

# إعداد الصفحة واسم التبويب في المتصفح
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("اختر المرحلة الدراسية:", stages)

try:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}"
    df = pd.read_csv(url)
    
    if not df.empty:
      if not df.empty:
        # الكود يعرض الأعمدة بالترتيب: 0=المادة، 1=المنهج، 2=الواجب، 3=الملاحظات
        for index, row in df.iterrows():
            with st.container(border=True):
                st.subheader(f"📖 {row.iloc[0]}") # العمود الأول
                st.info(f"**المنهج:** {row.iloc[1]}") # العمود الثاني
                st.warning(f"**الواجب:** {row.iloc[2]}") # العمود الثالث
                
                # إضافة خانة الملاحظات (العمود الرابع) إذا كانت موجودة
                if len(row) > 3:
                    st.success(f"**ملاحظات:** {row.iloc[3]}")
    else:
        st.info("لا توجد بيانات مسجلة في هذه المرحلة حتى الآن.")
except:
    st.error("تأكد أن اسم التبويب في الإكسيل مطابق لما اخترته (مثلاً Grade8)")
