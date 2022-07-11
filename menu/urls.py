from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
    path("", views.home, name="home"),
    path("menu_am", views.menu_am, name="menu-am"),
    path("menu_pm", views.menu_pm, name="menu-pm")
]
