# from django.contrib import admin
# # from .models import Student
# # Register your models here.
# # admin.site.register(Student)

# # students/admin.py

# from .models import Student, StudentProfile

# admin.site.register(Student)
# admin.site.register(StudentProfile)

# students/admin.py

from django.contrib import admin
from .models import Student, StudentDetail # أضفنا StudentDetail

admin.site.register(Student)
admin.site.register(StudentDetail) # تسجيل النموذج الجديد

# تغيير عنوان الهيدر في صفحة الإدارة
admin.site.site_header = "لوحة تحكم إدارة المدرسة"

# تغيير العنوان في صفحة تسجيل الدخول
admin.site.site_title = "نظام إدارة المدرسة"

# تغيير النص الذي يظهر في الصفحة الرئيسية للإدارة
admin.site.index_title = "مرحبًا بك في لوحة تحكم النظام"