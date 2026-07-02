import streamlit as st

# إعدادات الصفحة الكاملة للمتحف
st.set_page_config(
    page_title="المتحف المصري الكبير - الجولة الرقمية",
    page_icon="🏛️",
    layout="wide"
)

# تصميم الألوان الفرعونية الملكية (الوضع الملوكي)
st.markdown("""
    <style>
    .stApp {
        background-color: #0A0A0A !important;
    }
    h1, h2 {
        color: #FFD700 !important;
        text-align: center;
        font-family: 'Cairo', sans-serif;
        text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.4);
    }
    .museum-card {
        background: rgba(20, 20, 20, 0.9) !important;
        border: 1px solid #FFD700 !important;
        border-radius: 15px;
        padding: 20px;
        margin-top: 15px;
        color: #F5F5F5 !important;
    }
    .spec-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    .spec-table td {
        padding: 8px;
        border-bottom: 1px solid #333;
    }
    .spec-label {
        color: #FFD700;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏛️ محاكاة جولة المتحف المصري الكبير 3D</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #AAA;'>مرحباً بك في البهو العظيم وقاعات العرض. حرك التماثيل بلمسة من شاشتك لاستكشاف تفاصيلها الحجرية.</p>", unsafe_allow_html=True)

# تقسيم قاعات المتحف (هنا تعريف المتغير عشان ما يديش NameError)
قاعات_المتحف = st.tabs(["🗿 البهو العظيم (رمسيس)", "👑 قاعة القناع الذهبي", "𓂀 تمثال أبو الهول الإهداي"])

# --- القاعة الأولى: تمثال رمسيس الثاني ---
with قاعات_المتحف[0]:
    st.markdown("<h2>🗿 تمثال الملك رمسيس الثاني الضخم</h2>")
    
    # الرابط الجديد المحدث لتمثال رمسيس الثاني لتفادي خطأ 404
    st.components.v1.html(
        """
        <iframe title="Ramesses II" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="450" src="https://sketchfab.com/models/19ebca33e8394e0996843477f72f2d90/embed?autostart=1&ui_controls=1&ui_infos=0&ui_watermark=0"></iframe>
        """,
        height=450
    )
    
    st.markdown("""
    <div class='museum-card'>
        <h3 style='color: #FFD700;'>📋 بطاقة بيانات الأثر</h3>
        <table class='spec-table'>
            <tr><td class='spec-label'>الحقبة الزمنية:</td><td>الدولة الحديثة - الأسرة التاسعة عشر (حوالي 1279–1213 ق.م)</td></tr>
            <tr><td class='spec-label'>مادة النحت:</td><td>الجرانيت الوردي الفاخر</td></tr>
            <tr><td class='spec-label'>الارتفاع الفعلي:</td><td>11 مترًا</td></tr>
            <tr><td class='spec-label'>الوزن:</td><td>83 طنًا</td></tr>
            <tr><td class='spec-label'>مكان الاكتشاف:</td><td>معبد ميت رهينة الكبير (منف)</td></tr>
        </table>
        <br>
        <p><b>الأسرار والنقوش:</b> يزين حزام الملك خنجرًا ذو مقبض ذهبي، ويظهر على كتفه الأيمن نقوش غائرة تحمل اسمه الملكي "وسر ماعت رع ستب إن رع". تم نقل هذا التمثال في موكب مهيب ليكون أول مستقبل لزوار المتحف الكبير.</p>
    </div>
    """, unsafe_allow_html=True)

# --- القاعة الثانية: قناع توت عنخ آمون ---
with قاعات_المتحف[1]:
    st.markdown("<h2>👑 قناع دفن الملك الذهبي توت عنخ آمون</h2>")
    
    st.components.v1.html(
        """
        <iframe title="Tutankhamun Mask" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="450" src="https://sketchfab.com/models/bf384358a9e046209b552de6eb0bc5db/embed?autostart=1&ui_controls=1&ui_infos=0&ui_watermark=0"></iframe>
        """,
        height=450
    )
    
    st.markdown("""
    <div class='museum-card'>
        <h3 style='color: #FFD700;'>📋 بطاقة بيانات الأثر</h3>
        <table class='spec-table'>
            <tr><td class='spec-label'>الحقبة الزمنية:</td><td>الأسرة الثامنة عشر (حوالي 1332–1323 ق.م)</td></tr>
            <tr><td class='spec-label'>مادة الصنع:</td><td>ذهب خالص مرصع بالأحجار الكريمة (اللازورد، العقيق، والزجاج الملون)</td></tr>
            <tr><td class='spec-label'>الوزن الإجمالي:</td><td>10.23 كيلوجرام من الذهب</td></tr>
            <tr><td class='spec-label'>الرمزية:</td><td>يمثل الوجه الآدمي للملك بهيئة المعبود أوزيريس لضمان البعث.</td></tr>
        </table>
        <br>
        <p><b>التفاصيل الطبية والفنية:</b> القناع يحمل ملامح شديدة الدقة للملك الشاب، وعلى ظهر القناع توجد نقوش هيروغليفية سحرية من كتاب الموتى (الفصل 151) لحماية جسد الملك في العالم الآخر.</p>
    </div>
    """, unsafe_allow_html=True)

# --- القاعة الثالثة: أبو الهول ---
with قاعات_المتحف[2]:
    st.markdown("<h2>𓂀 تمثال أبو الهول الصغير (Votive Sphinx)</h2>")
    
    st.components.v1.html(
        """
        <iframe title="The Sphinx" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="450" src="https://sketchfab.com/models/007421ae33704870b22ff7728dfc9861/embed?autostart=1&ui_controls=1&ui_infos=0&ui_watermark=0"></iframe>
        """,
        height=450
    )
    
    st.markdown("""
    <div class='museum-card'>
        <h3 style='color: #FFD700;'>📋 بطاقة بيانات الأثر</h3>
        <table class='spec-table'>
            <tr><td class='spec-label'>نوع الأثر:</td><td>تمثال إهدائي للمعبد لطلب البركة</td></tr>
            <tr><td class='spec-label'>المادة:</td><td>الحجر الجيري النقي</td></tr>
            <tr><td class='spec-label'>التصميم:</td><td>جسد أسد يرمز للقوة الجسدية، ورأس ملك يرمز للحكمة والعقل.</td></tr>
        </table>
        <br>
        <p><b>ملاحظة الجولة:</b> هذا النوع من التماثيل كان ينحت بدقة فائقة كقرابين توضع في المعابد الكبرى لإظهار الولاء، وتوضح تفاصيل النحت قوة التمكن من أدوات الحفر الحجرية.</p>
    </div>
    """, unsafe_allow_html=True)
