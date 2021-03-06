from django import forms
from django.db.models import fields
from .models import Group, Group_post


class GroupForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = ('name', 'description')


class PostForm(forms.ModelForm):
    class Meta():
        model = Group_post
        fields = ('author', 'group', 'text')
