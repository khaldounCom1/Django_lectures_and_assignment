# student/forms.py
from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    gpa = forms.FloatField()

# student/forms.py
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'gpa']
