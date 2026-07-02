import streamlit as st

st.set_page_config(
    page_title="🏛️ #ATegypT",
    page_icon="🇪🇬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== Glassmorphism CSS ======================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0a, #1a0033);
        background-attachment: fixed;
    }
    
    /* Glassmorphism Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.4s ease;
    }
    
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-6px);
        border-color: #FFD700;
    }

    h1, h2, h3 {
        color: #FFD700 !important;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
    }

    .sidebar .css-1d391kg {
        background: rgba(10, 10, 20, 0.85) !important;
        backdrop-filter: blur(10px);
    }

    .gold-btn {
        background: linear-gradient(135deg, #FFD700, #FFAA00);
        color: black;
        font-weight: bold;
        border-radius: 50px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s;
    }
    .gold-btn:hover {
        transform: scale(1.08);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# ====================== Sidebar - القائمة الموسعة ======================
st.sidebar.image("https://img.icons8.com/color/96/ankh.png", width=70)
st.sidebar.markdown("<h2 style='color:#FFD700; text-align:center;'>☥ البوصلة الفرعونية</h2>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "اختر القسم",
    [
        "🏠 الرئيسية",
        "🧥 أسلوب الحياة",
        "🧪 أسرار الصناعة",
        "🛠️ خدماتنا",
        "🛠️ أدواتنا",
        "🏛️ معرض الصور",
        "📜 عن المشروع"
    ]
)

# ====================== Header ======================
st.markdown("""
<div style='text-align:center; padding:2rem 0; border-bottom:3px solid #FFD700; margin-bottom:2rem;'>
    <h1>🏛️ #ATegypT</h1>
    <p style='color:#ddd; font-size:1.3rem;'>عظمة مصر الخالدة في عالم رقمي</p>
</div>
""", unsafe_allow_html=True)

# ====================== الأقسام ======================
if menu == "🏠 الرئيسية":
    st.image("https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1400&q=80", use_container_width=True)
    
    st.markdown("""
    <div class='glass-card'>
        <h3 style='text-align:center;'>𓋹 مرحباً بك في بوابة الحضارة</h3>
        <p style='text-align:center; font-size:1.1rem;'>استكشف تاريخ مصر بطريقة فخمة وعصرية.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🧥 أسلوب الحياة":
    st.markdown("<h1 style='text-align:center;'>🧥 أسلوب الحياة الفرعوني</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("<div class='glass-card'><h4>🌾 الكتان الملكي</h4><p>القماش الأساسي للنبلاء والكهنة.</p></div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<div class='glass-card'><h4>👁️ الكحل وعين حورس</h4><p>حماية وجمال في آن واحد.</p></div>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<div class='glass-card'><h4>💍 المجوهرات الذهبية</h4><p>رموز القوة والخلود.</p></div>", unsafe_allow_html=True)

elif menu == "🧪 أسرار الصناعة":
    st.markdown("<h1 style='text-align:center;'>🧪 أسرار الصناعة</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='glass-card'>
        <h3>⚱️ فن التحنيط</h3>
        <p>كيمياء متقدمة حيرت العالم لآلاف السنين.</p>
    </div>
    <div class='glass-card'>
        <h3>✨ الهندسة الفلكية</h3>
        <p>دقة متناهية في بناء الأهرامات والمعابد.</p>
    </div>
    """, unsafe_allow_html=True)

# ====================== قسم الخدمات الجديد ======================
elif menu == "🛠️ خدماتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ خدماتنا</h1>", unsafe_allow_html=True)
    cols = st.columns(2)
    
    with cols[0]:
        st.markdown("""
        <div class='glass-card'>
            <h4>🎨 تصميم هوية بصرية فرعونية</h4>
            <p>لوجو، براند، وتصاميم مستوحاة من الحضارة المصرية.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class='glass-card'>
            <h4>📱 تطوير مواقع وتطبيقات</h4>
            <p>واجهات عصرية تحمل روح التاريخ المصري.</p>
        </div>
        """, unsafe_allow_html=True)

# ====================== قسم الأدوات الجديد ======================
elif menu == "🛠️ أدواتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ أدواتنا الرقمية</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("<div class='glass-card'><h4>🗓️ حاسبة التواريخ الفرعونية</h4></div>", unsafe_allow_html=True)
    with
