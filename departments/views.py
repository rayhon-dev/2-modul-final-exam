from .models import Department
from teachers.models import Teacher
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DepartmentForm
from subjects.models import Subject
from groups.models import Group
from students.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from json import dumps
from django.db.models import Count
from django.db.models.functions import ExtractMonth


class DashboardView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)


        total_students = Student.objects.filter(
            status='active').count()
        total_teachers = Teacher.objects.filter(status='active').count()
        total_groups = Group.objects.filter(status='active').count()
        total_subjects = Subject.objects.all().count()


        ctx['teachers'] = Teacher.objects.all()
        ctx['groups'] = Group.objects.all()
        ctx['subjects'] = Subject.objects.all()
        ctx['total_students'] = total_students
        ctx['total_teachers'] = total_teachers
        ctx['total_groups'] = total_groups
        ctx['total_subjects'] = total_subjects


        ctx['subject_names'] = [subject.name for subject in Subject.objects.all()]
        ctx['subject_teachers_counts'] = [subject.teachers.count() for subject in Subject.objects.all()]


        enrollments = (
            Student.objects.filter(status='active')
            .annotate(month=ExtractMonth('created_at'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )

        enrollment_data = {i: 0 for i in range(1, 13)}
        for enrollment in enrollments:
            enrollment_data[enrollment['month']] = enrollment['count']

        ctx['enrollment_counts'] = dumps(list(enrollment_data.values()))

        return ctx


class DepartmentListView(LoginRequiredMixin,ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        departments = Department.objects.all()


        head_of_department_filter = self.request.GET.get('head_of_department')
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')


        if head_of_department_filter:
            departments = departments.filter(head_of_department_id=head_of_department_filter)



        if status:
            departments = departments.filter(status=status)


        if search_query:
            departments = departments.filter(name__icontains=search_query)

        return departments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['heads_of_department'] = Teacher.objects.all()

        return context


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'head_of_department': Teacher.objects.filter(status='active')}
        return kwargs

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'


class DepartmentUpdateView( UpdateView):
    model = Department
    template_name = 'departments/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:list')


class DepartmentDeleteView( DeleteView):
    model = Department
    template_name = 'departments/delete-confirm.html'
    success_url = reverse_lazy('departments:list')
