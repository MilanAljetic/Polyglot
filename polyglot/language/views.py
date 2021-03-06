from django.shortcuts import redirect, render
from language.models import Language_learn, Language_nativ, User_profile, Rate, Group, Group_post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from datetime import datetime
from .form import GroupForm, PostForm
from django.urls import reverse


class User_list(ListView):
    template_name = 'base.html'
    model = User_profile

    def get_queryset(self):
        object_list = User_profile.objects.all()
        return object_list


class Group_list(ListView):
    template_name = 'group_list.html'
    model = Group

    def get_queryset(self):
        object_list = Group.objects.all()
        return object_list


class New_group(CreateView):
    template_name = 'group_form.html'
    model = Group
    form_class = GroupForm

    def get_success_url(self):
        return reverse('group_list')


class Group_content(ListView):
    template_name = 'group_content.html'
    model = Group_post
    form_class = PostForm

    def get_queryset(self):
        object_list = Group_post.objects.all()
        return object_list


class New_post(CreateView):
    template_name = 'new_post.html'
    model = Group_post
    form_class = PostForm

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(New_post, self).form_valid(form)

    def get_success_url(self):
        return reverse('group_content')
