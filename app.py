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
    
    /* تنسيق خاص لعنوان الأداة السفلية */
    .lab-title {
        color: #2E86C1;
        text-align: center !important;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #2E86C1;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    /* تكبير خطوط الأسئلة والاختيارات داخل الأداة */
    .stRadio label {
        font-size: 18px !important;
        font-weight: bold;
    }
    .stMultiSelect label {
        font-size: 18px !important;
        font-weight: bold;
    }
    .stButton button {
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# --- 4. الهيكل الشامل للفهرس (مقسم إلى قسمين) ---
book_sections = {
    "📖 الكتاب الأساسي (الفصول)": {
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
        "الفصل الثاني عشر: خرافات اللياقة": "ch_12.jpg"
    },
    "🏋️ الموسوعة العملية (الملحقات)": {
        "الملحق 1: المشي والجري": "appx_1.jpg",
        "الملحق 2: التدريب بوزن الجسم": "appx_2.jpg",
        "الملحق 3: حبل الوثب": "appx_3.jpg",
        "الملحق 4: صندوق الخطو": "appx_4.jpg",
        "الملحق 5: عقلة الباب": "appx_5.jpg",
        "الملحق 6: أحزمة المقاومة المطاطية": "appx_6.jpg",
        "الملحق 7: سلم التوافق": "appx_7.jpg",
        "الملحق 8: أطواق اللياقة": "appx_8.jpg",
        "الملحق 9: كرة اللياقة": "appx_9.jpg",
        "الملحق 10: الكرة الطبية": "appx_10.jpg",
        "الملحق 11: الأثقال الحرة": "appx_11.jpg",
        "الملحق 12: أحزمة التعلق (TRX)": "appx_12.jpg",
        "الملحق 13: حبال القوة القتالية": "appx_13.jpg",
        "الملحق 14: جرس الكيتل بيل": "appx_14.jpg"
    }
}

# --- 5. القائمة الجانبية (Sidebar) ---
st.sidebar.header("تصفح المنصة")

# اختيار القسم الرئيسي (لتخفيف الزحام في القائمة)
selected_section = st.sidebar.selectbox("حدد القسم:", list(book_sections.keys()))
st.sidebar.markdown("---")

# مساحة لصورة الغلاف بناءً على الاختيار
image_container = st.sidebar.empty()

# عرض الفصول التابعة للقسم المختار فقط
selected_chapter = st.sidebar.radio(f"اختر من {selected_section.split(' ')[1]}:", list(book_sections[selected_section].keys()))

# تحديث صورة الغلاف
image_name = book_sections[selected_section][selected_chapter]
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
    st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)**.")
    components.html(
        """<iframe src="https://heyzine.com/flip-book/cfea6877c0.html" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
        height=620
    )
    
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

def render_placeholder(chapter_title):
    st.subheader(chapter_title)
    st.info(f
