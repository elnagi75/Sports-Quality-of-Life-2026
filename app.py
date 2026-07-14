import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. الإعدادات الأساسية للمنصة ---
st.set_page_config(page_title="الرياضة وجودة الحياة", page_icon="🏃‍♂️", layout="wide")

# --- 2. تنسيق CSS المُعالج والفاخر (تحديث الأزرار والنتائج) ---
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
        margin-bottom: 25px;
        line-height: 1.6;
    }
    
    /* العناوين والأسئلة (كحلي داكن وضخم) */
    .q-title {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #1a5276 !important;
        margin-bottom: 5px !important;
        margin-top: 15px !important;
    }
    
    /* الخيارات والدوائر (أخضر زمردي) */
    div[role="radiogroup"] label p, div[data-baseweb="select"] span, div[data-baseweb="checkbox"] label p {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #117A65 !important; 
    }
    
    /* 🔴 زر الإرسال - أحمر سميك ومثير للضغط 🔴 */
    .stButton button { 
        font-size: 26px !important; 
        font-weight: 900 !important; 
        border-radius: 12px !important; 
        padding: 15px !important; 
        width: 100%;
        background-color: #C0392B !important; /* أحمر رياضي داكن */
        color: white !important;
        border: 3px solid #922B21 !important;
        box-shadow: 0px 5px 8px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
        margin-top: 25px !important;
        margin-bottom: 15px !important;
    }
    .stButton button:hover {
        background-color: #E74C3C !important; /* أحمر ساطع عند التفاعل */
        border: 3px solid #C0392B !important;
        transform: scale(1.02) !important; /* تأثير التكبير عند لمس الماوس */
    }

    /* ✨ تكبير نصوص النتائج والتقارير لتتطابق مع العناوين ✨ */
    div[data-testid="stAlert"] div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stAlert"] div[data-testid="stMarkdownContainer"] span {
        font-size: 24px !important;
        font-weight: bold !important;
        line-height: 1.8 !important;
    }

    /* النصوص العادية التي تظهر كتقارير أسفل الزر */
    form div[data-testid="stMarkdownContainer"] p {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #1a5276 !important;
        line-height: 1.6;
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

components.html(
    f"""<iframe src="{chapters[selected_chapter]}" width="100%" height="600" frameborder="0" allowfullscreen sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation"></iframe>""",
    height=620
)

# ==============================================================================
# --- 7. قسم المختبرات التفاعلية (مع التحكم التام في العناوين والتفريغ) ---
# ==============================================================================

if selected_chapter == "الفصل الأول: هندسة الحركة البشرية":
    st.markdown("<h2 class='lab-title'>🛠️ مختبر القوام الرقمي: استمارة التحليل الذاتي</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً للمهام الواردة في صـ 11): قف أمام المرآة وسجل ملاحظاتك بصدق. (يُرجى تحديد خيار واحد من كل عنصر).</div>", unsafe_allow_html=True)
    
    with st.form("lab1"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p class='q-title'>الرأس والرقبة:</p>", unsafe_allow_html=True)
            head = st.radio("head1", ["متعامد مع الكتف (طبيعي)", "مائل للأمام (Forward Head)"], index=None, label_visibility="collapsed")
            
            st.markdown("<p class='q-title'>أعلى الظهر:</p>", unsafe_allow_html=True)
            upper_back = st.radio("back1", ["مسطح طبيعي", "محدب (Kyphosis)"], index=None, label_visibility="collapsed")
        with col2:
            st.markdown("<p class='q-title'>الكتفان:</p>", unsafe_allow_html=True)
            shoulders = st.radio("sh1", ["متساويان", "أحدهما أعلى من الآخر"], index=None, label_visibility="collapsed")
            
            st.markdown("<p class='q-title'>أسفل الظهر:</p>", unsafe_allow_html=True)
            lower_back = st.radio("lb1", ["انحناء طبيعي", "مقعر بشدة (Lordosis)", "مسطح (Flat Back)"], index=None, label_visibility="collapsed")
            
        st.markdown("<p class='q-title'>اختر العادات اليومية الخاطئة:</p>", unsafe_allow_html=True)
        habits = st.multiselect("habits1", ["استخدام الهاتف بكثرة بانحناء", "حمل الحقيبة على كتف واحد", "الجلوس الخاطئ", "قلة الحركة"], default=None, label_visibility="collapsed")
        
        if st.form_submit_button("استخراج الخطة التصحيحية"):
            if None in [head, upper_back, shoulders, lower_back]:
                st.error("⚠️ يرجى الإجابة على جميع عناصر الفحص البصري أولاً.")
            else:
                st.success("✅ تم التحليل الميكانيكي!")
                if "مائل للأمام" in head or "محدب" in upper_back:
                    st.warning("⚠️ **تشخيص:** مؤشرات لمتلازمة التقاطع العلوي. تحتاج لتقوية عضلات أعلى الظهر وإطالة عضلات الصدر والرقبة.")
                if "مقعر" in lower_back:
                    st.warning("⚠️ **تشخيص:** زيادة التقعر القطني. تحتاج لتقوية عضلات البطن (Core) وإطالة عضلات الفخذ الأمامية.")
                if "طبيعي" in head and "طبيعي" in upper_back and "طبيعي" in lower_back:
                    st.info("🌟 قوامك متزن! استمر في نشاطك.")

elif selected_chapter == "الفصل الثاني: فسيولوجيا الجهد":
    st.markdown("<h2 class='lab-title'>🫀 مختبر فسيولوجيا الجهد: حاسبة النبض المستهدف</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمعادلة كارفونين في صـ 24): أدخل بياناتك لحساب النطاق الأمثل لنبض قلبك أثناء التدريب.</div>", unsafe_allow_html=True)
    
    with st.form("lab2"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p class='q-title'>العمر (بالسنوات):</p>", unsafe_allow_html=True)
            age = st.number_input("age2", min_value=10, max_value=100, value=None, step=1, label_visibility="collapsed")
        with col2:
            st.markdown("<p class='q-title'>النبض وقت الراحة (نبضة/دقيقة):</p>", unsafe_allow_html=True)
            resting_hr = st.number_input("rhr2", min_value=40, max_value=120, value=None, step=1, label_visibility="collapsed")
            
        st.markdown("<p class='q-title'>الهدف من التدريب (Target Zone):</p>", unsafe_allow_html=True)
        goal = st.selectbox("goal2", ["الاستشفاء وحرق الدهون (50% - 60%)", "اللياقة القلبية والتخسيس (60% - 70%)", "تطوير الأداء الرياضي (70% - 80%)", "الحد الأقصى اللاهوائي (80% - 90%)"], index=None, label_visibility="collapsed")
        
        if st.form_submit_button("حساب مناطق التدريب"):
            if age is None or resting_hr is None or goal is None:
                st.error("⚠️ يرجى إدخال جميع البيانات المطلوبة.")
            else:
                max_hr = 220 - age
                hr_reserve = max_hr - resting_hr
                min_int, max_int = (0.5, 0.6) if "50%" in goal else (0.6, 0.7) if "60%" in goal else (0.7, 0.8) if "70%" in goal else (0.8, 0.9)
                t_min, t_max = int((hr_reserve * min_int) + resting_hr), int((hr_reserve * max_int) + resting_hr)
                
                st.success("✅ التقرير الفسيولوجي:")
                st.write(f"📊 أقصى معدل لضربات القلب = 220 - العمر = **{max_hr}** نبضة/دقيقة.")
                st.info(f"🎯 **النبض المستهدف لتحقيق هدفك:** من **{t_min}** إلى **{t_max}** نبضة/دقيقة.")

elif selected_chapter == "الفصل الثالث: القياسات الجسمية":
    st.markdown("<h2 class='lab-title'>⚖️ مختبر تحليل تركيب الجسم ونمطه</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمهام التقييم في صـ 36): أدخل قياساتك لتقييم صحة تركيبك الجسماني.</div>", unsafe_allow_html=True)
    
    with st.form("lab3"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p class='q-title'>الوزن (كجم):</p>", unsafe_allow_html=True)
            weight = st.number_input("w3", min_value=30.0, max_value=200.0, value=None, label_visibility="collapsed")
            
            st.markdown("<p class='q-title'>الطول (سم):</p>", unsafe_allow_html=True)
            height_cm = st.number_input("h3", min_value=100.0, max_value=220.0, value=None, label_visibility="collapsed")
        with col2:
            st.markdown("<p class='q-title'>محيط الخصر (سم):</p>", unsafe_allow_html=True)
            waist = st.number_input("wa3", min_value=40.0, max_value=150.0, value=None, label_visibility="collapsed")
            
            st.markdown("<p class='q-title'>محيط الحوض (سم):</p>", unsafe_allow_html=True)
            hip = st.number_input("hi3", min_value=40.0, max_value=150.0, value=None, label_visibility="collapsed")
            
        if st.form_submit_button("تحليل البيانات"):
            if None in [weight, height_cm, waist, hip]:
                st.error("⚠️ يرجى إدخال جميع القياسات.")
            else:
                height_m = height_cm / 100
                bmi = round(weight / (height_m * height_m), 1)
                whr = round(waist / hip, 2)
                
                st.success("✅ تقرير تركيب الجسم:")
                st.write(f"📊 مؤشر كتلة الجسم = **{bmi}**")
                st.write(f"📊 نسبة الخصر للحوض = **{whr}**")
                if bmi < 18.5: st.warning("النتيجة: نحافة.")
                elif 18.5 <= bmi <= 24.9: st.info("النتيجة: وزن مثالي وصحي.")
                else: st.warning("النتيجة: وزن زائد (يجب ضبط النظام الغذائي).")

elif selected_chapter == "الفصل الرابع: اللياقة القلبية":
    st.markdown("<h2 class='lab-title'>🫁 محلل كفاءة المحرك القلبي (اختبار كوبر)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار كوبر في صـ 46): أدخل المسافة المقطوعة (بالمتر) خلال 12 دقيقة.</div>", unsafe_allow_html=True)
    
    with st.form("lab4"):
        st.markdown("<p class='q-title'>المسافة المقطوعة (بالمتر):</p>", unsafe_allow_html=True)
        distance = st.number_input("d4", min_value=500, max_value=4000, value=None, step=50, label_visibility="collapsed")
        
        if st.form_submit_button("حساب السعة الهوائية (VO2max)"):
            if distance is None:
                st.error("⚠️ يرجى إدخال المسافة أولاً.")
            else:
                vo2max = round((distance - 504.9) / 44.73, 1)
                st.success("✅ التقرير القلبي التنفسي:")
                st.write(f"📊 الحد الأقصى لاستهلاك الأكسجين (VO2max) = **{vo2max}** مل/كجم/دقيقة.")
                if vo2max < 30: st.warning("التصنيف: ضعيف (تحتاج للبدء ببرنامج مشي منتظم).")
                elif 30 <= vo2max < 40: st.info("التصنيف: متوسط.")
                else: st.success("التصنيف: ممتاز (كفاءة قلبية عالية).")

elif selected_chapter == "الفصل الخامس: القوة والتحمل":
    st.markdown("<h2 class='lab-title'>🦾 مقياس التحمل وتوقع القوة القصوى (1RM)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمعادلة القوة في صـ 59): أدخل الوزن الذي تدربت به وعدد التكرارات لحساب أقصى وزن يمكن رفعه لمرة واحدة.</div>", unsafe_allow_html=True)
    
    with st.form("lab5"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p class='q-title'>الوزن المستخدم (كجم):</p>", unsafe_allow_html=True)
            weight = st.number_input("w5", min_value=1, max_value=300, value=None, step=1, label_visibility="collapsed")
        with col2:
            st.markdown("<p class='q-title'>عدد التكرارات المنجزة:</p>", unsafe_allow_html=True)
            reps = st.number_input("r5", min_value=1, max_value=20, value=None, step=1, label_visibility="collapsed")
            
        if st.form_submit_button("حساب القوة القصوى"):
            if weight is None or reps is None:
                st.error("⚠️ يرجى إدخال الوزن وعدد التكرارات.")
            else:
                one_rm = round(weight + (weight * reps / 30), 1)
                st.success("✅ تقرير القوة العضلية:")
                st.write(f"📊 القوة القصوى (1RM) = **{one_rm}** كجم.")
                st.info("💡 لتدريب الضخامة: استخدم أوزاناً تتراوح بين 70% إلى 80% من هذا الرقم.")

elif selected_chapter == "الفصل السادس: المرونة":
    st.markdown("<h2 class='lab-title'>🧘‍♂️ مؤشر صحة المفاصل والمرونة</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار المرونة في صـ 73): أدخل نتيجتك في اختبار (صندوق المرونة - Sit and Reach).</div>", unsafe_allow_html=True)
    
    with st.form("lab6"):
        st.markdown("<p class='q-title'>المسافة المسجلة (سم):</p>", unsafe_allow_html=True)
        reach = st.number_input("r6", min_value=-20, max_value=50, value=None, step=1, label_visibility="collapsed")
        
        if st.form_submit_button("تقييم المرونة"):
            if reach is None:
                st.error("⚠️ يرجى إدخال المسافة المسجلة.")
            else:
                st.success("✅ التقرير:")
                if reach < 20: st.warning(f"المسافة ({reach} سم): المرونة ضعيفة. أنت بحاجة لبرنامج إطالات يومي.")
                elif 20 <= reach <= 35: st.info(f"المسافة ({reach} سم): المرونة متوسطة وجيدة.")
                else: st.success(f"المسافة ({reach} سم): المرونة ممتازة! نطاقك الحركي مثالي.")

elif selected_chapter == "الفصل السابع: اللياقة المهارية":
    st.markdown("<h2 class='lab-title'>🧠 حاسبة التوازن (اختبار اللقلق)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لاختبار التوازن في صـ 87): أدخل الزمن الذي استطعت الثبات فيه على قدم واحدة.</div>", unsafe_allow_html=True)
    
    with st.form("lab7"):
        st.markdown("<p class='q-title'>زمن الثبات (بالثواني):</p>", unsafe_allow_html=True)
        time_sec = st.number_input("t7", min_value=0, max_value=120, value=None, step=1, label_visibility="collapsed")
        
        if st.form_submit_button("تقييم التوافق العصبي"):
            if time_sec is None:
                st.error("⚠️ يرجى إدخال الزمن.")
            else:
                st.success("✅ التقرير العصبي العضلي:")
                if time_sec < 10: st.warning("التوازن: ضعيف. ينصح بإدراج تدريبات الثبات والمركز (Core) يومياً.")
                elif 10 <= time_sec <= 25: st.info("التوازن: متوسط.")
                else: st.success("التوازن: ممتاز! كفاءة عالية في المستقبلات العصبية العضلية.")

elif selected_chapter == "الفصل الثامن: مبادئ التدريب":
    st.markdown("<h2 class='lab-title'>⚙️ مهندس البرامج التدريبية (معادلة F.I.T.T)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمبادئ التدريب في صـ 101): حدد المعطيات لتصميم هيكل برنامجك التدريبي.</div>", unsafe_allow_html=True)
    
    with st.form("lab8"):
        st.markdown("<p class='q-title'>الأيام المتاحة أسبوعياً:</p>", unsafe_allow_html=True)
        days = st.selectbox("d8", ["3 أيام", "4 أيام", "5 أيام"], index=None, label_visibility="collapsed")
        
        st.markdown("<p class='q-title'>الهدف الأساسي:</p>", unsafe_allow_html=True)
        goal = st.selectbox("g8", ["تحسين الصحة العامة", "بناء العضلات", "حرق الدهون"], index=None, label_visibility="collapsed")
        
        if st.form_submit_button("إنشاء التوصية التدريبية"):
            if days is None or goal is None:
                st.error("⚠️ يرجى تحديد الأيام والهدف.")
            else:
                st.success("✅ وصفة (F.I.T.T) التدريبية:")
                st.write(f"**التكرار (Frequency):** التدريب {days} أسبوعياً.")
                if "العضلات" in goal:
                    st.write("**الشدة (Intensity):** 70-80% من أقصى قوة، مع أوزان حرة.")
                    st.write("**الزمن (Time):** 45 - 60 دقيقة.")
                    st.write("**النوع (Type):** تدريبات مقاومة (أوزان).")
                elif "الدهون" in goal:
                    st.write("**الشدة (Intensity):** 60-70% من أقصى معدل نبض.")
                    st.write("**الزمن (Time):** 30 - 45 دقيقة.")
                    st.write("**النوع (Type):** مزيج بين الكارديو والتدريب الدائري.")
                else:
                    st.write("**الشدة (Intensity):** متوسطة إلى خفيفة.")
                    st.write("**الزمن (Time):** 30 دقيقة يومياً.")
                    st.write("**النوع (Type):** أنشطة هوائية متنوعة.")

elif selected_chapter == "الفصل التاسع: أنظمة تدريب القوة":
    st.markdown("<h2 class='lab-title'>📅 مستشار تقسيم الأيام التدريبية</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لأنظمة التدريب في صـ 115): كم يوماً ستذهب للصالة الرياضية؟</div>", unsafe_allow_html=True)
    
    with st.form("lab9"):
        st.markdown("<p class='q-title'>عدد أيام التدريب المتاحة:</p>", unsafe_allow_html=True)
        days = st.radio("d9", ["3 أيام", "4 أيام", "6 أيام"], index=None, label_visibility="collapsed")
        
        if st.form_submit_button("أفضل نظام تدريبي"):
            if days is None:
                st.error("⚠️ يرجى اختيار عدد الأيام.")
            else:
                st.success("✅ النظام المقترح علمياً:")
                if "3" in days: st.info("النظام الأفضل: **شامل للجسم (Full Body)**. قم بتدريب جميع العضلات 3 مرات أسبوعياً.")
                elif "4" in days: st.info("النظام الأفضل: **علوي/سفلي (Upper / Lower)**. يومان للجزء العلوي ويومان للسفلي.")
                else: st.info("النظام الأفضل: **دفع/سحب/أرجل (Push / Pull / Legs)**. مناسب للمتقدمين لضمان حجم تدريبي مكثف.")

elif selected_chapter == "الفصل العاشر: التدريب الذكي":
    st.markdown("<h2 class='lab-title'>⏱️ صانع دوائر حرق الدهون (HIIT)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لبروتوكولات التاباتا في صـ 130): اختر مستواك لتوليد بروتوكول التدريب المتقطع.</div>", unsafe_allow_html=True)
    
    with st.form("lab10"):
        st.markdown("<p class='q-title'>حدد مستواك البدني الحالي:</p>", unsafe_allow_html=True)
        level = st.radio("l10", ["مبتدئ", "متوسط", "متقدم"], index=None, label_visibility="collapsed")
        
        if st.form_submit_button("توليد البروتوكول"):
            if level is None:
                st.error("⚠️ يرجى تحديد المستوى أولاً.")
            else:
                st.success("✅ بروتوكول العمل والراحة:")
                if level == "مبتدئ": st.write("⏱️ **البروتوكول:** 30 ثانية عمل بطيء / 30 ثانية راحة تامة. (كرر 4 مرات).")
                elif level == "متوسط": st.write("⏱️ **البروتوكول:** 40 ثانية عمل سريع / 20 ثانية راحة نشطة. (كرر 6 مرات).")
                else: st.write("⏱️ **البروتوكول (تاباتا):** 20 ثانية عمل بأقصى سرعة / 10 ثواني راحة. (كرر 8 مرات متتالية).")

elif selected_chapter == "الفصل الحادي عشر: التغذية":
    st.markdown("<h2 class='lab-title'>🥩 حاسبة وقود الأبطال (الماكروز والتروية)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً لمفاهيم التغذية في صـ 142): أدخل وزنك لحساب احتياجك اليومي من البروتين والماء.</div>", unsafe_allow_html=True)
    
    with st.form("lab11"):
        st.markdown("<p class='q-title'>الوزن (كجم):</p>", unsafe_allow_html=True)
        weight = st.number_input("w11", min_value=30.0, max_value=200.0, value=None, label_visibility="collapsed")
        
        st.markdown("<p class='q-title'>الهدف الأساسي:</p>", unsafe_allow_html=True)
        goal = st.radio("g11", ["الحفاظ على الصحة العامة", "بناء الكتلة العضلية"], index=None, label_visibility="collapsed")
        
        if st.form_submit_button("حساب الاحتياجات"):
            if weight is None or goal is None:
                st.error("⚠️ يرجى إدخال الوزن وتحديد الهدف.")
            else:
                water = round(weight * 0.033, 1)
                protein = round(weight * 1.6, 1) if "بناء" in goal else round(weight * 1.0, 1)
                st.success("✅ التقرير الغذائي:")
                st.write(f"💧 **الاحتياج المائي:** **{water}** لتر يومياً (تزيد مع التعرق).")
                st.write(f"🥩 **الاحتياج البروتيني:** **{protein}** جرام يومياً مقسمة على وجباتك.")

elif selected_chapter == "الفصل الثاني عشر: خرافات اللياقة":
    st.markdown("<h2 class='lab-title'>💡 مختبر الوعي الرياضي (IQ Quiz)</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>📌 تعليمات (تطبيقاً للمفاهيم الصحيحة في صـ 155): أجب عن صحة أو خطأ هذه المعتقدات الشائعة.</div>", unsafe_allow_html=True)
    
    with st.form("lab12"):
        st.markdown("<p class='q-title'>1. لبس الكيس البلاستيك أثناء الجري يزيد من حرق الدهون.</p>", unsafe_allow_html=True)
        q1 = st.radio("q1_12", ["صح", "خطأ"], index=None, label_visibility="collapsed")
        
        st.markdown("<p class='q-title'>2. تحويل الدهون إلى عضلات ممكن بالتدريب الشاق.</p>", unsafe_allow_html=True)
        q2 = st.radio("q2_12", ["صح", "خطأ"], index=None, label_visibility="collapsed")
        
        st.markdown("<p class='q-title'>3. تمارين البطن تحرق دهون الكرش موضعياً.</p>", unsafe_allow_html=True)
        q3 = st.radio("q3_12", ["صح", "خطأ"], index=None, label_visibility="collapsed")
        
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
