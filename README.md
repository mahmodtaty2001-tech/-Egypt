# ATegypT - Streamlit 3D Museum

هذا الفرع يضيف ملفات دعم لتشغيل تطبيق Streamlit الموجود (app.py) ويُسهّل عرض نماذج 3D وبيئات VR عبر تضمينات (Sketchfab) وA-Frame.

ما تمّ إضافته في هذا الفرع:
- requirements.txt: المتطلبات الأساسية لتشغيل التطبيق محليًا.
- README.md: تعليمات التثبيت والتشغيل السريعة.
- sketchfab_helper.py: مساعد بسيط لبحث وقوائم نتائج Sketchfab (يتطلب API token لاستخدام ميزات البحث/التحميل).
- fetch_models.py: أداة مساعدة سطر أوامر لاختبار البحث على Sketchfab.
- assets/aframe_demo.html: صفحة HTML بسيطة تستخدم A-Frame لعرض نموذج GLTF/GLB عبر رابط.

تشغيل محلي سريع:
1. python -m venv venv
2. source venv/bin/activate  (أو venv\\Scripts\\activate على ويندوز)
3. pip install -r requirements.txt
4. streamlit run app.py

ملاحظات مهمة:
- لميزات البحث والتحميل من Sketchfab، ستحتاج إلى توكن API. لا تقم بحفظ التوكن في الريبو بشكل علني — استخدم متغيرات البيئة أو GitHub Secrets عند إعداد CI.
- إذا رغبت بتنزيل نماذج كبيرة داخل المستودع، سنحتاج Git LFS.

للمساعدة أو لتعديل السلوك (تحميل ملفات محليًا، تكامل Streamlit Cloud، أو تحسين واجهة VR) أبلغني وسأُجري التعديلات.
