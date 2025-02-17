from django.http import HttpResponseRedirect

from .forms import TeacherForm
from .models import Teacher
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from departments.models import Department
from subjects.models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin



class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'
    paginate_by = 10

    def get_queryset(self):
        teachers = Teacher.objects.all()

        department_filter = self.request.GET.get('department')
        subject_filter = self.request.GET.get('subject')
        status_filter = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if department_filter:
            teachers = teachers.filter(department_id=department_filter)

        if subject_filter:
            teachers = teachers.filter(subjects__id=subject_filter)

        if status_filter:
            teachers = teachers.filter(status=status_filter)

        if search_query:
            teachers = teachers.filter(
                first_name__icontains=search_query,
                last_name__icontains=search_query,
                email__icontains=search_query
            )

        return teachers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['departments'] = Department.objects.all()
        context['subjects'] = Subject.objects.all()

        return context


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')



class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete-confirm.html'
    success_url = reverse_lazy('teachers:list')
