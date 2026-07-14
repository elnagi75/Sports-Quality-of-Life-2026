import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS المُعالج ---
st.markdown("""
<style>
    .stApp { direction: rtl; font-family: 'Arial', sans-serif; }
    [data-testid="stSidebar"] { direction: rtl; }
    [data-testid="collapsedControl"], [data-testid="stHeader"] { direction: ltr; }
    h1, h2, h3, p, label, .stMarkdown { text-align: right !important; }
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

# --- 4. الفهرس الشامل (بروابط مستقلة لكل قسم) ---
chapters = {
    "محتويات الكتاب": {"url": "https://heyzine.com/flip-book/faddab62a3.html", "img": "intro.jpg"},
    "الفصل الأول: هندسة الحركة البشرية": {"url": "https://heyzine.com/flip-book/d09ee1dab9.html", "img": "ch_1.jpg"},
    "الفصل الثاني: فسيولوجيا الجهد": {"url": "https://heyzine.com/flip-book/f059fd3aa1.html", "img": "ch_2.jpg"},
    "الفصل الثالث: القياسات الجسمية": {"url": "https://heyzine.com/flip-book/ed691a91e8.html", "img": "ch_3.jpg"},
    "الفصل الرابع: اللياقة القلبية": {"url": "https://heyzine.com/flip-book/f0b14c7b98.html", "img": "ch_4.jpg"},
    "الفصل الخامس: القوة والتحمل": {"url": "https://heyzine.com/flip-book/7e2edd61fa.html", "img": "ch_5.jpg"},
    "الفصل السادس: المرونة": {"url": "https://heyzine.com/flip-book/4bff7c4ee8.html", "img": "ch_6.jpg"},
    "الفصل السابع: اللياقة المهارية": {"url": "https://heyzine.com/flip-book/f792a88385.html", "img": "ch_7.jpg"},
    "الفصل الثامن: مبادئ التدريب": {"url": "https://heyzine.com/flip-book/0431dd6c91.html", "img": "ch_8.jpg"},
    "الفصل التاسع: أنظمة تدريب القوة": {"url": "https://heyzine.com/flip-book/49d7104e27.html", "img": "ch_9.jpg"},
    "الفصل العاشر: التدريب الذكي": {"url": "https://heyzine.com/flip-book/5e12e6f633.html", "img": "ch_10.jpg"},
    "الفصل الحادي عشر: التغذية": {"url": "https://heyzine.com/flip-book/a32eabe8e2.html", "img": "ch_11.jpg"},
    "الفصل الثاني عشر: خرافات اللياقة": {"url": "https://heyzine.com/flip-book/ee76aa64b6.html", "img": "ch_12.jpg"},
    
    "الملحق 1: المشي والجري": {"url": "https://heyzine.com/flip-book/2e9b1604e3.html", "img": "appx_1.jpg"},
    "الملحق 2: التدريب بوزن الجسم": {"url": "https://heyzine.com/flip-book/41501d648f.html", "img": "appx_2.jpg"},
    "الملحق 3: حبل الوثب": {"url": "https://heyzine.com/flip-book/f1bc76d144.html", "img": "appx_3.jpg"},
    "الملحق 4: صندوق الخطو": {"url": "https://heyzine.com/flip-book/4e4df20d4d.html", "img": "appx_4.jpg"},
    "الملحق 5: عقلة الباب": {"url": "https://heyzine.com/flip-book/ecccacca58.html", "img": "appx_5.jpg"},
    "الملحق 6: أحزمة المقاومة المطاطية": {"url": "https://heyzine.com/flip-book/cfcc0549ca.html", "img": "appx_6.jpg"},
    "الملحق 7: سلم التوافق": {"url": "https://heyzine.com/flip-book/971b5b5cab.html", "img": "appx_7.jpg"},
    "الملحق 8: أطواق اللياقة": {"url": "https://heyzine.com/flip-book/288b61af8e.html", "img": "appx_8.jpg"},
    "الملحق 9: كرة اللياقة": {"url": "https://heyzine.com/flip-book/5028381119.html", "img": "appx_9.jpg"},
    "الملحق 10: الكرة الطبية": {"url": "https://heyzine.com/flip-book/65288cb346.html", "img": "appx_10.jpg"},
    "الملحق 11: الأثقال الحرة": {"url": "https://heyzine.com/flip-book/93b1b05123.html", "img": "appx_11.jpg"},
    "الملحق 12: أحزمة التعلق (TRX)": {"url": "https://heyzine.com/flip-book/af0a057c69.html", "img": "appx_12.jpg"},
    "الملحق 13: حبال القوة القتالية": {"url": "https://heyzine.com/flip-book/d1599fe763.html", "img": "appx_13.jpg"},
    "الملحق 14: جرس الكيتل بيل": {"url": "https://heyzine.com/flip-book/4451c715f9.html", "img": "appx_14.jpg"},
    
    "قائمة المراجع والمصادر المساندة": {"url": "https://heyzine.com/flip-book/f2a541bb0b.html", "img": "ref.jpg"}
}

# --- 5. القائمة الجانبية (Sidebar) ---
st.sidebar.header("محتويات الكتاب")

image_container = st.sidebar.empty()
selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))

# جلب بيانات الاختيار
chapter_data = chapters[selected_chapter]

if os.path.exists(chapter_data["img"]):
    image_container.image(chapter_data["img"], use_column_width=True)
else:
    image_container.warning(f"مساحة محجوزة لغلاف: {chapter_data['img']}")
st.sidebar.markdown("---")

# --- 6. عرض الكتب والأدوات التفاعلية ---
st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")

# العرض المباشر والنظيف للرابط
components.html(
    f"""<iframe src="{chapter_data['url']}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>""",
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
