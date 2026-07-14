import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS المُعالج والفاخر ---
st.markdown("""
<style>
    /* التوجيه والخطوط */
    .stApp { direction: rtl; font-family: 'Arial', sans-serif; }
    [data-testid="stSidebar"] { direction: rtl; }
    [data-testid="collapsedControl"], [data-testid="stHeader"] { direction: ltr; }
    
    /* إخفاء الحروف المتقطعة في زر الطي */
    [data-testid="collapsedControl"] span { display: none !important; }
    
    h1, h2, h3, p, label, .stMarkdown { text-align: right !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* عنوان المختبر */
    .lab-title {
        color: #2E86C1;
        text-align: center !important;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #2E86C1;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    /* سطر التعليمات (الأزرق) */
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
    
    /* تكبير وتلوين العناوين الرئيسية للأسئلة (كحلي داكن) */
    .stRadio > label, .stMultiSelect > label, .stSelectbox > label, .stNumberInput > label { 
        font-size: 24px !important; 
        font-weight: bold !important; 
        color: #1a5276 !important; 
    }
    
    /* إبهار بصري: تكبير وتلوين الخيارات نفسها بلون أخضر زمردي مميز */
    div[role="radiogroup"] label p, div[data-baseweb="select"] span, div[data-baseweb="checkbox"] label p {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #117A65 !important; 
    }
    
    /* زر الإرسال */
    .stButton button { 
        font-size: 20px !important; 
        font-weight: bold !important; 
        border-radius: 8px !important; 
        padding: 10px !important; 
        width: 100%;
        background-color: #2E86C1;
        color: white;
    }
    .stButton button:hover {
        background-color: #1a5276;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. الترويسة الرئيسية ---
st.title("الرياضة وجودة الحياة (دليل التطبيق الذاتي)")
st.markdown("---")

# --- 4. الفهرس الشامل (الروابط المستقلة) ---
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
if os.path.exists("intro.jpg"):
    st.sidebar.image("intro.jpg", use_column_width=True)
else:
    st.sidebar.info("مساحة الغلاف الرئيسي للكتاب (يرجى رفع ملف intro.jpg)")

selected_chapter = st.sidebar.radio("اختر الفصل أو الملحق:", list(chapters.keys()))
st.sidebar.markdown("---")

# --- 6. عرض الكتب والأدوات التفاعلية ---
st.info("📱 **تنويه لمستخدمي الهواتف الذكية:** لتصفح صفحات الكتاب بسلاسة، يُرجى الضغط على أيقونة **التكبير (Fullscreen)** الموجودة داخل إطار العرض.")

# عرض الكتاب مع السماح بروابط يوتيوب (popups و top-navigation) مع منع توجيه المنصة الأساسية
components.html(
    f"""<iframe src="{chapters[selected_chapter]}" width="100%" height="600" frameborder="0" allowfullscreen sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation"></iframe>""",
    height=620
)

# ==============================================================================
# --- 7. قسم المختبرات التفاعلية (12 مختبراً) ---
# ==============================================================================

if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي: استمارة التحليل الذاتي</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً للمهام الواردة في صـ 7): قف أمام المرآة وسجل ملاحظاتك بصدق. (يُرجى تحديد خيار واحد من كل عنصر).</div>", unsafe_allow_html=True)
    
    with st.form("lab1"):
        col1, col2 = st.columns(2)
        with col1:
            head = st.radio("الرأس والرقبة:", ["متعامد مع الكتف (طبيعي)", "مائل للأمام (Forward Head)"])
            upper_back = st.radio("أعلى الظهر:", ["مسطح طبيعي", "محدب (Kyphosis)"])
        with col2:
            shoulders = st.radio("الكتفان:", ["متساويان", "أحدهما أعلى من الآخر"])
            lower_back = st.radio("أسفل الظهر:", ["انحناء طبيعي", "مقعر بشدة (Lordosis)", "مسطح (Flat Back)"])
            
        habits = st.multiselect("اختر العادات اليومية:", ["استخدام الهاتف بكثرة بانحناء", "حمل الحقيبة على كتف واحد", "الجلوس الخاطئ", "قلة الحركة"])
        if st.form_submit_button("استخراج الخطة التصحيحية"):
            st.success("✅ تم التحليل الميكانيكي!")
            if "مائل للأمام" in head or "محدب" in upper_back:
                st.warning("⚠️ **تشخيص:** مؤشرات لمتلازمة التقاطع العلوي. تحتاج لتقوية عضلات أعلى الظهر وإطالة عضلات الصدر والرقبة.")
            if "مقعر" in lower_back:
                st.warning("⚠️ **تشخيص:** زيادة التقعر القطني. تحتاج لتقوية عضلات البطن (Core) وإطالة عضلات الفخذ الأمامية.")
            if "طبيعي" in head and "طبيعي" in upper_back and "طبيعي" in lower_back:
                st.info("🌟 قوامك متزن! استمر في نشاطك.")

