import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة ---
# استخدام العرض الشامل (wide) يعطي أفضل نتيجة للكمبيوتر، ويتكيف آلياً مع الموبايل
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS المُعالج ---
st.markdown("""
<style>
    /* ضبط الاتجاه العام للمنصة لليمين */
    .stApp {
        direction: rtl;
        font-family: 'Arial', sans-serif;
    }
    
    /* القائمة الجانبية */
    [data-testid="stSidebar"] {
        direction: rtl;
    }
    
    /* الحل الجذري لمشكلة الحروف العمودية في الموبايل */
    [data-testid="collapsedControl"], [data-testid="stHeader"] {
        direction: ltr;
    }
    
    /* محاذاة العناوين والنصوص لليمين */
    h1, h2, h3, p, label, .stMarkdown {
        text-align: right !important;
    }
    
    /* إخفاء القوائم الافتراضية لمنصة Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# --- 4. الفهرس وربط كل فصل بصورة الغلاف ---
chapters = {
    "محتويات الكتاب": "intro.jpg",
    "الفصل الأول: هندسة الحركة البشرية": "ch_1.jpg",
    "الفصل الثاني: فسيولوجيا الجهد": "ch_2.jpg",
    "الفصل الثالث: القياسات الجسمية": "ch_3.jpg",
    "الفصل الرابع: اللياقة القلبية": "ch_4.jpg",
    "الفصل الخامس: القوة والتحمل": "ch_5.jpg",
    "الفصل السادس: المرونة": "ch_6.jpg",
    "الفصل السابع: اللياقة المهارية": "ch_7.jpg",
    "الفصل الثامن: مبادئ التدريب": "ch_8.jpg",
    "الفصل التاسع: أنظمة تدريب القوة": "ch_9.jpg",
    "الفصل العاشر: التدريب الذكي": "ch_10.jpg",
    "الفصل الحادي عشر: التغذية": "ch_11.jpg",
    "الفصل الثاني عشر: خرافات اللياقة": "ch_12.jpg",
    "الملحق الموسوعي للأجهزة": "appendix.jpg"
}

# --- 5. القائمة الجانبية (Sidebar) ---
st.sidebar.header("محتويات الكتاب")

# حجز مساحة علوية للصورة لتظهر فوق الأزرار بشكل احترافي
image_container = st.sidebar.empty()

# عرض أزرار الاختيار تحت الصورة
selected_chapter = st.sidebar.radio("اختر الفصل للبدء:", list(chapters.keys()))

# تحديث الصورة في المساحة العلوية بناءً على الاختيار
image_name = chapters[selected_chapter]
if os.path.exists(image_name):
    image_container.image(image_name, use_column_width=True)
else:
    image_container.warning(f"مساحة محجوزة لغلاف: {image_name}")

st.sidebar.markdown("---")

# --- 6. الموجه الديناميكي (مساحة العرض) ---
if selected_chapter == "محتويات الكتاب":
    # إضافة رسالة توجيهية لمستخدمي الهواتف
    st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")
    
    # الكود المدمج من Heyzine بحجم مريح للقراءة
    components.html(
        """
        <iframe src="https://heyzine.com/flip-book/8107d3f1a1.html" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
        """,
        height=620
    )
else:
    st.subheader(selected_chapter)
    st.info(f"محتوى '{selected_chapter}' قيد التجهيز... سيتم بناؤه لاحقاً خطوة بخطوة.")
