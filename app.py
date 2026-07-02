import streamlit as st

st.set_page_config(page_title="🏛️ #ATegypT", page_icon="🇪🇬", layout="wide", initial_sidebar_state="expanded")

# CSS - Glassmorphism
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a0a0a, #1a0033); }
    .glass-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,215,0,0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        transition: all 0.4s;
    }
    .glass-card:hover {
        background: rgba(255,255,255,0.13);
        transform: translateY(-6px);
        border-color: #FFD700;
    }
    h1, h2, h3 { color: #FFD700 !important; text-shadow: 0 0 15px rgba(255,215,0,0.5); }
    .gold-btn { background: linear-gradient(135deg, #FFD700, #FFAA00); color: black; font-weight: bold; border-radius: 50px; padding: 10px 25px; }
    .gold-btn:hover { transform: scale(1.08); }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/ankh.png", width=70)
st.sidebar.markdown("<h2 style='color:#FFD700; text-align:center;'>☥ البوصلة الفرعونية</h2>", unsafe_allow_html=True)

menu = st.sidebar.radio("اختر القسم", [
    "🏠 الرئيسية", "🧥 أسلوب الحياة", "🧪 أسرار الصناعة",
    "🛠️ خدماتنا", "🛠️ أدواتنا", "🏛️ معرض الصور", "📜 عن المشروع"
])

# Header
st.markdown("<div style='text-align:center; padding:2rem 0; border-bottom:3px solid #FFD700; margin-bottom:2rem;'><h1>🏛️ #ATegypT</h1><p style='color:#ddd; font-size:1.3rem;'>عظمة مصر الخالدة</p></div>", unsafe_allow_html=True)

# الأقسام
if menu == "🏠 الرئيسية":
    st.image("https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1400&q=80", use_container_width=True)
    st.markdown("<div class='glass-card'><h3 style='text-align:center;'>𓋹 مرحباً بك في بوابة الحضارة</h3><p style='text-align:center;'>استكشف تاريخ مصر بطريقة فخمة.</p></div>", unsafe_allow_html=True)

elif menu == "🧥 أسلوب الحياة":
    st.markdown("<h1 style='text-align:center;'>🧥 أسلوب الحياة الفرعوني</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🌾 الكتان الملكي</h4><p>قماش النبلاء والكهنة.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>👁️ الكحل وعين حورس</h4><p>حماية وجمال.</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>💍 المجوهرات</h4><p>رموز القوة والخلود.</p></div>", unsafe_allow_html=True)

elif menu == "🧪 أسرار الصناعة":
    st.markdown("<h1 style='text-align:center;'>🧪 أسرار الصناعة</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>⚱️ فن التحنيط</h3><p>كيمياء متقدمة حيرت العالم.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><h3>✨ الهندسة الفلكية</h3><p>دقة الأهرامات والمعابد.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ خدماتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ خدماتنا</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='glass-card'><h4>🎨 تصميم هوية فرعونية</h4><p>لوجو وبراند مصري أصيل.</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📱 تطوير مواقع</h4><p>واجهات تحمل روح مصر.</p></div>", unsafe_allow_html=True)

elif menu == "🛠️ أدواتنا":
    st.markdown("<h1 style='text-align:center;'>🛠️ أدواتنا</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='glass-card'><h4>🗓️ حاسبة تواريخ</h4></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='glass-card'><h4>📜 مولد أسماء</h4></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='glass-card'><h4>🎨 مولد ألوان</h4></div>", unsafe_allow_html=True)

elif menu == "🏛️ معرض الصور":
    st.markdown("<h1 style='text-align:center;'>🏛️ معرض الصور</h1>", unsafe_allow_html=True)

else:
    st.markdown("<h1 style='text-align:center;'>📜 عن #ATegypT</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'><p>اكتب وصف المشروع هنا...</p></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#aaa; padding:25px;'>𓋹 Glorifying Ancient Egypt 𓆣</div>", unsafe_allow_html=True)
