"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name= 'University'
urlpatterns = [
    #Include default auth urls
    path('', views.homepage,name="homepage"),
    path('login', views.login,name="login"),
    path('signup', views.signUp,name="signup"),
    path('menu',views.menu,name="menu"),
    path('course_add',views.course_add,name='course_add'),
    path('course_drop',views.course_drop,name='course_drop'),
    path('course_registration',views.course_registration,name='course_registration'),
    path('personal_information',views.personal_information,name='personal_information'),
    path('results',views.results,name='results'),
    path('student_registration',views.student_registration,name='student_registration'),
    
]