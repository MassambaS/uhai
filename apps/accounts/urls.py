from django.urls import path
from . import views
from knox import views as knox_views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("", views.UserViewSet)

urlpatterns =  [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', knox_views.LoginView.as_view(), name="logout"),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name="logout-all")

] + router.urls 