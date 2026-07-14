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
    
    /* إخفاء الحروف العربية المتقطعة عند طي القائمة الجانبية */
    [data-testid="collapsedControl"] span { display: none !important; }
    
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
    
    /* تنسيق خاص ومكبر لسطر التعليمات */
    .instruction-text {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #1a5276 !important;
        background-color: #eaf2f8;
        padding: 15px;
        border-radius: 8px;
        border-right: 6px solid #2E86C1;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    
    .stRadio label, .stMultiSelect label, .stSelectbox label { font-size: 18px !important; font-weight: bold; }
    .stNumberInput label { font-size: 18px !important; font-weight: bold; }
    .stButton button { font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; padding: 10px !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# --- 4. الفهرس الشامل للروابط ---
chapters = {
    "محتويات الكتاب": "https://heyzine.com/flip-book/faddab62a3.html",
    "الفصل الأول: هندسة الحركة البشرية": "https://heyzine.com/flip-book/d09ee1dab9.html",
    "الفصل الثاني: فسيولوجيا الجهد": "https://heyzine.com/flip-book/f059fd3aa1.html",
    "الفصل الثالث: القياسات الجسمية": "https://heyzine.com/flip-book/ed691a91e8.html",
    "الفصل الرابع: اللياقة القلبية": "https://heyzine.com/flip-book/f0b14c7b98.html",
    "الفصل الخامس: القوة والتحمل": "https://heyzine.com/flip-book/7e2edd61fa.html",
    "الفصل السادس: المرونة": "https://heyzine.com/flip-book/4bff7c4ee8.html",
    "الفصل السابع: اللياقة المهارية": "https://heyzine.com/flip-book/f792a88385.html",
    "الفصل الثامن: مبادئ التدريب": "https://heyzine.com/flip-book/0431dd6c91.html",
    "الفصل التاسع: أنظمة تدريب القوة": "https://heyzine.com/flip-book/49d7104e27.html",
    "الفصل العاشر: التدريب الذكي": "https://heyzine.com/flip-book/5e12e6f633.html",
    "الفصل الحادي عشر: التغذية": "https://heyzine.com/flip-book/a32eabe8e2.html",
    "الفصل الثاني عشر: خرافات اللياقة": "https://heyzine.com/flip-book/ee76aa64b6.html",
    "الملحق 1: المشي والجري": "https://heyzine.com/flip-book/2e9b1604e3.html",
    "الملحق 2: التدريب بوزن الجسم": "https://heyzine.com/flip-book/41501d648f.html",
    "الملحق 3: حبل الوثب": "https://heyzine.com/flip-book/f1bc76d144.html",
    "الملحق 4: صندوق الخطو": "https://heyzine.com/flip-book/4e4df20d4d.html",
    "الملحق 5: عقلة الباب": "https://heyzine.com/flip-book/ecccacca58.html",
    "الملحق 6: أحزمة المقاومة المطاطية": "https://heyzine.com/flip-book/cfcc0549ca.html",
    "الملحق 7: سلم التوافق": "https://heyzine.com/flip-book/971b5b5cab.html",
    "الملحق 8: أطواق اللياقة": "https://heyzine.com/flip-book/288b61af8e.html",
    "الملحق 9: كرة اللياقة": "https://heyzine.com/flip-book/5028381119.html",
    "الملحق 10: الكرة الطبية": "https://heyzine.com/flip-book/65288cb346.html",
    "الملحق 11: الأثقال الحرة": "https://heyzine.com/flip-book/93b1b05123.html",
    "الملحق 12: أحزمة التعلق (TRX)": "https://heyzine.com/flip-book/af0a057c69.html",
    "الملحق 13: حبال القوة القتالية": "https://heyzine.com/flip-book/d1599fe763.html",
    "الملحق 14: جرس الكيتل بيل": "https://heyzine.com/flip-book/4451c715f9.html",
    "قائمة المراجع والمصادر المساندة": "https://heyzine.com/flip-book/f2a541bb0b.html"
}

# --- 5. القائمة الجانبية (Sidebar) ---
st.sidebar.header("محتويات الكتاب")

# تثبيت الغلاف الرئيسي فقط بشكل دائم أعلى القائمة
if os.path.exists("intro.jpg"):
    st.sidebar.image("intro.jpg", use_column_width=True)
else:
    st.sidebar.info("مساحة الغلاف الرئيسي للكتاب (يرجى رفع ملف intro.jpg)")

selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))
st.sidebar.markdown("---")

