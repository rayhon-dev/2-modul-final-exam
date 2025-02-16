from django import forms
from students.models import Student
from groups.models import Group



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['photo', 'first_name', 'last_name', 'gender', 'dob', 'email', 'phone', 'group', 'grade_level',  'address', 'parent_name', 'parent_email', 'parent_phone', 'status', 'subjects', 'relationship', 'enrollment_date']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'px-4 py-2 border rounded-lg hover:bg-gray-50'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder':'Enter email address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'group': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'

            }),
            'grade_level': forms.Select(choices=Student.GRADE_LEVEL,attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Enter full address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'parent_name': forms.TextInput(attrs={
                'placeholder': 'Enter parent/guardian name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'parent_phone': forms.TextInput(attrs={
                'placeholder': 'Enter parent/guardian phone',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'parent_email': forms.EmailInput(attrs={
                'placeholder': 'Enter parent/guardian email',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'status': forms.Select(choices=Student.STATUS_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'subjects': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded text-blue-600',
                'required': False
            }),
            'relationship': forms.TextInput(attrs={
                'placeholder': 'e.g Father/Mother',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.filter(status='active')



