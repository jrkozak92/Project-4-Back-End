from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/user', views.UserList.as_view(), name="user_list"),
    path('api/user/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('api/user/login', csrf_exempt(views.check_login), name="check_login")
]
