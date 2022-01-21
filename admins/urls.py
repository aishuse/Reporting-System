from django.urls import path
from . import views

urlpatterns = [

    path('home', views.Home.as_view(), name='home'),
    path('base', views.Base.as_view(), name='base'),

    path('courses', views.AddCourse.as_view(), name='courses'),
    path('course/list', views.ListCourse.as_view(), name='listcourse'),
    path('batches', views.AddBatch.as_view(), name='batches'),
    path('batch/list', views.ListBatches.as_view(), name='listbatch'),
    path('addtelecaller', views.AddTelecaller.as_view(), name='telecalleradd'),
    path('telecaller/list', views.ListTelecallers.as_view(), name='listtelecallers')

]