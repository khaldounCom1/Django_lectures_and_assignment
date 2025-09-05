# from django.db import models

# class Student(models.Model):
#     Levels = [
#         ('1', 'Level 1'),
#         ('2', 'Level 2'),
#         ('3', 'Level 3'),
#         ('4', 'Level 4'),
#     ]
    
#     f_name  = models.CharField(max_length=10, default="Student")
#     l_name  = models.CharField(max_length=10, default="Student")
#     age     = models.IntegerField(default=18)  # عمر افتراضي
#     level   = models.CharField(choices=Levels, max_length=20, default='1')
#     gpa     = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
#     status  = models.BooleanField(default=True)  # افتراضي أنه نشط
#     report  = models.TextField(max_length=300, default="", blank=True)
#     image = models.ImageField(upload_to='images/%y/%m/%d',null=True)
#     file_report = models.FileField(upload_to='files/%y/%m/%d',null=True)

#     def __str__(self):
#         return f"{self.f_name} {self.l_name}"
    
#     def delete(self):
#         self.image.delete()
#         self.file_report.delete()
#         return super().delete()
# students/models.py

from django.db import models

class Student(models.Model):
    Levels = [
        ('1', 'Level 1'),
        ('2', 'Level 2'),
        ('3', 'Level 3'),
        ('4', 'Level 4'),
    ]
    
    f_name  = models.CharField(max_length=10, default="Student")
    l_name  = models.CharField(max_length=10, default="Student")
    age     = models.IntegerField(default=18)
    level   = models.CharField(choices=Levels, max_length=20, default='1')
    gpa     = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    status  = models.BooleanField(default=True)
    report  = models.TextField(max_length=300, default="", blank=True)
    image = models.ImageField(upload_to='images/%y/%m/%d',null=True, blank=True) # أضفت blank=True
    file_report = models.FileField(upload_to='files/%y/%m/%d',null=True, blank=True) # أضفت blank=True

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    def delete(self):
        # تأكد من أن الحقل ليس فارغًا قبل محاولة حذفه
        if self.image:
            self.image.delete()
        if self.file_report:
            self.file_report.delete()
        return super().delete()

# **علاقة One-to-One: الطالب لديه تفاصيل إضافية واحدة**
class StudentDetail(models.Model):
    # ربط StudentDetail بـ Student بعلاقة One-to-One
    # primary_key=True يجعل هذا الحقل المفتاح الأساسي للنموذج
    # ويضمن أن يكون لكل طالب تفصيل واحد فقط
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    
    # حقول إضافية لتفاصيل الطالب
    national_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Details for {self.student.f_name} {self.student.l_name}"