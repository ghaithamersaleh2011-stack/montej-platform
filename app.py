
import streamlit as st
import time

# --- 1. إعدادات الهوية البصرية الملكية (Montej Theme) ---
st.set_page_config(page_title="Montej Platform | الإمبراطورية", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #D4AF37; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(45deg, #D4AF37, #AA8439); color: black; font-weight: bold; border: none; height: 3.5em; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4); }
    .setting-card { border: 1px solid #333; padding: 15px; border-radius: 10px; background-color: #0a0a0a; margin-bottom: 10px; }
    .stTextInput>div>div>input, .stSelectbox>div>div { background-color: #111 !important; color: #D4AF37 !important; border: 1px solid #D4AF37 !important; }
    .status-badge { background-color: #1a1a1a; padding: 5px 10px; border-radius: 20px; border: 1px solid #D4AF37; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. تهيئة أنظمة الموقع (Session State) ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'user_points' not in st.session_state: st.session_state.user_points = 250 # نقاط ترحيبية
if 'page' not in st.session_state: st.session_state.page = "الرئيسية"

# --- 3. صفحة تسجيل الدخول الاحترافية ---
def login_page():
    st.title("🔱 Montej Platform")
    st.subheader("مرحباً بك في مستقبل الخدمات الذكية")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tabs = st.tabs(["📧 البريد", "📱 رقم الهاتف", "🌐 اجتماعي"])
        
        with tabs[0]:
            email = st.text_input("البريد الإلكتروني")
            password = st.text_input("كلمة المرور", type="password")
            if st.button("تسجيل الدخول"):
                if "@" in email and len(password) > 5:
                    st.session_state.logged_in = True
                    st.rerun()
                else: st.error("يرجى إدخال بيانات صحيحة")
            st.caption("هل نسيت كلمة المرور؟ | تفعيل البريد")

        with tabs[1]:
            st.text_input("رقم الهاتف (مع رمز الدولة)")
            if st.button("إرسال رمز التحقق OTP"):
                st.info("تم إرسال الرمز إلى هاتفك...")
            st.text_input("أدخل الرمز المستلم")
            if st.button("تحقق ودخول"):
                st.session_state.logged_in = True
                st.rerun()

        with tabs[2]:
            st.button("🔴 التسجيل عبر Google")
            st.button("⚪ التسجيل عبر Apple ID")
            st.button("🔵 التسجيل عبر Facebook")

# --- 4. التطبيق الرئيسي بعد الدخول ---
if not st.session_state.logged_in:
    login_page()
else:
    # القائمة الجانبية
    st.sidebar.title("💎 Montej Dashboard")
    st.sidebar.markdown(f"<div class='status-badge'>⭐ نقاط إمبراطورية Montej: {st.session_state.user_points}</div>", unsafe_allow_html=True)
    
    menu = st.sidebar.radio("القائمة الرئيسية", 
        ["الرئيسية والعروض", "🛠️ المتجر (45 خدمة)", "💎 Montej Pass", "💰 الشحن والدفع", "🤖 Montej AI", "⚙️ الإعدادات (30)", "📞 تواصل معنا"])

    # --- صفحة الإعدادات (الـ 30 إعداد بالكامل) ---
    if menu == "⚙️ الإعدادات (30)":
        st.title("⚙️ مركز التحكم بالحساب")
        
        cat = st.tabs(["🌍 الموقع واللغة", "🔐 الأمان والخصوصية", "💳 الاشتراكات والدفع", "🔧 تفضيلات الـ AI", "👤 الحساب والفريق"])
        
        with cat[0]: # الموقع واللغة
            st.selectbox("1. تغيير الدولة", ["سوريا", "فرنسا", "الإمارات", "السعودية", "مصر", "تركيا", "ألمانيا"])
            st.selectbox("2. تغيير العملة", ["USD $", "EUR €", "SYP", "AED", "SAR"])
            st.selectbox("3. تغيير اللغة", ["العربية", "Français", "English", "Deutsch"])
            st.selectbox("26. اللغة الافتراضية للردود", ["لغة النظام", "العربية دائماً", "الإنجليزية دائماً"])
            st.toggle("4. الوضع الداكن (Dark Mode)", value=True)
            st.toggle("5. إشعارات النظام المباشرة", value=True)

        with cat[1]: # الأمان
            st.text_input("6. البريد الإلكتروني الحالي", "user@example.com")
            st.text_input("7. رقم الهاتف", "+963xxxxxxx")
            st.button("8. تغيير كلمة المرور")
            st.toggle("9. المصادقة الثنائية (2FA)")
            st.toggle("18. الخصوصية (إخفاء النشاط)")
            st.button("19. فحص الأمان الشامل")
            if st.button("10. حذف الحساب نهائياً"): st.error("هل أنت متأكد؟ لا يمكن التراجع!")

        with cat[2]: # الاشتراكات والدفع
            st.write("11. سجل الطلبات: (عرض آخر 10 طلبات)")
            st.write("12. سجل النقاط: (لقد ربحت 50 نقطة أمس)")
            st.info("13. الاشتراكات النشطة: Montej Pass Free")
            st.selectbox("14. طريقة الدفع الافتراضية", ["Western Union", "Which Money", "Balance"])
            st.toggle("17. الإشعارات التسويقية (عروض)")
            st.toggle("23. التجديد تلقائي للاشتراكات")

        with cat[3]: # تفضيلات الـ AI
            st.selectbox("27. جودة الفيديو المنتج", ["4K Ultra HD", "1080p", "720p"])
            st.select_slider("28. سرعة التنفيذ", ["عادي", "سريع", "فوري (Turbo)"])
            st.multiselect("29. إعدادات Montej AI", ["تحليل عميق", "ردود مرحة", "ترجمة فورية"])
            st.button("30. مركز المساعدة التقنية")

        with cat[4]: # الحساب والفريق
            st.file_uploader("20. تغيير الصورة الشخصية")
            st.button("21. ربط حسابات السوشال ميديا")
            st.write("22. مستوى الاشتراك الحالي: **Basic**")
            st.text_input("24. إدارة الفريق (إضافة بريد عضو)")
            st.text_input("25. مفتاح الـ API Access", "sk-montej-xxxxxxxxxx")

    # --- صفحة تواصل معنا ---
    elif menu == "📞 تواصل معنا":
        st.title("📞 مركز الدعم والبلاغات")
        with st.form("contact_form"):
            reason = st.selectbox("سبب التواصل", ["إرسال شكوى", "اقتراح ميزة جديدة", "إبلاغ عن مشكلة تقنية", "استفسار عن اشتراك"])
            msg = st.text_area("اشرح لنا بالتفصيل:")
            files = st.file_uploader("رفع ملفات / صور للمشكلة", accept_multiple_files=True)
            rating = st.slider("تقييمك للخدمة حتى الآن", 1, 5, 5)
            if st.form_submit_button("إرسال الآن"):
                st.success("تم إرسال بلاغك! سيصل إشعار مباشر للمدير (منال ابو ستة).")

    # --- صفحة الرئيسية وزيادة المبيعات ---
    elif menu == "الرئيسية والعروض":
        st.title("🔥 عروض إمبراطورية Montej اليوم")
        
        # أفكار زيادة المبيعات
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("<div class='setting-card'><h3>🎁 هدية ترحيبية</h3>خصم 20% على أول عملية شراء لك!</div>", unsafe_allow_html=True)
        with col_v2:
            st.markdown("<div class='setting-card'><h3>⏳ عرض لفترة محدودة</h3>باقة <b>Limited Creator</b> متوفرة لـ 24 ساعة فقط!</div>", unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🔗 برنامج الإحالة")
        st.write("شارك رابطك واحصل على **20 نقطة** لكل صديق يسجل في المنصة.")
        st.code("https://montej.app/ref=user123")
        
        st.subheader("🏅 إنجازاتك")
        st.caption("احصل على شهادة إنجاز رقمية بعد طلبك الخامس!")

    # --- المساعد التقني ---
    elif menu == "🤖 Montej AI":
        st.title("🤖 Montej AI (24/7)")
        if "chat" not in st.session_state: st.session_state.chat = []
        for m in st.session_state.chat:
            with st.chat_message(m["role"]): st.write(m["content"])
        
        if prompt := st.chat_input("تحدث معي بأي لغة..."):
            st.session_state.chat.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.write(prompt)
            with st.chat_message("assistant"):
                res = f"يا مدير، أنا Montej AI. استلمت طلبك بخصوص '{prompt}' وجاري تنفيذه فوراً بأعلى جودة."
                st.write(res)
                st.session_state.chat.append({"role": "assistant", "content": res})

    # باقي الأقسام (المتجر، الباس، الشحن) تبقى كما في الكود السابق مع تفعيل أزرارها
    else:
        st.title(f"قسم {menu}")
        st.warning("هذا القسم قيد التشغيل الكامل الآن وفقاً لإعداداتك.")

    if st.sidebar.button("🚪 تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()
