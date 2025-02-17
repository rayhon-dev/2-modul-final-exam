from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
    }), label="Email")

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
    }), label="Password")

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Email yoki parol noto‘g‘ri!")

        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
    )

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-md'})
    )

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="New Password"
    )

    repeat_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        label="Repeat Password"
    )

    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['username'].initial = user.username

        for field_name in self.fields:
            if field_name not in ["birth_date", "new_password", "repeat_password"]:
                self.fields[field_name].widget.attrs.update({
                    'class': 'w-full px-3 py-2 border rounded-md'
                })

        self.fields['bio'].widget.attrs.update({'rows': '4'})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and CustomUser.objects.filter(username=username).exclude(id=self.instance.user.id).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        repeat_password = cleaned_data.get("repeat_password")

        if new_password or repeat_password:
            if new_password != repeat_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user = user_profile.user

        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user.set_password(new_password)
            user.save()

        username = self.cleaned_data.get("username")
        if username:
            user.username = username
            user.save()

        if commit:
            user_profile.save()

        return user_profile