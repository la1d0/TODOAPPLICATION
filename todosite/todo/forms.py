from django import forms
from .models import Todotask


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Todotask
        fields = ['title', 'content']