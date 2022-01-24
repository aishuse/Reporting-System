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
    path('telecaller/list', views.ListTelecallers.as_view(), name='listtelecallers'),
    path('course/delete/<int:pk>', views.CourseDelete.as_view(), name='coursedelete'),
    path('course/update/<int:pk>', views.CourseUpdate.as_view(), name='courseupdate'),
    path('telecaller/delete/<int:pk>', views.TelecallerDelete.as_view(), name='telecallerdelete'),
    path('telecaller/update/<int:pk>', views.TelecallerUpdate.as_view(), name='telecallerupdate'),
    path('batch/delete/<int:pk>', views.BatchDelete.as_view(), name='batchdelete'),
    path('batch/update/<int:pk>', views.BatchUpdate.as_view(), name='batchupdate'),

]