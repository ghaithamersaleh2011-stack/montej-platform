import streamlit as st
from googletrans import Translator

# --- 1. إعدادات الهوية واللغة ---
translator = Translator()

def get_text(text, target_lang='ar'):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text

st.set_page_config(page_title="Montej Platform", layout="wide")

# --- 2. التصميم الفخم (Black & Gold) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; font-weight: bold; }
    .service-box { border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; background: #111; transition: 0.3s; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. نظام تسجيل الدخول ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Montej | بوابة الدخول")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("تسجيل الدخول")
        st.text_input("البريد الإلكتروني")
        st.text_input("كلمة المرور", type="password")
        if st.button("دخول"):
            st.session_state.logged_in = True
            st.rerun()
    with col2:
        st.subheader("إنشاء حساب (Signup)")
        st.selectbox("مكان الإقامة لتحديد اللغة تلقائياً", ["فرنسا (Français)", "سوريا (العربية)", "أخرى"])
        st.button("إنشاء حساب جديد")

else:
    # --- 4. واجهة التطبيق الرئيسية ---
    st.sidebar.title("💎 Montej AI")
    st.sidebar.write("⭐ نقاطك: **150 نقطة**")
    
    menu = st.sidebar.radio("القائمة", ["الخدمات", "Montej Pass", "شحن الرصيد", "Montej AI (المساعد)", "تواصل معنا", "الإعدادات"])

    # --- 5. قسم الخدمات (الـ 45 خدمة) ---
    if menu == "الخدمات":
        st.title("🛠️ سوق الخدمات الاحترافية")
        cat = st.selectbox("اختر القسم", ["الكتابة وصناعة المحتوى", "التصميم والعروض", "الفيديو والمونتاج", "خدمات متقدمة", "الباقات المميزة"])
        
        if cat == "الكتابة وصناعة المحتوى":
            services = [
                ("كتابة كتب PDF", "50$"), ("تلخيص كتب", "20$"), ("مقالات SEO", "15$"),
                ("سكربتات يوتيوب", "25$"), ("وصف منتجات", "10$"), ("سيرة ذاتية CV", "30$")
            ]
            for s, p in services:
                col_s, col_p = st.columns([3, 1])
                col_s.write(f"✅ {s}")
                if col_p.button(f"طلب ({p})", key=s):
                    st.toast(f"تم إضافة {s} لطلباتك!")

    # --- 6. نظام Montej Pass (PS Plus Style) ---
    elif menu == "Montej Pass":
        st.title("💎 اشتراكات Montej Pass")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("### Essential\n15$/شهر - 140$/سنة\n5 خدمات مجانية")
        with c2:
            st.success("### Pro 🏆\n35$/شهر - 320$/سنة\nكل شيء مفتوح + سرعة AI")
        with c3:
            st.warning("### Professional 💎\n60$/شهر - 550$/سنة\nدعم خاص + جودة 4K")

    # --- 7. الإعدادات (الـ 30 إعداد) ---
    elif menu == "الإعدادات":
        st.title("⚙️ الإعدادات")
        col_a, col_b = st.columns(2)
        with col_a:
            st.selectbox("اللغة", ["العربية", "Français", "English"])
            st.selectbox("العملة", ["USD", "EUR", "SYP"])
            st.text_input("الدولة")
        with col_b:
            st.toggle("تفعيل الإشعارات")
            st.toggle("الوضع الليلي التلقائي")
            st.slider("حجم الخط", 12, 24, 16)

    # --- 8. المساعد التقني و تواصل معنا (نظام الترجمة) ---
    elif menu == "تواصل معنا":
        st.title("📞 مركز الرسائل")
        user_msg = st.text_area("اكتب رسالتك للمدير (بأي لغة)")
        if st.button("إرسال"):
            # محاكي ترجمة للمدير
            translated = get_text(user_msg, 'ar')
            st.write(f"سوف تصل للمدير هكذا: {translated}")
            st.success("تم الإرسال!")

    elif menu == "شحن الرصيد":
        st.title("💰 شحن الرصيد")
        st.info("الدفع عبر: Western Union / Which Money")
        st.write("الاسم: **منال ابو ستة** | الهاتف: **81146047**")
        st.file_uploader("ارفع صورة إيصال الدفع")
