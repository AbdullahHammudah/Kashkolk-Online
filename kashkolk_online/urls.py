"""Defines URL patterns for learning logs."""

from django.urls import path
from . import views

app_name = 'kashkolk_online'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    
    # Topics page
    path('topics', views.topics, name='topics'),
    
    #Detail page for a single 
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    
    #page for adding new topics
    path('new_topic', views.new_topic, name='new_topic'),
    
    #page for adding new topics for the entries
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
    
    #page for editting an existing entry
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
    
    ]
