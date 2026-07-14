import streamlit as st
import streamlit.components.v1 as components
import os
import time

# --- 1. الإعدادات الأساسية للمنصة ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS المُعالج ---
st.markdown("""
<style>
    .stApp {
        direction: rtl;
        font-family: 'Arial', sans-serif;
    }
    [data-testid="stSidebar"] {
        direction: rtl;
    }
    [data-testid="collapsedControl"], [data-testid="stHeader"] {
        direction: ltr;
    }
    h1, h2, h3, p, label, .stMarkdown {
        text-align: right !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .lab-title {
        color: #2E86C1;
        text-align: center !important;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #2E86C1;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    .stRadio label, .stMultiSelect label { font-size: 18px !important; font-weight: bold; }
    .stButton button { font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; padding: 10px !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# الروابط الرئيسية للكتب
MAIN_BOOK_URL = "https://heyzine.com/flip-book/248efb967c.html"
APPX_BOOK_URL = "https://heyzine.com/flip-book/e18c597993.html"

# --- 4. الفهرس الشامل (مع أرقام القفز التلقائي للصفحات) ---
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

# --- 5. القائمة الجانبية (Sidebar) ---
st.sidebar.header("محتويات الكتاب") # تم التعديل كما تفضلت

image_container = st.sidebar.empty()
selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))

# جلب بيانات الفصل المختار
chapter_data = chapters[selected_chapter]

if os.path.exists(chapter_data["img"]):
    image_container.image(chapter_data["img"], use_column_width=True)
else:
    image_container.warning(f"مساحة محجوزة لغلاف: {chapter_data['img']}")
st.sidebar.markdown("---")

# --- 6. عرض الكتب والأدوات التفاعلية ---

st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")

# بناء الرابط النهائي مع متغير زمني لكسر الذاكرة المؤقتة وإجبار الإطار على تحديث الصفحة
timestamp = int(time.time())
final_url = f"{chapter_data['url']}?t={timestamp}#page={chapter_data['page']}"

components.html(
    f"""<iframe src="{final_url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
    height=620
)

# عرض الأداة التفاعلية حصراً مع الفصل الأول
if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي: استمارة التحليل الذاتي (مهمة تطبيقية)</h2>", unsafe_allow_html=True)
    st.write("📌 **تعليمات:** قف أمام المرآة وسجل ملاحظاتك بصدق. (يُرجى تحديد خيار واحد من كل عنصر، الدوائر فارغة افتراضياً لضمان دقة اختيارك).")
    
    with st.form("posture_lab_form"):
        st.subheader("أولاً: الفحص البصري (Check Point)")
        col1, col2 = st.columns(2)
        
        with col1:
            head = st.radio("الرأس والرقبة:", ["متعامد مع الكتف (طبيعي)", "مائل للأمام (Forward Head)"], index=None)
            upper_back = st.radio("أعلى الظهر:", ["مسطح طبيعي", "محدب (Kyphosis)"], index=None)
            pelvis = st.radio("الحوض:", ["متساوي الجانبين", "مائل لجهة واحدة"], index=None)
            
        with col2:
            shoulders = st.radio("الكتفان:", ["متساويان", "أحدهما أعلى من الآخر"], index=None)
            lower_back = st.radio("أسفل الظهر:", ["انحناء طبيعي", "مقعر بشدة (Lordosis)", "مسطح (Flat Back)"], index=None)
            
        st.subheader("ثانياً: العادات والمسببات (Analysis)")
        habits = st.multiselect("اختر العادات التي تمارسها يومياً (يمكنك اختيار أكثر من واحدة):", 
                                ["استخدام الهاتف بكثرة وبوضع انحناء", "حمل الحقيبة على كتف واحد", "الجلوس الخاطئ لفترات طويلة", "قلة ممارسة التمارين الرياضية"])
        
        submit_btn = st.form_submit_button("استخراج الخطة التصحيحية الهندسية")
        
        if submit_btn:
            if None in [head, upper_back, pelvis, shoulders, lower_back]:
                st.error("⚠️ خطأ: الرجاء تحديد خيار في جميع عناصر الفحص البصري قبل استخراج الخطة.")
            else:
                st.success("✅ تم تحليل البيانات ميكانيكياً بنجاح! إليك خطتك التصحيحية:")
                
                if head == "مائل للأمام (Forward Head)" or upper_back == "محدب (Kyphosis)":
                    st.warning("⚠️ **تشخيص:** لديك مؤشرات لـ (متلازمة التقاطع العلوي - Upper Crossed Syndrome).")
                    st.write("**الخطة:**")
                    st.write("- **عضلات تحتاج إطالة (مشدودة):** عضلات الصدر وأعلى الرقبة الخلفية.")
                    st.write("- **عضلات تحتاج تقوية (ضعيفة):** عضلات أعلى الظهر (بين اللوحين) وعضلات الرقبة الأمامية العميقة.")
                    st.write("- **تطبيق عملي فوري:** قم بتمرين (Chin Tuck) لمدة 10 ثوانٍ 3 مرات يومياً لفك الضغط عن الرقبة.")
                    
                if lower_back == "مقعر بشدة (Lordosis)":
                    st.warning("⚠️ **تشخيص:** زيادة في التقعر القطني (Lordosis).")
                    st.write("**الخطة:** تقوية عضلات البطن (Core) وإطالة عضلات الفخذ الأمامية.")
                elif lower_back == "مسطح (Flat Back)":
                    st.warning("⚠️ **تشخيص:** ظهر مسطح (Flat Back) وفقدان الانحناء الطبيعي.")
                    st.write("**الخطة:** تجنب الجلوس بظهر مرتخٍ، وقم بتمارين مرونة أسفل الظهر.")
                
                if shoulders == "أحدهما أعلى من الآخر" or pelvis == "مائل لجهة واحدة":
                    st.warning("⚠️ **تشخيص:** عدم توازن جانبي (ميكانيكا السلسلة الحركية متأثرة).")
                    if "حمل الحقيبة على كتف واحد" in habits:
                        st.write("**الخطة:** تجنب حمل الحقيبة على كتف واحد فوراً، قم بتمارين الإطالة الجانبية لتصحيح التوازن العضلي.")
                
                if head == "متعامد مع الكتف (طبيعي)" and upper_back == "مسطح طبيعي" and lower_back == "انحناء طبيعي" and shoulders == "متساويان" and pelvis == "متساوي الجانبين":
                    st.info("🌟 **تشخيص:** قوامك الهندسي متزن وممتاز! حافظ على عاداتك الجيدة واستمر في ممارسة الرياضة.")
