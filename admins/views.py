from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView

from admins.forms import CourseForm, BatchForm
from admins.models import Course, Batch
from authapp.admin import UserCreationForm
from authapp.forms import MyUserForm
from authapp.models import MyUser
from telecaller.models import Student


class Home(TemplateView):
    template_name = 'admins/home.html'


class Base(TemplateView):
    template_name = 'admins/base.html'


class AddCourse(CreateView):
    template_name = 'admins/course.html'
    model = Course
    form_class = CourseForm
    success_url = 'courses'


class ListCourse(ListView):
    template_name = 'admins/listcourse.html'
    model = Course
    context_object_name = 'courses'


class CourseDelete(DeleteView):
    model = Course
    template_name = 'admins/delete.html'
    success_url = '/admins/course/list'


class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'admins/courseupdate.html'
    success_url = '/admins/course/list'


class AddBatch(CreateView):
    template_name = 'admins/batch.html'
    model = Batch
    form_class = BatchForm
    success_url = 'batches'


class ListBatches(ListView):
    template_name = 'admins/listbatch.html'
    model = Batch
    context_object_name = 'batches'

class BatchDelete(DeleteView):
    model = Batch
    template_name = 'admins/delete.html'
    success_url = '/admins/batch/list'


class BatchUpdate(UpdateView):
    model = Batch
    form_class = BatchForm
    template_name = 'admins/batchupdate.html'
    success_url = '/admins/batch/list'



class AddTelecaller(CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'admins/telesignup.html'
    success_url = '/admins/telecaller/list'

    def form_valid(self, form):
        form.instance.role = MyUser.TELECALLER
        return super(AddTelecaller, self).form_valid(form)


class ListTelecallers(ListView):
    model = MyUser
    template_name = 'admins/telecallers.html'
    context_object_name = 'telecallers'



class TelecallerDelete(DeleteView):
    model = MyUser
    template_name = 'admins/delete.html'
    success_url = '/admins/telecaller/list'


class TelecallerUpdate(UpdateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'admins/teleupdate.html'
    success_url = '/admins/telecaller/list'




