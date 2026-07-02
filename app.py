import streamlit as st

st.set_page_config(page_title="المتحف المصري الكبير - جولة رقمية", layout="wide")

# تصميم القاعات
tabs = st.tabs(["🏛️ الدرج العظيم", "👑 قاعة توت عنخ آمون", "⚱️ مختبر الأسرار"])

with tabs[0]:
    st.header("الدرج العظيم")
    st.write("استكشف التماثيل الضخمة للملوك العظام.")
    # هنا هنربط ملف الـ 3D لاحقاً
    st.info("جاري تحميل النموذج ثلاثي الأبعاد لتمثال رمسيس الثاني...")

with tabs[1]:
    st.header("كنوز توت عنخ آمون")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/95/Tutankhamun_mask.jpg", caption="القناع الذهبي")
    with col2:
        st.write("### تفاصيل القناع")
        st.write("وزن القناع يتجاوز الـ 10 كيلو جرام من الذهب الخالص.")
        st.button("اكتشف أسرار الصناعة")

with tabs[2]:
    st.header("مختبر الأسرار")
    st.warning("هنا تكتشف أسرار كيمياء التحنيط والبرديات.")