# --- 6. عرض الكتب والأدوات التفاعلية ---
st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")

# العرض المباشر للرابط مع قفل الحماية (sandbox)
components.html(
    f"""<iframe src="{chapters[selected_chapter]}" width="100%" height="600" frameborder="0" allowfullscreen sandbox="allow-scripts allow-same-origin allow-popups"></iframe>""",
    height=620
)

# --------------------------------------------------------------------------------
# --- 7. المختبرات التفاعلية (Tools) ---
# --------------------------------------------------------------------------------

# الفصل الأول: مختبر القوام
if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي: استمارة التحليل الذاتي</h2>", unsafe_allow_html=True)
    
    # سطر التعليمات المكبر مع ذكر رقم الصفحة
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً للمهام الواردة في صـ 7): قف أمام المرآة وسجل ملاحظاتك بصدق. (يُرجى تحديد خيار واحد من كل عنصر، الدوائر فارغة افتراضياً لضمان دقة اختيارك).</div>", unsafe_allow_html=True)
    
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

# الفصل الثاني: مختبر فسيولوجيا الجهد (حاسبة النبض)
elif selected_chapter == "الفصل الثاني: فسيولوجيا الجهد":
    st.markdown("<h2 class='lab-title'>🫀 مختبر فسيولوجيا الجهد: حاسبة النبض المستهدف</h2>", unsafe_allow_html=True)
    
    # سطر التعليمات المكبر مع ذكر رقم الصفحة
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمعادلة كارفونين في صـ 18): أدخل بياناتك الفسيولوجية بدقة لحساب النطاق الأمثل لنبض قلبك أثناء التدريب لتحقيق هدفك بفاعلية.</div>", unsafe_allow_html=True)
    
    with st.form("karvonen_lab_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("العمر (بالسنوات):", min_value=10, max_value=100, value=20, step=1)
        with col2:
            resting_hr = st.number_input("معدل النبض وقت الراحة (نبضة/دقيقة):", min_value=40, max_value=120, value=70, step=1)
            
        goal = st.selectbox("حدد الهدف من التدريب (Target Zone):", [
            "الاستشفاء وحرق الدهون الأساسي (50% - 60%)",
            "تحسين اللياقة القلبية التنفسية والتخسيس (60% - 70%)",
            "تطوير الأداء الرياضي (المنطقة الهوائية) (70% - 80%)",
            "الحد الأقصى (اللاهوائي) (80% - 90%)"
        ])
        
        submit_btn = st.form_submit_button("حساب مناطق التدريب (المعالجة الرياضية)")
        
        if submit_btn:
            # المعالجة الرياضية للمعادلات
            max_hr = 220 - age
            hr_reserve = max_hr - resting_hr
            
            # تحديد النسب المئوية بناءً على الاختيار
            if "50%" in goal:
                min_int, max_int = 0.50, 0.60
            elif "60%" in goal:
                min_int, max_int = 0.60, 0.70
            elif "70%" in goal:
                min_int, max_int = 0.70, 0.80
            else:
                min_int, max_int = 0.80, 0.90
                
            target_min = int((hr_reserve * min_int) + resting_hr)
            target_max = int((hr_reserve * max_int) + resting_hr)
            
            # عرض النتائج
            st.success("✅ تم تحليل استجابتك الفسيولوجية بنجاح! إليك تقريرك العلمي:")
            st.write(f"📊 **أقصى معدل لضربات القلب (Max HR):** {max_hr} نبضة/دقيقة.")
            st.write(f"🫀 **احتياطي ضربات القلب (HR Reserve):** {hr_reserve} نبضة/دقيقة.")
            st.info(f"🎯 **نطاق النبض المستهدف لتحقيق هدفك:** يجب أن تحافظ على نبضك بين **{target_min}** و **{target_max}** نبضة/دقيقة أثناء التمرين.")
