import streamlit as st

st.set_page_config(page_title="مصر", page_icon="🇪🇬", layout="wide", initial_sidebar_state="expanded")

# ====================== CSS ======================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(5,5,15,0.9), rgba(20,10,5,0.85)), 
                    url('https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=2000&q=80');
        background-size: cover;
        background-attachment: fixed;
    }
    
    .glass-card {
        background: rgba(10, 10, 25, 0.82);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 215, 0, 0.45);
        border-radius: 24px;
        padding: 28px;
        margin: 18px 0;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.65);
    }
    
    .glass-card:hover {
        background: rgba(20, 15, 35, 0.9);
        transform: translateY(-8px);
    }

    h1, h2, h3 { 
        color: #FFD700 !important; 
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.75); 
    }
</style>
""", unsafe_allow_html=True)

# ====================== Sidebar - حتشبسوت ======================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Statue_of_Hatshepsut.jpg/800px-Statue_of_Hatshepsut.jpg", width=210)
st.sidebar.markdown("<h2 style='color:#FFD700; text-align:center;'>☥ حتشبسوت</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#D4AF37;'>الملكة الفرعونية</p>", unsafe_allow_html=True)

menu = st.sidebar.radio("اختر القسم", [
    "🏠 الرئيسية", 
    "🧥 أسلوب الحياة", 
    "🧪 أسرار الصناعة",
    "🛠️ خدماتنا", 
    "🛠️ أدواتنا", 
    "🏛️ معرض الصور", 
    "📜 عن مصر"
], label_visibility="collapsed")

# ====================== Header (بدون لوجو) ======================
st.markdown("""
<div style='text-align:center; padding:3rem 0 2rem 0; margin-bottom:2rem; border-bottom:4px solid #FFD700;'>
    <h1>🏛️ مصر</h1>
    <p style='color:#D4AF37; font-size:1.4rem;'>نملك تاريخ الحضارة الإنسانية</p>
</div>
""", unsafe_allow_html=True)

# ====================== الأقسام ======================
if menu == "🏠 الرئيسية":
    st.markdown("""
    <div class='glass-card'>
        <h3 style='text-align:center;'>𓋹 مرحباً بك في مصر</h3>
        <p style='text-align:center;'>نحن نملك الآثار المصرية القديمة ونعيد إحياء عظمتها رقمياً.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🧥 أسلوب الحياة":
    st.markdown("<h1 style='text-align:center;'>🧥 أسلوب الحياة الفرعوني</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🌾 الكتان الملكي</h4><p>قماش النبلاء.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>👁️ الكحل وعين حورس</h4><p>حماية وجمال.</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>💍 المجوهرات</h4><p>رموز الخلود.</p></div>", unsafe_allow_html=True)

elif menu == "🧪 أسرار الصناعة":
    st.markdown("<h1 style='text-align:center;'>🧪 أسرار الصناعة</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>⚱️ فن التحنيط</h3><p>كيمياء مقدّسة.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>✨ الهندسة الفلكية</h3><p>دقة الأهرامات.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ خدماتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ خدماتنا</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='glass-card'><h4>🎨 تصميم هوية فرعونية</h4><p>براند أصيل.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📱 تطوير مواقع</h4><p>واجهات فخمة.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ أدواتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ أدواتنا</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🗓️ حاسبة تواريخ</h4></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📜 مولد أسماء</h4></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>🎨 مولد ألوان</h4></div>", unsafe_allow_html=True)

else:
    st.markdown("<h1 style='text-align:center;'>📜 عن مصر</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><p>نملك أعظم الآثار المصرية القديمة ونقدمها لك رقمياً.</p></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#D4AF37; padding:25px;'>𓋹 مصر • حضارة خالدة 𓆣</div>", unsafe_allow_html=True)
