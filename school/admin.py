from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import Student, Class, School
from .forms import TeacherCreationForm, TeacherChangeForm

Teacher = get_user_model()


class TeacherAdmin(UserAdmin):
    model = Teacher
    add_form = TeacherCreationForm
    form = TeacherChangeForm
    list_display = ["username", "email", "phone_number", "is_superuser"]
    list_display_links = ["username", "email"]
    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "item_name",
                    "teacher_class",
                )
            },
        ),
        ("Permissions", {"fields": ("is_superuser", "is_active")}),
    )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(School)
