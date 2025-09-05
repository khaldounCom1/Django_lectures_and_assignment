# courses/models.py

from django.db import models
from teachers.models import Teacher # استيراد نموذج المدرس

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField(default=3)
    
    # **علاقة One-to-Many: المدرس الواحد يمكن أن يدرس عدة مقررات**
    # إذا حذف المدرس، يتم تعيين حقل 'teacher' في المقررات إلى NULL
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    def __str__(self):
        return self.name