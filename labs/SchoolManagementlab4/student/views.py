from django.shortcuts import render
from .models import Student

# Create your views here.
# def index(request):
#     return render(request,'index.html')
def home(request):
    return render(request,'home.html')

def list_students(request):
    students={
        "name":"Malek",
        "marks":[90,95,98,97],
        "eachsub":{"Software Engineering":96,
                   "Image Prossing":94,
                   "Client and Server Programming":96}
    }
    return render(request,'showstudents.html',students)

def edit_students(request):
    students={"total":286,
              "marks":{"Software Engineering":96,
                       "Image Processing":94,
                       "Client and Server Programming":96}}
    return render(request,'editstudents.html',students)

def delete_students(request):
    return render(request,'deletestudents.html')

def index(request):
    name={"fname":"Malek"}
    return render(request,'index.html',name)
def main_page(request):
    return render(request, 'main.html')



def read(request):
    status = request.GET.get('q')
    if status == 'all' or status is None:
     Students = Student.objects.all()
    elif status:
      Students=Student.objects.filter(status=status)
    Students_count = Students.count()
    return render(request, 'allStudents.html', {
        "Students": Students,
        "Students_count": Students_count
    })


def read_one(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student_one.html', {
        "student": student
    })

def create(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        gpa = request.POST.get('gpa')
        level = request.POST.get('level')
        status = request.POST.get('status')
        report = request.POST.get('report')
        image=request.FILES.get('image')
        file_report=request.FILES.get('repo')

        new_student = Student(
            f_name=f_name,
            l_name=l_name,
            age=age,
            gpa=gpa,
            level=level,
            status=status,
            report=report,
            file_report=file_report,
            image = image
        )
        new_student.save()
        return render(request, 'messages/created.html')
    else:
        return render(request, 'insert_student.html')


def update(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)

        student.f_name = request.POST.get('f_name')
        student.l_name = request.POST.get('l_name')
        student.age = request.POST.get('age')
        student.gpa = request.POST.get('gpa')
        student.level = request.POST.get('level')
        student.status = request.POST.get('status')
        student.report = request.POST.get('report')

        student.save()

        return render(request, 'messages/updated.html')
    else:
        student = Student.objects.get(id=id)
        return render(request, 'update_student.html', {"student": student})


def delete(request, id):
    Student.objects.get(id=id).delete()
    return render(request, 'messages/deleted.html')



def getstudents(request):
    students = Student.objects.all().order_by('gpa')
    return render(request, 'showstudents.html', {"students": students})


def getstudents(request):
    students = Student.objects.all().order_by('-gpa')
    return render(request, 'showstudents.html', {"students": students})

def getstudents(request):
    students = Student.objects.filter(gpa__in=[91.20, 90.2])
    return render(request, 'showstudents.html', {"students": students})


def getstudents(request):
    students = Student.objects.filter(gpa__range=[89, 91])
    return render(request, 'showstudents.html', {"students": students})


def getstudents(request):
    students = Student.objects.filter(gpa__exact=91.2)
    return render(request, 'showstudents.html', {"students": students})


def getstudents(request):
    students = Student.objects.all().exclude(f_name="Malek")
    return render(request, 'showstudents.html', {"students": students})

from django.db.models import Q

def getstudents(request):
    students = Student.objects.all().exclude(Q(f_name="Malek") | Q(age=23))
    return render(request, 'showstudents.html', {"students": students})
