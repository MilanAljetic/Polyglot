from django.urls import path, include
from language import views

urlpatterns = [
    path('group_list/', views.Group_list.as_view(), name='group_list'),
    path('group_list/new_group/', views.New_group.as_view(), name='new_group'),
    path('group_list/group_content/',
         views.Group_content.as_view(), name='group_content'),
    path('group_list/group_content/new_post/',
         views.New_post.as_view(), name='new_post'),

]
