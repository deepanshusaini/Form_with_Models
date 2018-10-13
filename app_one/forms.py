from django import forms
from app_one.models import Student

class Myform(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"