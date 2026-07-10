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
    
    /* تنسيق القائمة الجانبية */
    [data-testid="stSidebar"] {
        direction: rtl;
    }
    
    /* إخفاء القائمة العلوية الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* تحسينات العرض على الموبايل */
    @media (max-width: 600px) {
        h1 { font-size: 22px !important; margin-bottom: 5px !important; }
        h3 { font-size: 16px !important; margin-bottom: 5px !important; }
        .stMarkdown p { font-size: 14px !important; }
        /* تقليل الهوامش العلوية والسفلية في الموبايل لتوفير مساحة */
        .main .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
    }
</style>
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
    st.sidebar.image(image_name, use_column_width=True)
else:
    st.sidebar.warning(f"يرجى رفع صورة الغلاف باسم: {image_name}")

st.sidebar.markdown("---")
st.sidebar.info("📌 هذه المنصة التفاعلية مصممة لمساعدتك على التطبيق العملي للمفاهيم المدروسة بأسلوب مبسط.")

# --- 5. وحدات الفصول (مساحة العرض الديناميكية) ---

def render_intro():
    st.subheader("المقدمة وقائمة المحتويات")
    # الكود المدمج من Heyzine
    components.html(
        """
        <iframe allowfullscreen="allowfullscreen" allow="autoplay; fullscreen; clipboard-write" scrolling="no" class="fp-iframe" style="border: 1px solid lightgray; width: 100%; height: 479px;" src="https://heyzine.com/flip-book/8107d3f1a1.html"></iframe>
        """,
        height=500
    )
    st.markdown("---")

def render_placeholder(chapter_title):
    st.subheader(chapter_title)
    st.info(f"محتوى '{chapter_title}' قيد التجهيز... سيتم بناؤه لاحقاً.")

# --- 6. الموجه الديناميكي (Router) ---
if selected_chapter == "المقدمة وقائمة المحتويات":
    render_intro()
else:
    render_placeholder(selected_chapter)
