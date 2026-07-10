import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="centered") # layout="centered" هو الأفضل للموبايل

# CSS متجاوب مع الموبايل
st.markdown("""
<style>
    html, body { direction: rtl; text-align: right; }
    [data-testid="stSidebar"] { direction: rtl; }
    
    /* تصميم متجاوب للموبايل */
    .stApp { max-width: 600px; margin: 0 auto; } 
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* تصغير العناوين للموبايل */
    h1 { font-size: 20px !important; text-align: center; }
    h3 { font-size: 16px !important; }
</style>
""", unsafe_allow_html=True)

# ترويسة مبسطة
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")

chapters = {
    "محتويات الكتاب": "intro.jpg", # تم تغيير الاسم
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

# القائمة الجانبية
st.sidebar.header("محتويات الكتاب")
selected_chapter = st.sidebar.radio("اختر الفصل:", list(chapters.keys()))

# عرض الغلاف والاسم جنباً إلى جنب في القائمة الجانبية (بشكل رأسي)
image_name = chapters[selected_chapter]
if os.path.exists(image_name):
    st.sidebar.image(image_name, use_column_width=True)

# الموجه الديناميكي
if selected_chapter == "محتويات الكتاب":
    components.html("""<iframe src="https://heyzine.com/flip-book/8107d3f1a1.html" width="100%" height="450" frameborder="0" allowfullscreen></iframe>""", height=460)
else:
    st.subheader(selected_chapter)
    st.info("قيد التجهيز...")
