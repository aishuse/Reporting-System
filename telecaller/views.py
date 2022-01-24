from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from admins.models import Batch
from .forms import StudentForm, StudentUpdateForm
from .models import Student


class TeleHome(TemplateView):
    template_name = 'telecaller/telehome.html'


class StudentAdd(CreateView):
    model = Student
    template_name = 'telecaller/studentadd.html'
    form_class = StudentForm
    success_url = '/telecaller/studentadd'

    def form_valid(self, form):
        form.instance.telecaller = self.request.user
        if form.instance.status == 'ADMITTED':
            batch = Batch.objects.get(id=form.data.__getitem__('batch'))
            if batch.available_seat == 0:
                messages.error(self.request, 'SORRY!! No seat available for the selected course')
                return redirect('studentadd')
            else:
                batch.available_seat = batch.available_seat - 1
                batch.save()
        return super(StudentAdd, self).form_valid(form)


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'telecaller/studupdate.html'
    success_url = '/telecaller/listenquires'

    def form_valid(self, form):
        if form.instance.status == 'ADMITTED':
            batch = Batch.objects.get(id=form.data.__getitem__('batch'))
            if batch.available_seat == 0:
                messages.error(self.request, 'SORRY!! No seat available for the selected course')
                return redirect('studentadd')
            else:
                batch.available_seat = batch.available_seat - 1
                batch.save()
        return super(StudentUpdate, self).form_valid(form)



class StudentDelete(DeleteView):
    model = Student
    template_name = 'telecaller/delete.html'
    success_url = '/telecaller/listenquires'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import pdb
        # pdb.set_trace()
        x = context['student']
        if x.status == 'ADMITTED':
            batch = Batch.objects.get(id=x.batch.id)
            batch.available_seat = batch.available_seat + 1
            batch.save()
        return context


def load_cities(request):
    course_id = request.GET.get('course_id')
    print(course_id)
    cities = Batch.objects.filter(course_id=course_id).all()
    print(cities)
    return render(request, 'telecaller/coursebatch.html', {'cities': cities})


class ListEnquires(ListView):
    model = Student
    template_name = 'telecaller/liststudents.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(telecaller=self.request.user)

