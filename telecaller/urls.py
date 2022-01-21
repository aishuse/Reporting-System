from django.urls import path
from . import views

urlpatterns = [
    path('studentadd', views.StudentAdd.as_view(), name='studentadd'),
    path('telehome', views.TeleHome.as_view(), name='telehome'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
    path('enquires/list', views.ListEnquires.as_view(), name='listenquires')

]