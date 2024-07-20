from django.urls import path
from . import views
from django.contrib.auth.models import User
from requests import request

urlpatterns = [
    path('', views.main_page, name = 'main'),
    path('myplans', views.myplans, name = 'myplans'),
    path('dayplan', views.dayplan, name = 'dayplan'),
    path('edit/<int:us>/<int:pk>', views.PlanUpdate.as_view(), name = 'edit_plan'),
    path('delete/<int:pk>', views.delete_plan, name = 'delete_plan'),
    path('account', views.account, name = 'account'),
    path('signup', views.register, name='signup'),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.LogInView.as_view(), name='login'),
    path('del_user', views.delete_user, name = 'del_user'),
    path('change_theme', views.change_theme, name = 'change_theme')
]