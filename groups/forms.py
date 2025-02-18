from django import forms
from .models import Group
from teachers.models import Teacher



class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','grade_level','class_teacher', 'academic_year', 'schedule', 'max_students', 'desc', 'subjects', 'status']


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter group name',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'grade_level': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'class_teacher': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'schedule': forms.Select(attrs={
                'placeholder': 'Enter department description',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'academic_year': forms.TextInput(attrs={
                'placeholder': 'e.g., 2023-2024',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'max_students': forms.NumberInput(attrs={
                'placeholder': 'Enter maximum number of students',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'desc': forms.Textarea(attrs={
                'placeholder': 'Enter group description',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'subjects': forms.CheckboxSelectMultiple(attrs={
                'class': 'mr-2',
                'required': False
            }),
            'status': forms.Select(choices=Group.STATUS_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),

        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['class_teacher'].queryset = Teacher.objects.filter(status='active')

