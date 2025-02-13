from .forms import SubjectForm
from .models import Subject
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from departments.models import Department
from django.http import HttpResponseRedirect





class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'
    paginate_by = 10

    def get_queryset(self):
        subjects = Subject.objects.all()

        department_filter = self.request.GET.get('department')
        grade_level_filter = self.request.GET.get('grade_level')
        status_filter = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if department_filter:
            subjects = subjects.filter(department_id=department_filter)

        if grade_level_filter:
            subjects = subjects.filter(grade_level_id=grade_level_filter)

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

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return HttpResponseRedirect(self.success_url)
    #
    # def form_invalid(self, form):
    #     print(form.errors)
    #     return HttpResponseRedirect(self.success_url)


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'


class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    fields = ['name', 'department', 'desc', 'credit_hours', 'grade_level', 'prerequisites']
    success_url = reverse_lazy('subjects:list')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/delete-confirm.html'
    success_url = reverse_lazy('subjects:list')
