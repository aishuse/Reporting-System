from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=120, unique=True)
    fees = models.PositiveIntegerField(max_length=120)
    active_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course_name

class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coursebatch')
    batch_name = models.CharField(max_length=120)
    active_status = models.BooleanField(default=True)
    total_seat = models.IntegerField(default=30)
    available_seat = models.IntegerField()


    def __str__(self):
        return self.batch_name

    
