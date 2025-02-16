from django import forms
from .models import Department
from teachers.models import Teacher



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head_of_department', 'desc', 'location', 'email', 'phone', 'status']


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Add department name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'head_of_department': forms.Select(attrs={
                'placeholder': 'Department head name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'desc': forms.Textarea(attrs={
                'placeholder': 'Enter department description',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter department location',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter contact email',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter contact phone',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'subjects': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded text-blue-600',
                'required': False
            }),
            'status': forms.Select(choices=Department.STATUS_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),

        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # head_of_department maydonini Teacher modelidan faqat faol o'qituvchilar bilan to'ldirish
        self.fields['head_of_department'].queryset = Teacher.objects.filter(status='active')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name:
    #         raise forms.ValidationError("Department name is required.")
    #     return name
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