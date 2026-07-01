import streamlit as st
from data import life_style, industry_secrets

st.set_page_config(page_title="#ATegypT", page_icon="🇪🇬")

menu = st.sidebar.radio("استكشف التاريخ:", ["الرئيسية", "أسلوب الحياة", "أسرار الصناعة"])

if menu == "الرئيسية":
    st.title("🏛️ #ATegypT")
    st.subheader("بوابتك الرقمية لعظمة التاريخ المصري")
    st.info("استخدم القائمة الجانبية للتنقل.")

elif menu == "أسلوب الحياة":
    st.header(life_style["title"])
    st.write(life_style["content"])

elif menu == "أسرار الصناعة":
    st.header(industry_secrets["title"])
    st.write(industry_secrets["content"])
