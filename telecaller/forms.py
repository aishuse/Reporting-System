from django import forms

from admins.models import Course, Batch
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'phone', 'email', 'course', 'batch', 'status', 'followup_date', 'enquiry_date']

        widgets = {
            'student_name': forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            'course' : forms.Select(attrs={'class':'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            "followup_date": forms.DateInput(attrs={"type": "date"}),
            "enquiry_date": forms.DateInput(attrs={"type": "date"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['batch'].queryset = Course.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['batch'].queryset = Batch.objects.filter(course_id=course_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['batch'].queryset = self.instance.course.batch_set.order_by('batch_name')