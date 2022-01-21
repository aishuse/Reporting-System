from django import forms
from .models import Batch, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'fees']
        widgets = {
            "course_name": forms.TextInput(attrs={"class": "form-control"}),
            "fees": forms.NumberInput(attrs={"class": "form-control"}),
            'active_status': forms.Select(attrs={"class": "form-select"})
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'course', 'total_seat', 'available_seat']
        widgets = {
            "batch_name": forms.TextInput(attrs={"class": "form-control"}),
            'active_status': forms.Select(attrs={"class": "form-select"}),
            'course': forms.Select(attrs={"class": "form-select"}),
            'total_seat': forms.NumberInput(attrs={"class": "form-control"}),
            'available_seat': forms.NumberInput(attrs={"class": "form-control"})

        }