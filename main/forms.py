from django import forms
from .models import Group, Ticket, User


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'group']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']
