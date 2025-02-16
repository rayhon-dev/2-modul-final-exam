from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, UserProfile



class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'block w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(disabled=True, required=False)
    class Meta:
        model = UserProfile
        fields = ('bio', 'phone', 'birth_date')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['email'].initial = user.email

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-opacity-50'
            }) 