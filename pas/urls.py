# Developer : Lucas Liu
# Date: 2022/1/10 Time: 22:57
from django.urls import path

from pas import views

urlpatterns = [
    path('', views.toLogin_view, name='toLogin'),
    path('index/', views.toIndex_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('toRegister/', views.toRegister_view, name='toRegister'),
    path('register/', views.register_view, name='register'),
    path('showInfo', views.stuInfo_view, name='studentInfo'),
    path('score', views.score_view, name='score'),
    path('stuInfo/add', views.addInfo_view, name='addInfo'),
]