# enrollments/models.py

from django.db import models
from student.models import Student # استيراد نموذج الطالب
from courses.models import Course   # استيراد نموذج المقرر

# **علاقة Many-to-Many: الطالب الواحد يسجل في عدة مقررات، والمقرر الواحد يضم عدة طلاب**
# نستخدم نموذج وسيط لتخزين معلومات إضافية عن العلاقة (مثل الدرجة)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    
    GRADES = [
        ('A', 'Excellent'),
        ('B', 'Good'),
        ('C', 'Average'),
        ('D', 'Pass'),
        ('F', 'Fail'),
        ('P', 'Pass (No Grade)'),
    ]
    grade = models.CharField(max_length=1, choices=GRADES, blank=True, null=True)

    class Meta:
        # لضمان عدم تكرار تسجيل الطالب في نفس المقرر مرتين
        unique_together = ('student', 'course') 

    def __str__(self):
        return f"{self.student.f_name} {self.student.l_name} - {self.course.name}"