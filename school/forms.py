from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Student, Class


class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "phone_number",
            "email",
            "teacher_class",
            "item_name",
        )


class TeacherChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class StudentCreate(forms.ModelForm):
    student_class = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Класс",
    )

    class Meta:
        model = Student
        fields = "__all__"


class EmailMessageForm(forms.Form):
    recipients = forms.CharField(
        label="Recipients", help_text="Enter email addresses separated by commas"
    )
    subject = forms.CharField(label="Subject")
    message = forms.CharField(label="Message", widget=forms.Textarea)
