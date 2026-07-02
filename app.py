import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="🏛️ #ATegypT",
    page_icon="🇪🇬",
    layout="centered"
)

# التصميم الفرعوني الأسطوري بالـ CSS
st.markdown("""
    <style>
    /* خلفية الموقع كاملة بصورة الأهرامات فوكاس ناعم */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://images.unsplash.com/photo-1600577916048-804c9191e36c?auto=format&fit=crop&w=1200&q=80') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* القائمة الجانبية - ثيم مفتاح الحياة الذهبي */
    [data-testid="stSidebar"] {
        background: linear-gradient(rgba(11, 11, 11, 0.95), rgba(27, 20, 10, 0.95)),
                    url('https://img.icons8.com/ios-filled/100/ffffff/ankh.png') no-repeat bottom right;
        background-size: 40%;
        border-left: 2px solid #FFD700;
    }
    
    /* العناوين الرئيسية بالجولد اللامع */
    h1 {
        color: #FFD700 !important;
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.8);
        text-align: center;
        font-family: 'Cairo', sans-serif;
        font-weight: bold;
    }
    
    /* كروت المعلومات الزجاجية الشفافة (Glassmorphism) */
    .royal-card {
        background: rgba(22, 22, 22, 0.75) !important;
        backdrop-filter: blur(5px);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-right: 6px solid #FFD700 !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
        color: #F5F5F5 !important;
    }
    
    /* أزرار الراديو على شكل تصميم الجعران الأزرق الملكي */
    div Rigth-aligned [role="radiogroup"] label {
        background: linear-gradient(135deg, #005C97, #363795) !important; /* أزرق جعران ملكي */
        color: #FFD700 !important; /* كتابة جولد */
        border: 1px solid #FFD700 !important;
        padding: 12px 20px !important;
        border-radius: 30px !important; /* شكل بيضاوي كالجعران */
        margin-bottom: 10px !important;
        box-shadow: 0px 4px 10px rgba(0, 92, 151, 0.5) !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية مع أيقونة مفتاح الحياة
st.sidebar.markdown("<h1 style='font-size: 24px;'>☥ البوصلة الملكية</h1>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["𓉴 الرئيسية", "𓋹 أسلوب الحياة", "𓆗 أسرار الصناعة"])

# --- قسم الرئيسية ---
if menu == "𓉴 الرئيسية":
    st.markdown("<h1>𓉴 عظمة التاريخ المصري #ATegypT</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='royal-card'>
        <h3 style='color: #FFD700;'>𓋹 مرحباً بك في العرش الرقمي</h3>
        <p>هنا نرفع الستار عن أسرار وتفاصيل الحضارة الأقدم في التاريخ. افتح القائمة الجانبية (البوصلة) المصممة بنقش مفتاح الحياة لتتنقل بين الحكايات بأزرار الجعران المقدس.</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسلوب الحياة ---
elif menu == "𓋹 أسلوب الحياة":
    st.markdown("<h1>𓋹 أسلوب الحياة والملابس الفرعونية</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='royal-card'>
        <h3 style='color: #FFD700;'>🌾 قماش الكتان الملكي</h3>
        <p>كان هو القماش الأساسي لسهولته ونقائه وقدرته العالية على التعامل مع درجات الحرارة في مصر.</p>
    </div>
    <div class='royal-card'>
        <h3 style='color: #FFD700;'>👁️ سحر الكحل الفرعوني</h3>
        <p>لم يكن مجرد زينة للمظهر، بل كان تركيبة طبية تحمي العيون من أشعة الشمس الحارقة والأمراض.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسرار الصناعة ---
elif menu == "𓆗 أسرار الصناعة":
    st.markdown("<h1>𓆗 أسرار الصناعة والفلك</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='royal-card'>
        <h3 style='color: #FFD700;'>⚱️ سر التحنيط المقدّس</h3>
        <p>كيمياء طبية معقدة حيرت عقول العلماء عبر العصور، وما زالت تفاصيلها تُدهش العالم حتى اليوم.</p>
    </div>
    <div class='royal-card'>
        <h3 style='color: #FFD700;'>✨ الهندسة والفلك</h3>
        <p>بُنيت الأهرامات والمعابد بتوافق فلكي هندسي معقد ومعجز، يتوازى بدقة متناهية مع حركة النجوم.</p>
    </div>
    """, unsafe_allow_html=True)
