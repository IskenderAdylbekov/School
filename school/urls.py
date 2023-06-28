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
    path(
        "student/<int:pk>/delete/",
        views.StudentDeleteView.as_view(),
        name="student_delete",
    ),
    path("class/create", views.ClassCreateView.as_view(), name="class_create"),
    path("send-email/", views.send_email, name="send_email"),
    path(
        "class/<int:pk>/delete/", views.ClassDeleteView.as_view(), name="class_delete"
    ),
    path("class/", views.ClassListView.as_view(), name="class_list"),
]
