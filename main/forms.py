from django import forms
from .models import Group, Ticket, User, Permission


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'group']


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    user_permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'groups', 'user_permissions']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 == password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address must be unique.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
