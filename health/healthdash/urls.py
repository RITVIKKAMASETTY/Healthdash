
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.register,name= 'reg'),
    path('healthdash_login', views.login_view,name='login'),
    path('user-in-form', views.inform,name='inform'),
    path('<str:username>-dashboard',views.dashboard,name='dashboard'),
    path('qr',views.qr,name='qr'),
]