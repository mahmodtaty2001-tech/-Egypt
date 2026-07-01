import streamlit as st

# إعداد واجهة البرنامج بشكل احترافي
st.set_page_config(page_title="#ATegypT", page_icon="🇪🇬", layout="centered")

# إضافة شوية ستايل عشان الشكل يبان "شيك"
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #d4af37; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("🏛️ #ATegypT")
st.subheader("بوابتك الرقمية لعظمة التاريخ المصري")

# وصف المشروع
st.info("""
**#ATegypT** هي منصة رائدة بتعيد إحياء التاريخ. 
إحنا مش بنعرض صور، إحنا بنحكي قصص الحضارة:
- أسلوب الحياة والملابس الفرعونية.
- أسرار الصناعة والفلك.
- التخطيط الهندسي اللي حير العالم.
""")

# إضافة أيقونة أو صورة (اختياري)
# st.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/King_Tut_Mask.jpg")

# منطقة التفاعل
if st.button("🚀 ابدأ الرحلة الاستكشافية الآن"):
    st.balloons()
    st.success("تم تفعيل البوابة الزمنية! انتظر التحديثات القادمة للـ 3D و الـ AI.")
    st.write("المشروع تحت التطوير المستمر.. خليك متابع!")

# تذييل الصفحة
st.markdown("---")
st.caption("صُنع بكل فخر من أجل مصر 🇪🇬 | #ATegypT Team")
