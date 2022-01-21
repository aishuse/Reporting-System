from django.db import models

from admins.models import Course, Batch
from authapp.models import MyUser
from django.utils import timezone

class Student(models.Model):

    ADMITTED = 'admitted'
    NOT_INTERESTED = 'not_interested'
    FOLLOWUP = 'followup'
    options = (
        ('ADMITTED', 'admitted'),
        ('NOT_INTERESTED', 'not_interested'),
        ('FOLLOWUP', 'followup')
    )
    student_name = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=options, default='FOLLOWUP')
    followup_date = models.DateField(null=True)
    enquiry_date = models.DateTimeField(default=timezone.now)
    telecaller = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


