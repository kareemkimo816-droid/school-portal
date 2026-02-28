import streamlit as st
import pandas as pd

st.set_page_config(page_title="First Language School", page_icon="🏫")
st.title("🏫 First Language School - Giza")

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("اختر المرحلة الدراسية:", stages)

try:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}"
    df = pd.read_csv(url)
    
    if not df.empty:
        # الكود ده هيعرض أول 3 أعمدة بغض النظر عن أسمائهم إيه
        for index, row in df.iterrows():
            with st.container(border=True):
                st.subheader(f"📖 {row.iloc[0]}") # العمود الأول (المادة)
                st.info(f"**المنهج:** {row.iloc[1]}") # العمود الثاني
                st.warning(f"**الواجب:** {row.iloc[2]}") # العمود الثالث
    else:
        st.info("لا توجد بيانات مسجلة في هذه المرحلة حتى الآن.")
except:
    st.error("تأكد أن اسم التبويب في الإكسيل مطابق لما اخترته (مثلاً Grade8)")
