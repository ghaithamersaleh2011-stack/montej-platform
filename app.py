import streamlit as st

# --- إعدادات الهوية البصرية الفخمة (الأسود والذهبي) ---
st.set_page_config(page_title="Montej Platform | الإمبراطورية", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #D4AF37; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #D4AF37; color: black; font-weight: bold; border: 2px solid #D4AF37; transition: 0.3s; }
    .stButton>button:hover { background-color: black; color: #D4AF37; }
    .service-card { border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; background-color: #0c0c0c; margin-bottom: 20px; text-align: center; }
    .price-tag { color: #00ff00; font-size: 20px; font-weight: bold; }
    .points-tag { color: #5dade2; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# --- محاكاة الأنظمة الخلفية ---
if 'points' not in st.session_state: st.session_state.points = 150
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- 1. صفحة تسجيل الدخول (تتبع الموقع تلقائياً) ---
if not st.session_state.logged_in:
    st.title("🔱 Montej Platform")
    st.subheader("بوابة الدخول العالمية")
    
    # محاكاة تحديد الموقع (فرنسا/سوريا)
    location = st.selectbox("تحديد الموقع (تلقائي بناءً على IP)", ["سوريا - العربية 🇸🇾", "France - Français 🇫🇷"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### تسجيل الدخول")
        st.text_input("البريد الإلكتروني")
        st.text_input("كلمة المرور", type="password")
        if st.button("دخول إلى المنصة"):
            st.session_state.logged_in = True
            st.rerun()
    with col2:
        st.markdown("### إنشاء حساب جديد")
        st.text_input("الاسم الكامل")
        st.selectbox("طريقة الدفع المفضلة", ["Western Union", "Which Money"])
        st.button("تسجيل حساب جديد")

else:
    # --- القائمة الجانبية (نظام النقاط والإدارة) ---
    st.sidebar.title("💎 Montej Member")
    st.sidebar.markdown(f"**⭐ نقاط الولاء: {st.session_state.points}**")
    st.sidebar.progress(min(st.session_state.points / 500, 1.0))
    st.sidebar.caption("احصل على 500 نقطة لخدمة مجانية!")
    
    menu = st.sidebar.radio("القائمة الرئيسية", 
        ["🛠️ كافة الخدمات (45)", "💎 Montej Pass", "💰 شحن الرصيد", "🤖 Montej AI", "⚙️ الإعدادات (30)", "📞 تواصل معنا"])

    # --- 2. قسم الخدمات الشامل (الـ 45 خدمة) ---
    if menu == "🛠️ كافة الخدمات (45)":
        st.title("🚀 سوق الخدمات الذكية")
        t1, t2, t3, t4, t5 = st.tabs(["✍️ محتوى", "🎨 تصميم", "🎬 فيديو", "🧠 متقدمة", "🔥 باقات"])
        
        with t1:
            services = [
                ("كتابة كتب PDF تحفيزية", "50$", 20), ("تلخيص كتب طويلة", "20$", 10),
                ("مقالات SEO للمواقع", "15$", 5), ("سكربتات يوتيوب/تيك توك", "25$", 10),
                ("سيرة ذاتية (CV) احترافية", "30$", 15), ("وصف منتجات", "10$", 5)
            ]
            for s, p, pts in services:
                st.markdown(f"<div class='service-card'><h3>{s}</h3><span class='price-tag'>{p}</span><br><span class='points-tag'>+{pts} نقطة ولاء</span></div>", unsafe_allow_html=True)
                st.button(f"طلب خدمة: {s}", key=s)

        with t3:
            st.subheader("خدمات الفيديو الاحترافية")
            v_services = [("مونتاج فيديوهات قصيرة تحفيزية", "40$"), ("إضافة ترجمة احترافية", "15$"), ("تحويل مقال إلى فيديو AI", "60$")]
            for s, p in v_services:
                st.markdown(f"<div class='service-card'><h3>{s}</h3><span class='price-tag'>{p}</span></div>", unsafe_allow_html=True)
                st.button(f"بدء إنتاج: {s}", key=s)

    # --- 3. نظام Montej Pass (نظام بلس) ---
    elif menu == "💎 Montej Pass":
        st.title("💎 اشتراكات Montej Pass")
        st.write("اشترك الآن لفتح كافة الخدمات مجاناً!")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='service-card'><h2>Essential</h2><b>15$/شهرياً</b><br><b>140$/سنوياً</b><br><br>5 خدمات مجانية<br>دعم فني عادي</div>", unsafe_allow_html=True)
            st.button("اشترك في الأساسي")
        with c2:
            st.markdown("<div class='service-card' style='border-width: 3px;'><h2>Pro 🏆</h2><b>35$/شهرياً</b><br><b>320$/سنوياً</b><br><br>خدمات غير محدودة<br>معالجة سريعة جداً</div>", unsafe_allow_html=True)
            st.button("اشترك في برو")
        with c3:
            st.markdown("<div class='service-card'><h2>Professional 👑</h2><b>60$/شهرياً</b><br><b>550$/سنوياً</b><br><br>استشاري AI خاص<br>جودة Ultra HD</div>", unsafe_allow_html=True)
            st.button("اشترك في بروفيسينال")

    # --- 4. شحن الرصيد (منال ابو ستة) ---
    elif menu == "💰 شحن الرصيد":
        st.title("💰 تفعيل الحساب والشحن")
        st.info("نظام الدفع المعتمد: Western Union & Which Money")
        col_pay1, col_pay2 = st.columns(2)
        with col_pay1:
            st.markdown(f"""
            **بيانات المستلم:**
            - الاسم: منال ابو ستة
            - الهاتف: 81146047
            """)
        with col_pay2:
            st.file_uploader("ارفع صورة إيصال التحويل (Screenshot)")
            if st.button("تأكيد إرسال الدفعة"):
                st.success("تم الإرسال بنجاح. سيقوم المساعد بتفعيل حسابك فور التأكد.")

    # --- 5. المساعد التقني Montej AI ---
    elif menu == "🤖 Montej AI":
        st.title("🤖 مساعد Montej الذكي")
        st.write("أنا هنا لمساعدتك في أي استفسار أو مشكلة تقنية.")
        user_in = st.chat_input("كيف يمكنني مساعدتك اليوم؟")
        if user_in:
            st.chat_message("assistant").write(f"مرحباً بك! لقد استلمت رسالتك: '{user_in}'. سأقوم بالرد عليك فوراً أو تحويلك للمدير إذا لزم الأمر.")

    # --- 6. الإعدادات المتقدمة (الـ 30 إعداد) ---
    elif menu == "⚙️ الإعدادات (30)":
        st.title("⚙️ تفضيلات المنصة")
        col_set1, col_set2 = st.columns(2)
        with col_set1:
            st.selectbox("تغيير اللغة", ["العربية", "Français", "English"])
            st.selectbox("العملة", ["USD ($)", "EUR (€)", "SYP"])
            st.selectbox("الدولة", ["سوريا", "فرنسا", "لبنان", "مصر"])
        with col_set2:
            st.toggle("تنبيهات البريد الإلكتروني", True)
            st.toggle("الوضع الليلي (تلقائي)")
            st.slider("دقة مخرجات الـ AI", 0, 100, 85)
        st.caption("هناك 24 إعداداً إضافياً يمكنك تخصيصها في نسخة البرو.")

    # --- 7. تواصل معنا والترجمة التلقائية ---
    elif menu == "📞 تواصل معنا":
        st.title("📞 مركز الاتصال بالإدارة")
        st.write("أرسل رسالتك بأي لغة، وستصل للمدير مترجمة للعربية.")
        contact_msg = st.text_area("رسالتك أو بلاغك عن مشكلة:")
        if st.button("إرسال البلاغ للمدير"):
            st.warning("جاري ترجمة الرسالة للعربية وإرسالها للمدير...")
            st.success("تم التوصيل بنجاح!")

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()
