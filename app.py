import streamlit as st
# بنستدعي البيانات من ملف data.py اللي عملناه
from data import life_style, industry_secrets 

# إعداد واجهة البرنامج
st.set_page_config(page_title="#ATegypT", page_icon="🇪🇬", layout="centered")

# الستايل
st.markdown("""
    <style>
    .stButton>button { background-color: #d4af37; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية
menu = st.sidebar.radio("استكشف التاريخ:", ["الرئيسية", "أسلوب الحياة", "أسرار الصناعة"])

# عرض الصفحات
if menu == "الرئيسية":
    st.title("🏛️ #ATegypT")
    st.subheader("بوابتك الرقمية لعظمة التاريخ المصري")
    st.info("اختر قسماً من القائمة الجانبية لتبدأ رحلتك.")

elif menu == "أسلوب الحياة":
    st.header(life_style["title"])
    st.write(life_style["content"])

elif menu == "أسرار الصناعة":
    st.header(industry_secrets["title"])
    st.write(industry_secrets["content"])

# تذييل الصفحة
st.sidebar.markdown("---")
st.sidebar.caption("صُنع بكل فخر من أجل مصر 🇪🇬")
