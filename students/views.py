from .models import Student
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm
from groups.models import Group
from subjects.models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin





class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        students = Student.objects.all()

        group_filter = self.request.GET.get('group')
        grade_level_filter = self.request.GET.get('grade_level')
        status_filter = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if group_filter:
            students = students.filter(group_id=group_filter)

        if grade_level_filter:
            students = students.filter(grade_level=grade_level_filter)

        if status_filter:
            students = students.filter(status=status_filter)

        if search_query:
            students = students.filter(
                first_name__icontains=search_query,
                last_name__icontains=search_query,
                email__icontains=search_query
            )

        return students

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['groups'] = Group.objects.all()
        context['subjects'] = Subject.objects.all()

        return context


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Ensure that active teachers are used in the form field
        kwargs['initial'] = {'group': Group.objects.filter(status='active')}
        return kwargs



class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/delete-confirm.html'
    success_url = reverse_lazy('students:list')
