# from django.urls import path
# from . import views

# # urlpatterns = [
# #     path('',views.index,name="index"),
# #     path('home/',views.home,name='home'),
# #     path('show/',views.list_students,name='show'),
# #     path('edit/',views.edit_students,name='edit'),
# #     path('delete/',views.edit_students,name='delete'),
# # ]


from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path("", views.home, name='home'),
    path("allStudents/", views.read, name='allStudents'),
    path("one/<int:id>/", views.read_one, name='student_one'),
    path("create/", views.create, name='newStudent'),
    path("update/<int:id>/", views.update, name='edit'),
    path("delete/<int:id>/", views.delete, name='delete'),
    path("all/", views.read, name='students'), 
    path("main_page/",views.main_page,name='main_page')

    # path("insert_student/",views.create)
]













