import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="First Language School", page_icon="🏫", layout="wide")

# الهيدر والشعار (تقدر تغير رابط الصورة بلوجو مدرستك)
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏫 First Language School - Giza</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>متابعة المنهج الأسبوعي والواجبات</p>", unsafe_allow_html=True)

# رابط الشيت بتاعك اللي بعتهولي (بصيغة التصدير)
sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid="

# قائمة المراحل (تأكد إنها نفس أسماء التبويبات عندك)
stages = {
    "Prep 2": "0",  # الرقم ده (gid) بيتغير لكل تبويب، هعرفك تجيبه إزاي
    "KG 1": "12345", 
}

# اختيار المرحلة
selected_stage = st.selectbox("اختر المرحلة الدراسية للطالب:", list(stages.keys()))

# قراءة البيانات وعرضها
try:
    # هنا الكود بيروح يقرأ من جوجل شيت فوراً
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={selected_stage}")
    
    st.divider()
    
    # عرض البيانات في شكل بطاقات (Cards)
    cols = st.columns(3) # عرض 3 مواد في كل صف
    for index, row in df.iterrows():
        with cols[index % 3]:
            with st.container(border=True):
                st.subheader(f"📖 {row['المادة']}")
                st.info(f"**المنهج:** {row['ما تم دراسته']}")
                st.warning(f"**الواجب:** {row['الواجب']}")
                if 'ملاحظات' in row:
                    st.write(f"📝 {row['ملاحظات']}")
except:
    st.error("جاري تجهيز بيانات هذه المرحلة.. فضلاً اختر مرحلة أخرى.")
