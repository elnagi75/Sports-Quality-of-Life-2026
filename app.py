import streamlit as st
import streamlit.components.v1 as components
import os

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
    
    /* تنسيق خاص لعنوان الأداة السفلية ليكون بارزاً */
    .lab-title {
        color: #2E86C1;
        text-align: center !important;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #2E86C1;
        margin-top: 30px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# --- 4. الفهرس ---
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

# --- 5. القائمة الجانبية ---
st.sidebar.header("محتويات الكتاب")
image_container = st.sidebar.empty()
selected_chapter = st.sidebar.radio("اختر الفصل للبدء:", list(chapters.keys()))

image_name = chapters[selected_chapter]
if os.path.exists(image_name):
    image_container.image(image_name, use_column_width=True)
else:
    image_container.warning(f"مساحة محجوزة لغلاف: {image_name}")
st.sidebar.markdown("---")

# --- 6. دوال العرض الخاصة بكل فصل ---

def render_intro():
    st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")
    components.html(
        """<iframe src="https://heyzine.com/flip-book/8107d3f1a1.html" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
        height=620
    )

def render_chapter_1():
    # 1. عرض الكتاب التفاعلي (Heyzine)
    st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)**.")
    components.html(
        """<iframe src="https://heyzine.com/flip-book/cfea6877c0.html" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
        height=620
    )
    
    # 2. الأداة السفلية: مختبر القوام الرقمي
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي: استمارة التحليل الذاتي (مهمة تطبيقية)</h2>", unsafe_allow_html=True)
    st.write("بناءً على ما درسته في الفصل الأول (قاعدة الوصلات المترابطة ومتلازمة التقاطع العلوي)، قف أمام المرآة وسجل ملاحظاتك بصدق للحصول على خطتك التصحيحية.")
    
    with st.form("posture_lab_form"):
        st.subheader("أولاً: الفحص البصري (Check Point)")
        col1, col2 = st.columns(2)
        
        with col1:
            head = st.radio("الرأس والرقبة:", ["متعامد مع الكتف (طبيعي)", "مائل للأمام (Forward Head)"])
            upper_back = st.radio("أعلى الظهر:", ["مسطح طبيعي", "محدب (Kyphosis)"])
            pelvis = st.radio("الحوض:", ["متساوي الجانبين", "مائل لجهة واحدة"])
            
        with col2:
            shoulders = st.radio("الكتفان:", ["متساويان", "أحدهما أعلى من الآخر"])
            lower_back = st.radio("أسفل الظهر:", ["انحناء طبيعي", "مقعر بشدة (Lordosis)", "مسطح (Flat Back)"])
            
        st.subheader("ثانياً: العادات والمسببات (Analysis)")
        habits = st.multiselect("اختر العادات التي تمارسها يومياً:", 
                                ["استخدام الهاتف بكثرة وبوضع انحناء", "حمل الحقيبة على كتف واحد", "الجلوس الخاطئ لفترات طويلة", "قلة ممارسة التمارين الرياضية"])
        
        submit_btn = st.form_submit_button("استخراج الخطة التصحيحية الهندسية")
        
        if submit_btn:
            st.success("✅ تم تحليل البيانات ميكانيكياً بنجاح! إليك خطتك التصحيحية:")
            
            # تحليل الرقبة وأعلى الظهر (متلازمة التقاطع العلوي)
            if head == "مائل للأمام (Forward Head)" or upper_back == "محدب (Kyphosis)":
                st.warning("⚠️ **تشخيص:** لديك مؤشرات لـ (متلازمة التقاطع العلوي - Upper Crossed Syndrome).")
                st.write("**الخطة:**")
                st.write("- **عضلات تحتاج إطالة (مشدودة):** عضلات الصدر وأعلى الرقبة الخلفية.")
                st.write("- **عضلات تحتاج تقوية (ضعيفة):** عضلات أعلى الظهر (بين اللوحين) وعضلات الرقبة الأمامية العميقة.")
                st.write("- **تطبيق عملي فوري:** قم بتمرين (Chin Tuck) لمدة 10 ثوانٍ 3 مرات يومياً لفك الضغط عن الرقبة.")
                
            # تحليل أسفل الظهر والحوض
            if lower_back == "مقعر بشدة (Lordosis)":
                st.warning("⚠️ **تشخيص:** زيادة في التقعر القطني (Lordosis).")
                st.write("**الخطة:** تقوية عضلات البطن (Core) وإطالة عضلات الفخذ الأمامية.")
            
            if shoulders == "أحدهما أعلى من الآخر" or pelvis == "مائل لجهة واحدة":
                st.warning("⚠️ **تشخيص:** عدم توازن جانبي (ميكانيكا السلسلة الحركية متأثرة).")
                if "حمل الحقيبة على كتف واحد" in habits:
                    st.write("**الخطة:** تجنب حمل الحقيبة على كتف واحد فوراً، قم بتمارين الإطالة الجانبية لتصحيح التوازن العضلي.")
            
            if head == "متعامد مع الكتف (طبيعي)" and upper_back == "مسطح طبيعي" and lower_back == "انحناء طبيعي" and shoulders == "متساويان" and pelvis == "متساوي الجانبين":
                st.info("🌟 **تشخيص:** قوامك الهندسي متزن وممتاز! حافظ على عاداتك الجيدة واستمر في ممارسة الرياضة.")

def render_placeholder(chapter_title):
    st.subheader(chapter_title)
    st.info(f"محتوى '{chapter_title}' قيد التجهيز... سيتم بناؤه لاحقاً خطوة بخطوة.")

# --- 7. الموجه الديناميكي (Router) ---
if selected_chapter == "محتويات الكتاب":
    render_intro()
elif selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    render_chapter_1()
else:
    render_placeholder(selected_chapter)
