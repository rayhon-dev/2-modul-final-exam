from .models import Group
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from teachers.models import Teacher
from subjects.models import Subject
from .forms import GroupForm
from django.contrib.auth.mixins import LoginRequiredMixin






class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    paginate_by = 10

    def get_queryset(self):
        groups = Group.objects.all()

        # Fetch filter criteria from GET parameters
        grade_level_filter = self.request.GET.get('grade_level')
        class_teacher_filter = self.request.GET.get('class_teacher')
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        # Filter by head_of_department if provided
        if grade_level_filter:
            groups = groups.filter(grade_level_id=grade_level_filter)

        if class_teacher_filter:
            groups = groups.filter(class_teacher_id=class_teacher_filter)




        # Filter by status
        if status:
            groups = groups.filter(status=status)

        # Filter by department name (search query)
        if search_query:
            groups = groups.filter(name__icontains=search_query)

        return groups

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all teachers for head_of_department filtering
        context['class_teacher'] = Teacher.objects.all()
        context['subjects'] = Subject.objects.all()

        return context


class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Ensure that active teachers are used in the form field
        kwargs['initial'] = {'class_teacher': Teacher.objects.filter(status='active')}
        return kwargs

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups:list')


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/delete-confirm.html'
    success_url = reverse_lazy('groups:list')
