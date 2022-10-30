from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("edit/<int:id>/", views.edit_todo, name="edit-todo"),
    path("delete/<int:id>/", views.deleteTodo, name="delete-todo"),
    path("signup/", views.register, name="signup"),
    path(
        "signin/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="signin-user",
    ),
    path("signout/", auth_views.LogoutView.as_view(), name="logout"),
]
