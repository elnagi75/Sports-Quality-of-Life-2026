import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. التنسيق ---
st.markdown("""
<style>
    .stApp { direction: rtl; font-family: 'Arial', sans-serif; }
    [data-testid="stSidebar"] { direction: rtl; }
    .lab-title { color: #2E86C1; text-align: center; font-weight: bold; border-bottom: 2px solid #2E86C1; margin-top: 30px; }
    .stRadio label, .stMultiSelect label { font-size: 18px !important; font-weight: bold; }
    .stButton button { font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; padding: 10px !important; }
</style>
""", unsafe_allow_html=True)

st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")

# --- 3. بيانات الفصول ---
MAIN_BOOK_URL = "https://heyzine.com/flip-book/248efb967c.html"
APPX_BOOK_URL = "https://heyzine.com/flip-book/e18c597993.html"

chapters = {
    "محتويات الكتاب": {"url": MAIN_BOOK_URL, "page": 1, "img": "intro.jpg"},
    "الفصل الأول: هندسة الحركة البشرية": {"url": MAIN_BOOK_URL, "page": 1, "img": "ch_1.jpg"},
    "الفصل الثاني: فسيولوجيا الجهد": {"url": MAIN_BOOK_URL, "page": 13, "img": "ch_2.jpg"},
    "الفصل الثالث: القياسات الجسمية": {"url": MAIN_BOOK_URL, "page": 25, "img": "ch_3.jpg"},
    "الفصل الرابع: اللياقة القلبية": {"url": MAIN_BOOK_URL, "page": 37, "img": "ch_4.jpg"},
    "الفصل الخامس: القوة والتحمل": {"url": MAIN_BOOK_URL, "page": 47, "img": "ch_5.jpg"},
    "الفصل السادس: المرونة": {"url": MAIN_BOOK_URL, "page": 62, "img": "ch_6.jpg"},
    "الفصل السابع: اللياقة المهارية": {"url": MAIN_BOOK_URL, "page": 75, "img": "ch_7.jpg"},
    "الفصل الثامن: مبادئ التدريب": {"url": MAIN_BOOK_URL, "page": 89, "img": "ch_8.jpg"},
    "الفصل التاسع: أنظمة تدريب القوة": {"url": MAIN_BOOK_URL, "page": 103, "img": "ch_9.jpg"},
    "الفصل العاشر: التدريب الذكي": {"url": MAIN_BOOK_URL, "page": 117, "img": "ch_10.jpg"},
    "الفصل الحادي عشر: التغذية": {"url": MAIN_BOOK_URL, "page": 131, "img": "ch_11.jpg"},
    "الفصل الثاني عشر: خرافات اللياقة": {"url": MAIN_BOOK_URL, "page": 143, "img": "ch_12.jpg"},
    "الملحق 1: المشي والجري": {"url": APPX_BOOK_URL, "page": 1, "img": "appx_1.jpg"},
    "الملحق 2: التدريب بوزن الجسم": {"url": APPX_BOOK_URL, "page": 13, "img": "appx_2.jpg"},
    "الملحق 3: حبل الوثب": {"url": APPX_BOOK_URL, "page": 23, "img": "appx_3.jpg"},
    "الملحق 4: صندوق الخطو": {"url": APPX_BOOK_URL, "page": 41, "img": "appx_4.jpg"},
    "الملحق 5: عقلة الباب": {"url": APPX_BOOK_URL, "page": 53, "img": "appx_5.jpg"},
    "الملحق 6: أحزمة المقاومة المطاطية": {"url": APPX_BOOK_URL, "page": 65, "img": "appx_6.jpg"},
    "الملحق 7: سلم التوافق": {"url": APPX_BOOK_URL, "page": 79, "img": "appx_7.jpg"},
    "الملحق 8: أطواق اللياقة": {"url": APPX_BOOK_URL, "page": 105, "img": "appx_8.jpg"},
    "الملحق 9: كرة اللياقة": {"url": APPX_BOOK_URL, "page": 127, "img": "appx_9.jpg"},
    "الملحق 10: الكرة الطبية": {"url": APPX_BOOK_URL, "page": 155, "img": "appx_10.jpg"},
    "الملحق 11: الأثقال الحرة": {"url": APPX_BOOK_URL, "page": 167, "img": "appx_11.jpg"},
    "الملحق 12: أحزمة التعلق (TRX)": {"url": APPX_BOOK_URL, "page": 179, "img": "appx_12.jpg"},
    "الملحق 13: حبال القوة القتالية": {"url": APPX_BOOK_URL, "page": 211, "img": "appx_13.jpg"},
    "الملحق 14: جرس الكيتل بيل": {"url": APPX_BOOK_URL, "page": 227, "img": "appx_14.jpg"}
}

# --- 4. القائمة ---
st.sidebar.header("محتويات الكتاب")
selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))

chapter_data = chapters[selected_chapter]
image_container = st.sidebar.empty()
if os.path.exists(chapter_data["img"]):
    image_container.image(chapter_data["img"], use_column_width=True)

# --- 5. العرض (بدون Key لضمان عدم حدوث خطأ) ---
final_url = f"{chapter_data['url']}#page={chapter_data['page']}"
components.html(
    f"""<iframe src="{final_url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
    height=620
)

# الأداة التفاعلية (كما هي)
if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي</h2>", unsafe_allow_html=True)
    # (بقية كود النموذج...)
