from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("student/create/", views.StudentCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
]
