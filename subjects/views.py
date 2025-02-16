from .forms import SubjectForm
from .models import Subject
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from departments.models import Department
from django.contrib.auth.mixins import LoginRequiredMixin






class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'
    paginate_by = 10

    def get_queryset(self):
        subjects = Subject.objects.all()

        department_filter = self.request.GET.get('department')
        grade_level_filter = self.request.GET.get('grade_level')
        levels_filter = self.request.GET.get('levels')
        status_filter = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if department_filter:
            subjects = subjects.filter(department_id=department_filter)

        if grade_level_filter:
            subjects = subjects.filter(grade_level_id=grade_level_filter)

        if levels_filter:
            subjects = subjects.filter(levels_id=levels_filter)

        if status_filter:
            subjects = subjects.filter(status=status_filter)

        if search_query:
            subjects = subjects.filter(
                name__icontains=search_query,

            )


        return subjects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['departments'] = Department.objects.all()

        return context


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')




class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = self.object.teachers.all()  # Assuming there is a Many-to-Many relationship
        return context


class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/delete-confirm.html'
    success_url = reverse_lazy('subjects:list')
