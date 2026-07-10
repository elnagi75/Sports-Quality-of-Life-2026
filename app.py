import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة (متوافقة مع الموبايل) ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="centered")

# --- 2. تنسيق CSS ---
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
    
    /* تصميم متجاوب للموبايل لإزالة الهوامش العريضة */
    .stApp { max-width: 600px; margin: 0 auto; }
    
    /* إخفاء القوائم الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* تصغير العناوين لتتناسب مع شاشات الموبايل */
    h1 { font-size: 22px !important; text-align: center; margin-bottom: 10px !important;}
    h3 { font-size: 16px !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")

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

# حجز مساحة علوية للصورة لتظهر فوق الأزرار
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
    # الكود المدمج من Heyzine
    components.html(
        """
        <iframe src="https://heyzine.com/flip-book/8107d3f1a1.html" width="100%" height="480" frameborder="0" allowfullscreen></iframe>
        """,
        height=500
    )
else:
    st.subheader(selected_chapter)
    st.info(f"محتوى '{selected_chapter}' قيد التجهيز... سيتم بناؤه لاحقاً خطوة بخطوة.")
