import streamlit as st
import pandas as pd
import random

# 1. إعداد الصفحة
st.set_page_config(page_title="Fadl Modern Language School", page_icon="🏫")

# 2. كود اللون السماوي بدون أي تداخلات أو خطوط بيضاء خلف الشعار
st.markdown(
    """
    <style>
    /* تغيير لون الخلفية للتطبيق بالكامل */
    .stApp {
        background-color: #E3F2FD;
    }
    /* إخفاء أي خلفيات بيضاء إضافية خلف العناصر الرئيسية */
    [data-testid="stHeader"], [data-testid="stHeader"] > div {
        background-color: rgba(0,0,0,0) !important;
    }
    /* التأكد من أن النصوص والعناوين تظهر بشكل واضح */
    h1, h4 {
        color: #1E3A8A !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. عرض الشعار في المنتصف
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        # عرض الشعار بدون أي إطار أو خلفية
        st.image("logo.png", use_container_width=True)
    except:
        pass

# 4. العنوان الرئيسي (تم توحيد الألوان للأزرق الغامق)
st.markdown("<h1 style='text-align: center;'>Fadl Modern Language School</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Weekly Academic Follow-up</h4>", unsafe_allow_html=True)

st.divider()

# 5. اختيار المرحلة ورابط الشيت
stages = ["kg1", "kg2", "Grade1", "Grade2", "Grade3", "Grade4", "Grade5", "Grade6", "Grade7", "Grade8", "Grade9", "Grade10", "Grade11"]
stage = st.selectbox("Select Grade / اختر المرحلة الدراسية:", stages)

sheet_id = "17r99YTRCCRWP3a9vI6SwKtnK60_ajpmWvs0TUJOqQ_U"

# 6. جلب البيانات وعرضها داخل حاويات منظمة
try:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={stage}&v={random.randint(1,1000)}"
    df = pd.read_csv(url)
    
    if not df.empty:
        for index, row in df.iterrows():
            # استخدام border=True لعمل إطار بسيط حول المادة لسهولة القراءة
            with st.container(border=True):
                st.subheader(f"📖 {row.iloc[0]}")
                st.info(f"**Lesson:** {row.iloc[1]}")
                st.warning(f"**Homework:** {row.iloc[2]}")
                if len(row) > 3 and pd.notna(row.iloc[3]):
                    st.success(f"**Notes:** {row.iloc[3]}")
    else:
        st.info("No data available yet. / لا توجد بيانات حالياً.")

except Exception as e:
    st.error(f"Please check sheet name: {stage}.")
