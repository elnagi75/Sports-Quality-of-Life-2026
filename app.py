import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS ---
st.markdown("""
<style>
    .stApp { direction: rtl; font-family: 'Arial', sans-serif; }
    [data-testid="stSidebar"] { direction: rtl; }
    .lab-title { color: #2E86C1; text-align: center; font-weight: bold; border-bottom: 2px solid #2E86C1; margin-top: 30px; }
</style>
""", unsafe_allow_html=True)

st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")

# --- 3. بيانات الفصول ---
MAIN_BOOK_URL = "https://heyzine.com/flip-book/248efb967c.html"
APPX_BOOK_URL = "https://heyzine.com/flip-book/e18c597993.html"

chapters = {
    "محتويات الكتاب": {"url": MAIN_BOOK_URL, "page": 1},
    "الفصل الأول: هندسة الحركة البشرية": {"url": MAIN_BOOK_URL, "page": 1},
    "الفصل الثاني: فسيولوجيا الجهد": {"url": MAIN_BOOK_URL, "page": 13},
    "الفصل الثالث: القياسات الجسمية": {"url": MAIN_BOOK_URL, "page": 25},
    "الفصل الرابع: اللياقة القلبية": {"url": MAIN_BOOK_URL, "page": 37},
    "الفصل الخامس: القوة والتحمل": {"url": MAIN_BOOK_URL, "page": 47},
    "الفصل السادس: المرونة": {"url": MAIN_BOOK_URL, "page": 62},
    "الفصل السابع: اللياقة المهارية": {"url": MAIN_BOOK_URL, "page": 75},
    "الفصل الثامن: مبادئ التدريب": {"url": MAIN_BOOK_URL, "page": 89},
    "الفصل التاسع: أنظمة تدريب القوة": {"url": MAIN_BOOK_URL, "page": 103},
    "الفصل العاشر: التدريب الذكي": {"url": MAIN_BOOK_URL, "page": 117},
    "الفصل الحادي عشر: التغذية": {"url": MAIN_BOOK_URL, "page": 131},
    "الفصل الثاني عشر: خرافات اللياقة": {"url": MAIN_BOOK_URL, "page": 143},
    "الملحق 1: المشي والجري": {"url": APPX_BOOK_URL, "page": 1},
    "الملحق 2: التدريب بوزن الجسم": {"url": APPX_BOOK_URL, "page": 13},
    "الملحق 3: حبل الوثب": {"url": APPX_BOOK_URL, "page": 23},
    "الملحق 4: صندوق الخطو": {"url": APPX_BOOK_URL, "page": 41},
    "الملحق 5: عقلة الباب": {"url": APPX_BOOK_URL, "page": 53},
    "الملحق 6: أحزمة المقاومة المطاطية": {"url": APPX_BOOK_URL, "page": 65},
    "الملحق 7: سلم التوافق": {"url": APPX_BOOK_URL, "page": 79},
    "الملحق 8: أطواق اللياقة": {"url": APPX_BOOK_URL, "page": 105},
    "الملحق 9: كرة اللياقة": {"url": APPX_BOOK_URL, "page": 127},
    "الملحق 10: الكرة الطبية": {"url": APPX_BOOK_URL, "page": 155},
    "الملحق 11: الأثقال الحرة": {"url": APPX_BOOK_URL, "page": 167},
    "الملحق 12: أحزمة التعلق (TRX)": {"url": APPX_BOOK_URL, "page": 179},
    "الملحق 13: حبال القوة القتالية": {"url": APPX_BOOK_URL, "page": 211},
    "الملحق 14: جرس الكيتل بيل": {"url": APPX_BOOK_URL, "page": 227}
}

# --- 4. القائمة ---
st.sidebar.header("محتويات الكتاب") # تم إعادة العنوان
selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))

# --- 5. العرض ---
chapter_data = chapters[selected_chapter]
final_url = f"{chapter_data['url']}#page={chapter_data['page']}"

# استخدام key=selected_chapter لإجبار الإطار على إعادة التحميل
components.html(
    f"""<iframe src="{final_url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
    height=620,
    key=selected_chapter 
)

# الأداة (بقية الكود كما هو...)
if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي</h2>", unsafe_allow_html=True)
    # (بقية كود النموذج...)
