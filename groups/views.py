from .models import Group
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy




class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'



class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/form.html'
    fields = ['name', 'class_teacher', 'academic_year', 'grade_level', 'schedule', 'max_students', 'desc', 'subjects' ]
    success_url = reverse_lazy('group_list')

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'groups/form.html'
    fields = ['name', 'class_teacher', 'academic_year', 'grade_level', 'schedule', 'max_students', 'desc', 'subjects' ]
    success_url = reverse_lazy('group_list')


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/delete-confirm.html'
    success_url = reverse_lazy('group_list')
