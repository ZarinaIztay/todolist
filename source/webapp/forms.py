from django import forms
from django.forms import widgets
from webapp.models import Type, Status


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    description = forms.CharField(max_length=500, required=False, label='Description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Type')
