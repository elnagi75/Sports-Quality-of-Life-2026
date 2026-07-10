import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة ---
st.set_page_config(
    page_title="الرياضة وجودة الحياة",
    page_icon="🏃‍♂️",
    layout="wide"
)

# فرض اتجاه اليمين لليسار (RTL) وتنسيق الخطوط عبر CSS
st.markdown("""
<style>
    /* توجيه المنصة بالكامل للغة العربية */
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    
    /* تنسيق القائمة الجانبية لتتناسب مع الاتجاه */
    [data-testid="stSidebar"] {
        direction: rtl;
    }
    
    /* إخفاء القائمة العلوية الافتراضية لـ Streamlit لمظهر أكثر احترافية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 2. الترويسة الرئيسية الثابتة ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("### الأستاذ الدكتور محمود عبد المحسن أحمد")
st.markdown("**أستاذ التدريب الرياضي (الكرة الطائرة) - قسم الرياضات الجماعية وألعاب المضرب - كلية علوم الرياضة - جامعة المنيا**")
st.markdown("---")

# --- 3. الفهرس وربط كل فصل بصورة الغلاف الخاصة به ---
chapters = {
    "المقدمة وقائمة المحتويات": "intro.jpg",
    "الفصل الأول: هندسة الحركة البشرية": "ch_1.jpg",
    "الفصل الثاني: فسيولوجيا الجهد وإنتاج الطاقة": "ch_2.jpg",
    "الفصل الثالث: القياسات الجسمية وتركيب الجسم": "ch_3.jpg",
    "الفصل الرابع: اللياقة القلبية التنفسية": "ch_4.jpg",
    "الفصل الخامس: القوة والتحمل العضلي": "ch_5.jpg",
    "الفصل السادس: المرونة وصحة المفاصل": "ch_6.jpg",
    "الفصل السابع: اللياقة المهارية والتوافق العصبي": "ch_7.jpg",
    "الفصل الثامن: مبادئ التدريب ومعادلة F.I.T.T": "ch_8.jpg",
    "الفصل التاسع: أنظمة تدريب القوة": "ch_9.jpg",
    "الفصل العاشر: التدريب الذكي الوظيفي و HIIT": "ch_10.jpg",
    "الفصل الحادي عشر: التغذية الرياضية والاستشفاء": "ch_11.jpg",
    "الفصل الثاني عشر: خرافات اللياقة والأخطاء الشائعة": "ch_12.jpg",
    "الملحق الموسوعي العملي للأجهزة والأدوات": "appendix.jpg"
}

# --- 4. القائمة الجانبية (Sidebar) ---
st.sidebar.header("فهرس المنصة")

# اختيار الفصل
selected_chapter = st.sidebar.radio("اختر الفصل للبدء:", list(chapters.keys()))

st.sidebar.markdown("---")

# البرواز الديناميكي لعرض صورة الغلاف
image_name = chapters[selected_chapter]
if os.path.exists(image_name):
    # إذا كانت الصورة موجودة في المجلد، يتم عرضها
    st.sidebar.image(image_name, use_column_width=True)
else:
    # رسالة مؤقتة تظهر لك كإشعار حتى تقوم برفع الصورة
    st.sidebar.warning(f"مساحة محجوزة لغلاف: {image_name}")

st.sidebar.markdown("---")
st.sidebar.info("📌 هذه المنصة التفاعلية مصممة لمساعدتك على التطبيق العملي للمفاهيم المدروسة بأسلوب مبسط.")

# --- 5. وحدات الفصول (مساحة العرض الديناميكية) ---

def render_intro():
    st.subheader("المقدمة وقائمة المحتويات")
    # سيتم هنا دمج رابط Heyzine وأي أدوات تفاعلية نستخلصها
    st.info("نحن الآن في انتظار إضافة المحتوى التفاعلي الخاص بالمقدمة.")

def render_placeholder(chapter_title):
    st.subheader(chapter_title)
    st.info(f"محتوى '{chapter_title}' قيد التجهيز... سيتم بناؤه لاحقاً خطوة بخطوة.")

# --- 6. الموجه الديناميكي (Router) ---
if selected_chapter == "المقدمة وقائمة المحتويات":
    render_intro()
else:
    render_placeholder(selected_chapter)
