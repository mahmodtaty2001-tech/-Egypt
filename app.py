import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="🏛️ #ATegypT",
    page_icon="🇪🇬",
    layout="centered"
)

# نظام الألوان الديناميكي (دارك ملوكي / لايت صحراوي متاحف)
st.markdown("""
    <style>
    /* الكود بيتعرف تلقائياً على وضع الجهاز */
    
    /* 1. الوضع الملوكي (Dark Mode) - أسود وجولد لامع */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #0B0B0B !important;
        }
        h1 {
            color: #FFD700 !important; /* جولد لامع */
            text-shadow: 0px 0px 8px rgba(255, 215, 0, 0.6);
            text-align: center;
            font-family: 'Cairo', sans-serif;
        }
        h2, h3 {
            color: #F5F5F5 !important;
            font-family: 'Cairo', sans-serif;
        }
        .card {
            background-color: #161616 !important;
            padding: 20px;
            border-radius: 12px;
            border-right: 5px solid #FFD700 !important; /* حافة جولد */
            box-shadow: 0 4px 15px rgba(255,215,0,0.1);
            margin-bottom: 15px;
            color: #E0E0E0 !important;
        }
        p {
            color: #CCCCCC !important;
        }
    }

    /* 2. الوضع الصحراوي (Light Mode) - رمال ومتاحف */
    @media (prefers-color-scheme: light) {
        .stApp {
            background-color: #F4E8C1 !important; /* لون الرمال الناعمة للمعابد */
        }
        h1 {
            color: #8B5A2B !important; /* بني فخاري فرعوني */
            text-align: center;
            font-family: 'Cairo', sans-serif;
        }
        h2, h3 {
            color: #3E2723 !important;
            font-family: 'Cairo', sans-serif;
        }
        .card {
            background-color: #FFFDF6 !important; /* أبيض دافئ كالحجر الجيري */
            padding: 20px;
            border-radius: 12px;
            border-right: 5px solid #CD853F !important; /* حافة بلون الحجر الرملي */
            box-shadow: 0 4px 10px rgba(139,90,43,0.1);
            margin-bottom: 15px;
            color: #4E342E !important;
        }
        p {
            color: #5D4037 !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية
st.sidebar.markdown("<h2 style='text-align: center;'>🧭 البوصلة</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["🏛️ الرئيسية", "🧥 أسلوب الحياة", "🧪 أسرار الصناعة"])

# --- قسم الرئيسية ---
if menu == "🏛️ الرئيسية":
    st.markdown("<h1>🏛️ عظمة التاريخ المصري #ATegypT</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=800&q=80", caption="أهرامات الجيزة الخالدة")
    
    st.markdown("""
    <div class='card'>
        <h3>مرحباً بك في بوابتك الرقمية</h3>
        <p>هنا نرفع الستار عن أسرار وتفاصيل الحضارة الأقدم في التاريخ. استخدم القائمة الجانبية لتبدأ رحلتك الاستكشافية.</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسلوب الحياة ---
elif menu == "🧥 أسلوب الحياة":
    st.markdown("<h1>🧥 أسلوب الحياة والملابس الفرعونية</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>🌾 قماش الكتان الملكي</h3>
        <p>كان هو القماش الأساسي لسهولته ونقائه وقدرته العالية على التعامل مع درجات الحرارة في مصر.</p>
    </div>
    <div class='card'>
        <h3>👁️ سحر الكحل الفرعوني</h3>
        <p>لم يكن مجرد زينة للمظهر، بل كان تركيبة طبية تحمي العيون من أشعة الشمس الحارقة والأمراض.</p>
    </div>
    <div class='card'>
        <h3>🧼 هوس النظافة والنظام</h3>
        <p>كان المصري القديم مثالاً يُحتذى به في الطهارة؛ حيث كانت الاستحمام والزيوت العطرية جزءاً أساسياً من يومه.</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم أسرار الصناعة ---
elif menu == "🧪 أسرار الصناعة":
    st.markdown("<h1>🧪 أسرار الصناعة والفلك</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>⚱️ سر التحنيط المقدّس</h3>
        <p>كيمياء طبية معقدة حيرت عقول العلماء عبر العصور، وما زالت تفاصيلها تُدهش العالم حتى اليوم.</p>
    </div>
    <div class='card'>
        <h3>✨ الهندسة والفلك</h3>
        <p>بُنيت الأهرامات والمعابد بتوافق فلكي هندسي معقد ومعجز، يتوازى بدقة متناهية مع حركة النجوم والملوك.</p>
    </div>
    <div class='card'>
        <h3>📜 اختراع ورق البردي</h3>
        <p>المصريون هم أول من وثقوا التاريخ وصنعوا ثورة المعرفة عبر اختراع ورق البردي كأول وسيلة تدوين متينة.</p>
    </div>
    """, unsafe_allow_html=True)
