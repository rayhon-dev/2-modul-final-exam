from django import forms
from .models import Teacher
from teachers.models import Teacher



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo', 'first_name', 'last_name', 'department', 'subjects', 'qualification', 'email', 'phone', 'address', 'employment_type',  'status', 'joined_date']
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
            'department': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'subjects': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded text-blue-600',
                'required': False
            }),
            'qualification': forms.TextInput(attrs={
                'placeholder': 'Enter qualification',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Enter full address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'employment_type': forms.Select(choices=Teacher.EMPLOYMENT_TYPES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'status': forms.Select(choices=Teacher.STATUS_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'joined_date': forms.DateInput( attrs={
                'type':'date',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),

        }



    # def clean_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     # if not first_name:
    #     #     raise forms.ValidationError("First name is required.")
    #     # last_name = self.cleaned_data.get('last_name')
    #     # if not last_name:
    #     #     raise forms.ValidationError("Last name is required.")
    #     return first_name
    #
    # def clean_desc(self):
    #     desc = self.cleaned_data.get('desc')
    #     if not desc:
    #         raise forms.ValidationError("Description is required.")
    #     return desc
    #
    # def clean_location(self):
    #     location = self.cleaned_data.get('location')
    #     if not location:
    #         raise forms.ValidationError("Location is required.")
    #     return location
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email:
    #         raise forms.ValidationError("Email is required.")
    #     return email
    #
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone:
    #         raise forms.ValidationError("Phone number is required.")
    #     return phone