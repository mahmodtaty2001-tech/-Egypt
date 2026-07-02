import streamlit as st

st.set_page_config(page_title="🏛️ #ATegypT", page_icon="🇪🇬", layout="wide", initial_sidebar_state="expanded")

# ====================== CSS محسن مع 3D & ألوان أوضح ======================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(10,10,10,0.85), rgba(26,0,51,0.85)), 
                    url('https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=2000&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    .glass-card {
        background: rgba(15, 15, 35, 0.75);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 215, 0, 0.45);
        border-radius: 22px;
        padding: 25px;
        margin: 18px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6),
                    inset 0 2px 8px rgba(255, 215, 0, 0.1);
        transition: all 0.4s ease;
    }
    
    .glass-card:hover {
        background: rgba(20, 20, 45, 0.85);
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 215, 0, 0.25);
    }

    h1, h2, h3 { 
        color: #FFD700 !important; 
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.7); 
    }

    /* Sidebar Hatshepsut Style */
    .sidebar .css-1d391kg {
        background: rgba(8, 8, 25, 0.95) !important;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# ====================== Sidebar - وجه حتشبسوت ======================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Statue_of_Hatshepsut.jpg/800px-Statue_of_Hatshepsut.jpg", width=180)
st.sidebar.markdown("<h2 style='color:#FFD700; text-align:center;'>☥ حتشبسوت</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#ccc;'>الملكة الفرعونية</p>", unsafe_allow_html=True)

menu = st.sidebar.radio("اختر القسم", [
    "🏠 الرئيسية", 
    "🧥 أسلوب الحياة", 
    "🧪 أسرار الصناعة",
    "🛠️ خدماتنا", 
    "🛠️ أدواتنا", 
    "🏛️ معرض الصور", 
    "📜 عن المشروع"
], label_visibility="collapsed")

# ====================== Header ======================
st.markdown("""
<div style='text-align:center; padding:2.5rem 0; margin-bottom:2rem; border-bottom:4px solid #FFD700;'>
    <h1>🏛️ #ATegypT</h1>
    <p style='color:#ffeb99; font-size:1.35rem;'>عظمة مصر الخالدة</p>
</div>
""", unsafe_allow_html=True)

# ====================== الأقسام ======================
if menu == "🏠 الرئيسية":
    st.markdown("<div class='glass-card'><h3 style='text-align:center;'>𓋹 مرحباً بك في بوابة الحضارة المصرية</h3></div>", unsafe_allow_html=True)

elif menu == "🧥 أسلوب الحياة":
    st.markdown("<h1 style='text-align:center;'>🧥 أسلوب الحياة الفرعوني</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🌾 الكتان الملكي</h4><p>قماش النبلاء.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>👁️ الكحل وعين حورس</h4><p>حماية وجمال.</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>💍 المجوهرات الذهبية</h4><p>رموز الخلود.</p></div>", unsafe_allow_html=True)

elif menu == "🧪 أسرار الصناعة":
    st.markdown("<h1 style='text-align:center;'>🧪 أسرار الصناعة</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>⚱️ فن التحنيط</h3><p>كيمياء متقدمة.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>✨ الهندسة الفلكية</h3><p>دقة الأهرامات.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ خدماتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ خدماتنا</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='glass-card'><h4>🎨 تصميم هوية فرعونية</h4><p>براند مصري أصيل.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📱 تطوير مواقع وتطبيقات</h4><p>واجهات فخمة.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ أدواتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ أدواتنا</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🗓️ حاسبة تواريخ</h4></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📜 مولد أسماء فرعونية</h4></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>🎨 مولد ألوان مصرية</h4></div>", unsafe_allow_html=True)

else:
    st.markdown("<h1 style='text-align:center;'>📜 عن #ATegypT</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><p>اكتب هنا وصف مشروعك...</p></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#ccc; padding:20px;'>𓋹 𓆣 Glorifying Ancient Egypt 𓊖</div>", unsafe_allow_html=True)
