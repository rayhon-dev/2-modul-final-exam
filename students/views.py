from .models import Student
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy




class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'



class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    fields = ['photo', 'first_name', 'last_name', 'gender', 'dob', 'email', 'phone', 'group', 'grade', 'address', 'parent_name', 'parent_email', 'parent_phone' ]
    success_url = reverse_lazy('student_list')

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    fields = ['photo', 'first_name', 'last_name', 'gender', 'dob', 'email', 'phone', 'group', 'grade', 'address', 'parent_name', 'parent_email', 'parent_phone' ]
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/delete-confirm.html'
    success_url = reverse_lazy('student_list')
