from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    prerequisites = forms.MultipleChoiceField(
        choices=Subject.PREREQUISITES_CHOICES,
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
    class Meta:
        model = Subject
        fields = ['name', 'department', 'desc', 'credit_hours', 'grade_level', 'prerequisites', 'levels', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter subject name'}),
            'department': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'desc': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter subject description'}),
            'credit_hours': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter credit hours' }),
            'grade_level': forms.Select(attrs={'type': 'email', 'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter contact email'}),
            'levels': forms.Select(attrs={'class':'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter contact phone'}),
            'status': forms.Select(choices=Subject.STATUS_CHOICES, attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),

        }

    def clean_prerequisites(self):
        prerequisites = self.cleaned_data.get('prerequisites')
        # Join the selected prerequisites into a comma-separated string
        return ",".join(prerequisites)


