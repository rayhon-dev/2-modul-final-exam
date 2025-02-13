from django.shortcuts import render
from .models import Department
from teachers.models import Teacher
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DepartmentForm
from subjects.models import Subject
from groups.models import Group
from students.models import Student



def home(request):
    total_groups = Group.objects.count()
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()
    total_teachers = Teacher.objects.count()
    subject_names = [subject.name for subject in Subject.objects.all()]
    subject_teachers_counts = [subject.teachers.count() for subject in Subject.objects.all()]

    ctx = {
        'total_groups': total_groups,
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_teachers': total_teachers,
        'subject_names': subject_names,
        'subject_teachers_counts': subject_teachers_counts,
    }
    return render(request, 'dashboard.html', ctx)

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        departments = Department.objects.all()

        # Fetch filter criteria from GET parameters
        head_of_department = self.request.GET.get('head_of_department')
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        # Filter by head_of_department if provided
        if head_of_department:
            departments = departments.filter(head_of_department=head_of_department)

        # Filter by status
        if status:
            departments = departments.filter(status=status)

        # Filter by department name (search query)
        if search_query:
            departments = departments.filter(name__icontains=search_query)

        return departments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all teachers for head_of_department filtering
        context['heads_of_department'] = Teacher.objects.all()

        return context


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:list')

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
