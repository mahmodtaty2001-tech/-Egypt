import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="🏛️ #ATegypT",
    page_icon="🇪🇬",
    layout="centered"
)

# الألوان الملكية: أسود فخم، ذهبي، وأزرق جعران
st.markdown("""
    <style>
    .stApp {
        background-color: #050505 !important;
    }
    h1 {
        color: #FFD700 !important;
        text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.5);
        text-align: center;
        font-family: 'Cairo', sans-serif;
    }
    .scarab-btn {
        background: linear-gradient(135deg, #00416A, #E4E5E6);
        background-color: #002f52 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 20px;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 4px 15px rgba(0, 65, 106, 0.6);
    }
    .ankh-card {
        background: rgba(20, 20, 20, 0.8) !important;
        border: 1px solid #FFD700 !important;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        color: #F5F5F5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية (البوصلة)
st.sidebar.image("https://img.icons8.com/color/96/ankh.png", width=60)
st.sidebar.markdown("<h2 style='color: #FFD700;'>☥ البوصلة الملكية</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["الرئيسية", "أسلوب الحياة", "أسرار الصناعة"])

# --- قسم الرئيسية ---
if menu == "الرئيسية":
    st.markdown("<h1>🏛️ عظمة التاريخ المصري</h1>", unsafe_allow_html=True)
    
    # صورة فوكاس للأهرامات
    st.image("https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=800&q=80", use_container_width=True)
    
    st.markdown("""
    <div class='ankh-card'>
        <h3 style='color: #FFD700; text-align: center;'>𓋹 العرش الرقمي</h3>
        <p style='text-align: center;'>مرحباً بك في بوابتك الفرعونية الفخمة. استخدم البوصلة الجانبية للتنقل بين الأقسام المصممة برموز أجدادنا.</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسلوب الحياة ---
elif menu == "أسلوب الحياة":
    st.markdown("<h1>🧥 أسلوب الحياة والملابس</h1>", unsafe_allow_html=True)
    
    # أيقونة الجعران الأزرق كعنوان للقسم
    st.markdown("<div class='scarab-btn'><h3 style='color: #FFD700; margin:0;'>𓆣 الجعران الملكي الأزرق</h3></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='ankh-card'>
        <h4 style='color: #FFD700;'>🌾 قماش الكتان الملكي</h4>
        <p>كان هو القماش الأساسي لسهولته ونقائه وقدرته العالية على التعامل مع درجات الحرارة.</p>
    </div>
    <div class='ankh-card'>
        <h4 style='color: #FFD700;'>👁️ عين حور وسحر الكحل</h4>
        <p>لم يكن مجرد زينة، بل تركيبات طبية دقيقة لحماية العيون من أشعة الشمس والأمراض.</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسرار الصناعة ---
elif menu == "أسرار الصناعة":
    st.markdown("<h1>🧪 أسرار الصناعة والفلك</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='ankh-card'>
        <h4 style='color: #FFD700;'>⚱️ سر التحنيط المقدّس</h4>
        <p>كيمياء طبية معقدة حيرت عقول العلماء عبر العصور، وما زالت تفاصيلها تُدهش العالم.</p>
    </div>
    <div class='ankh-card'>
        <h4 style='color: #FFD700;'>✨ الهندسة والفلك المعجز</h4>
        <p>بُنيت الأهرامات والمعابد بتوافق فلكي هندسي يتوازى بدقة متناهية مع حركة النجوم.</p>
    </div>
    """, unsafe_allow_html=True)