elif selected_chapter == "الفصل الثاني: فسيولوجيا الجهد":
    st.markdown("<h2 class='lab-title'>🫀 مختبر فسيولوجيا الجهد: حاسبة النبض المستهدف</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمعادلة كارفونين في صـ 18): أدخل بياناتك لحساب النطاق الأمثل لنبض قلبك أثناء التدريب.</div>", unsafe_allow_html=True)
    
    with st.form("lab2"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("العمر (بالسنوات):", min_value=10, max_value=100, value=20)
        with col2:
            resting_hr = st.number_input("النبض وقت الراحة (نبضة/دقيقة):", min_value=40, max_value=120, value=70)
        goal = st.selectbox("الهدف من التدريب:", ["الاستشفاء وحرق الدهون (50% - 60%)", "اللياقة القلبية والتخسيس (60% - 70%)", "تطوير الأداء الرياضي (70% - 80%)", "الحد الأقصى اللاهوائي (80% - 90%)"])
        if st.form_submit_button("حساب مناطق التدريب"):
            max_hr = 220 - age
            hr_reserve = max_hr - resting_hr
            min_int, max_int = (0.5, 0.6) if "50%" in goal else (0.6, 0.7) if "60%" in goal else (0.7, 0.8) if "70%" in goal else (0.8, 0.9)
            t_min, t_max = int((hr_reserve * min_int) + resting_hr), int((hr_reserve * max_int) + resting_hr)
            
            st.success("✅ التقرير الفسيولوجي:")
            st.write(f"📊 أقصى معدل لضربات القلب = 220 - العمر = **{max_hr}** نبضة/دقيقة.")
            st.info(f"🎯 **النبض المستهدف لتحقيق هدفك:** من **{t_min}** إلى **{t_max}** نبضة/دقيقة.")

elif selected_chapter == "الفصل الثالث: القياسات الجسمية":
    st.markdown("<h2 class='lab-title'>⚖️ مختبر تحليل تركيب الجسم ونمطه</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمهام التقييم في صـ 30): أدخل قياساتك لتقييم صحة تركيبك الجسماني.</div>", unsafe_allow_html=True)
    
    with st.form("lab3"):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("الوزن (كجم):", min_value=30.0, max_value=200.0, value=70.0)
            height_cm = st.number_input("الطول (سم):", min_value=100.0, max_value=220.0, value=170.0)
        with col2:
            waist = st.number_input("محيط الخصر (سم):", min_value=40.0, max_value=150.0, value=80.0)
            hip = st.number_input("محيط الحوض (سم):", min_value=40.0, max_value=150.0, value=90.0)
        if st.form_submit_button("تحليل البيانات"):
            height_m = height_cm / 100
            bmi = round(weight / (height_m * height_m), 1)
            whr = round(waist / hip, 2)
            
            st.success("✅ تقرير تركيب الجسم:")
            st.write(f"📊 مؤشر كتلة الجسم = الوزن ÷ (الطول × الطول) = **{bmi}**")
            st.write(f"📊 نسبة الخصر للحوض = محيط الخصر ÷ محيط الحوض = **{whr}**")
            if bmi < 18.5: st.warning("النتيجة: نحافة.")
            elif 18.5 <= bmi <= 24.9: st.info("النتيجة: وزن مثالي وصحي.")
            else: st.warning("النتيجة: وزن زائد (يجب ضبط النظام الغذائي).")

elif selected_chapter == "الفصل الرابع: اللياقة القلبية":
    st.markdown("<h2 class='lab-title'>🫁 محلل كفاءة المحرك القلبي (اختبار كوبر)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار كوبر في صـ 42): أدخل المسافة المقطوعة (بالمتر) خلال 12 دقيقة جري/مشي لتقدير كفاءة استهلاك الأكسجين.</div>", unsafe_allow_html=True)
    
    with st.form("lab4"):
        distance = st.number_input("المسافة المقطوعة (بالمتر):", min_value=500, max_value=4000, value=2000)
        if st.form_submit_button("حساب السعة الهوائية (VO2max)"):
            vo2max = round((distance - 504.9) / 44.73, 1)
            st.success("✅ التقرير القلبي التنفسي:")
            st.write(f"📊 الحد الأقصى لاستهلاك الأكسجين (VO2max) = (المسافة - 504.9) ÷ 44.73 = **{vo2max}** مل/كجم/دقيقة.")
            if vo2max < 30: st.warning("التصنيف: ضعيف (تحتاج للبدء ببرنامج مشي منتظم).")
            elif 30 <= vo2max < 40: st.info("التصنيف: متوسط.")
            else: st.success("التصنيف: ممتاز (كفاءة قلبية عالية).")

elif selected_chapter == "الفصل الخامس: القوة والتحمل":
    st.markdown("<h2 class='lab-title'>🦾 مقياس التحمل وتوقع القوة القصوى (1RM)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمعادلة القوة في صـ 55): أدخل الوزن الذي تدربت به وعدد التكرارات لحساب أقصى وزن يمكن رفعه لمرة واحدة.</div>", unsafe_allow_html=True)
    
    with st.form("lab5"):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("الوزن المستخدم (كجم):", min_value=1, max_value=300, value=50)
        with col2:
            reps = st.number_input("عدد التكرارات المنجزة:", min_value=1, max_value=20, value=8)
        if st.form_submit_button("حساب القوة القصوى"):
            one_rm = round(weight + (weight * reps / 30), 1)
            st.success("✅ تقرير القوة العضلية:")
            st.write(f"📊 القوة القصوى (1RM) = الوزن + (الوزن × التكرارات ÷ 30) = **{one_rm}** كجم.")
            st.info("💡 لتدريب الضخامة: استخدم أوزاناً تتراوح بين 70% إلى 80% من هذا الرقم.")

elif selected_chapter == "الفصل السادس: المرونة":
    st.markdown("<h2 class='lab-title'>🧘‍♂️ مؤشر صحة المفاصل والمرونة</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار المرونة في صـ 68): أدخل نتيجتك في اختبار (صندوق المرونة - Sit and Reach).</div>", unsafe_allow_html=True)
    
    with st.form("lab6"):
        reach = st.number_input("المسافة المسجلة (سم):", min_value=-20, max_value=50, value=15)
        if st.form_submit_button("تقييم المرونة"):
            st.success("✅ التقرير:")
            if reach < 20:
                st.warning(f"المسافة ({reach} سم): المرونة ضعيفة. أنت بحاجة لبرنامج إطالات يومي لتجنب آلام أسفل الظهر.")
            elif 20 <= reach <= 35:
                st.info(f"المسافة ({reach} سم): المرونة متوسطة وجيدة.")
            else:
                st.success(f"المسافة ({reach} سم): المرونة ممتازة! نطاقك الحركي مثالي.")

elif selected_chapter == "الفصل السابع: اللياقة المهارية":
    st.markdown("<h2 class='lab-title'>🧠 حاسبة التوازن (اختبار اللقلق)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار التوازن في صـ 80): أدخل الزمن الذي استطعت الثبات فيه على قدم واحدة (وعيناك مغلقتان).</div>", unsafe_allow_html=True)
    
    with st.form("lab7"):
        time_sec = st.number_input("زمن الثبات (بالثواني):", min_value=0, max_value=120, value=10)
        if st.form_submit_button("تقييم التوافق العصبي"):
            st.success("✅ التقرير العصبي العضلي:")
            if time_sec < 10: st.warning("التوازن: ضعيف. ينصح بإدراج تدريبات الثبات والمركز (Core) يومياً.")
            elif 10 <= time_sec <= 25: st.info("التوازن: متوسط.")
            else: st.success("التوازن: ممتاز! كفاءة عالية في المستقبلات العصبية العضلية.")

elif selected_chapter == "الفصل الثامن: مبادئ التدريب":
    st.markdown("<h2 class='lab-title'>⚙️ مهندس البرامج التدريبية (معادلة F.I.T.T)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمبادئ التدريب في صـ 95): حدد المعطيات لتصميم هيكل برنامجك التدريبي.</div>", unsafe_allow_html=True)
    
    with st.form("lab8"):
        days = st.selectbox("الأيام المتاحة أسبوعياً:", ["3 أيام", "4 أيام", "5 أيام"])
        goal = st.selectbox("الهدف الأساسي:", ["تحسين الصحة العامة", "بناء العضلات", "حرق الدهون"])
        if st.form_submit_button("إنشاء التوصية التدريبية"):
            st.success("✅ وصفة (F.I.T.T) التدريبية:")
            st.write(f"**التكرار (Frequency):** التدريب {days} أسبوعياً.")
            if "العضلات" in goal:
                st.write("**الشدة (Intensity):** 70-80% من أقصى قوة، مع أوزان حرة وأجهزة.")
                st.write("**الزمن (Time):** 45 - 60 دقيقة.")
                st.write("**النوع (Type):** تدريبات مقاومة (أوزان).")
            elif "الدهون" in goal:
                st.write("**الشدة (Intensity):** 60-70% من أقصى معدل نبض.")
                st.write("**الزمن (Time):** 30 - 45 دقيقة.")
                st.write("**النوع (Type):** مزيج بين الكارديو (المشي السريع) والتدريب الدائري.")
            else:
                st.write("**الشدة (Intensity):** متوسطة إلى خفيفة.")
                st.write("**الزمن (Time):** 30 دقيقة يومياً.")
                st.write("**النوع (Type):** أنشطة هوائية متنوعة (سباحة، دراجة، مشي).")

elif selected_chapter == "الفصل التاسع: أنظمة تدريب القوة":
    st.markdown("<h2 class='lab-title'>📅 مستشار تقسيم الأيام التدريبية</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لأنظمة التدريب في صـ 110): كم يوماً ستذهب للصالة الرياضية؟</div>", unsafe_allow_html=True)
    
    with st.form("lab9"):
        days = st.radio("عدد أيام التدريب:", ["3 أيام", "4 أيام", "6 أيام"])
        if st.form_submit_button("أفضل نظام تدريبي"):
            st.success("✅ النظام المقترح علمياً:")
            if "3" in days: st.info("النظام الأفضل: **شامل للجسم (Full Body)**. قم بتدريب جميع العضلات 3 مرات أسبوعياً مع يوم راحة بين كل حصة.")
            elif "4" in days: st.info("النظام الأفضل: **علوي/سفلي (Upper / Lower)**. يومان للجزء العلوي ويومان للسفلي.")
            else: st.info("النظام الأفضل: **دفع/سحب/أرجل (Push / Pull / Legs)**. مناسب للمتقدمين لضمان حجم تدريبي مكثف.")

elif selected_chapter == "الفصل العاشر: التدريب الذكي":
    st.markdown("<h2 class='lab-title'>⏱️ صانع دوائر حرق الدهون (HIIT)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لبروتوكولات التاباتا في صـ 122): اختر مستواك لتوليد بروتوكول التدريب المتقطع.</div>", unsafe_allow_html=True)
    
    with st.form("lab10"):
        level = st.radio("مستواك البدني:", ["مبتدئ", "متوسط", "متقدم"])
        if st.form_submit_button("توليد البروتوكول"):
            st.success("✅ بروتوكول العمل والراحة:")
            if level == "مبتدئ": st.write("⏱️ **البروتوكول:** 30 ثانية عمل بطيء / 30 ثانية راحة تامة. (كرر 4 مرات).")
            elif level == "متوسط": st.write("⏱️ **البروتوكول:** 40 ثانية عمل سريع / 20 ثانية راحة نشطة. (كرر 6 مرات).")
            else: st.write("⏱️ **البروتوكول (تاباتا):** 20 ثانية عمل بأقصى سرعة / 10 ثواني راحة. (كرر 8 مرات متتالية).")

elif selected_chapter == "الفصل الحادي عشر: التغذية":
    st.markdown("<h2 class='lab-title'>🥩 حاسبة وقود الأبطال (الماكروز والتروية)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمفاهيم التغذية في صـ 135): أدخل وزنك لحساب احتياجك اليومي من البروتين والماء.</div>", unsafe_allow_html=True)
    
    with st.form("lab11"):
        weight = st.number_input("الوزن (كجم):", min_value=30.0, max_value=200.0, value=70.0)
        goal = st.radio("الهدف الأساسي:", ["الحفاظ على الصحة العامة", "بناء الكتلة العضلية"])
        if st.form_submit_button("حساب الاحتياجات"):
            water = round(weight * 0.033, 1)
            protein = round(weight * 1.6, 1) if "بناء" in goal else round(weight * 1.0, 1)
            st.success("✅ التقرير الغذائي:")
            st.write(f"💧 **الاحتياج المائي:** الوزن × 0.033 = **{water}** لتر يومياً (تزيد مع التعرق).")
            st.write(f"🥩 **الاحتياج البروتيني:** **{protein}** جرام يومياً مقسمة على وجباتك.")

elif selected_chapter == "الفصل الثاني عشر: خرافات اللياقة":
    st.markdown("<h2 class='lab-title'>💡 مختبر الوعي الرياضي (IQ Quiz)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً للمفاهيم الصحيحة في صـ 148): أجب عن صحة أو خطأ هذه المعتقدات الشائعة.</div>", unsafe_allow_html=True)
    
    with st.form("lab12"):
        q1 = st.radio("1. لبس الكيس البلاستيك أثناء الجري يزيد من حرق الدهون.", ["صح", "خطأ"], index=None)
        q2 = st.radio("2. تحويل الدهون إلى عضلات ممكن بالتدريب الشاق.", ["صح", "خطأ"], index=None)
        q3 = st.radio("3. تمارين البطن تحرق دهون الكرش موضعياً.", ["صح", "خطأ"], index=None)
        
        if st.form_submit_button("تصحيح المفاهيم"):
            if None in [q1, q2, q3]:
                st.error("⚠️ يرجى الإجابة على جميع الأسئلة.")
            else:
                st.success("✅ نتيجة الفحص:")
                if q1 == "خطأ": st.write("1. ✅ إجابة صحيحة. البلاستيك يفقدك السوائل (عرق) وليس الدهون، ويشكل خطراً فسيولوجياً.")
                else: st.error("1. ❌ خطأ علمي! البلاستيك يفقدك السوائل فقط ويؤدي للجفاف.")
                
                if q2 == "خطأ": st.write("2. ✅ إجابة صحيحة. الدهون نسيج والعضلات نسيج آخر، لا يتحول أحدهما للآخر.")
                else: st.error("2. ❌ خطأ علمي! النسيج الدهني لا يتحول لنسيج عضلي مطلقاً.")
                
                if q3 == "خطأ": st.write("3. ✅ إجابة صحيحة. لا يوجد حرق موضعي للدهون؛ الدهون تحرق من الجسم كاملاً كمنظومة.")
                else: st.error("3. ❌ خطأ علمي! علمياً لا يمكن استهداف منطقة معينة لحرق دهونها بالتمارين.")
