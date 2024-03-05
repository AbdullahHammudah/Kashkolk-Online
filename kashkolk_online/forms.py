from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    """a form for users to enter a new topics"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        
class EntryForm(forms.ModelForm):
    """a form for users to enter a new entry for topics""" 
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'clos':80})}
        
    
    
    
