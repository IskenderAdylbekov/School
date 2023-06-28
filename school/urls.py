from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("student/create/", views.StudentCreateView.as_view(), name="student_create"),
    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path(
        "student/<int:pk>/edit/", views.StudentEditView.as_view(), name="student_edit"
    ),
    path("class/", views.ClassCreateView.as_view(), name="class"),
    path("send-email/", views.send_email, name="send_email"),
]
