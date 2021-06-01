from django.urls import path
from django.views.generic.base import View

from . import views
app_name = 'UserMembers'
urlpatterns = [
    path('register/', views.DangkyThanhvien.as_view(), name="dangky"),
    path('login/', views.DangnhapThanhvien.as_view(), name="dangnhap"),
    path('user-view', views.ViewUser.as_view(),name="user-view"),
]
