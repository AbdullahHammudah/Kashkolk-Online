from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('kashkolk_online:index'))
    
    
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display a blank registeration form
        form = UserCreationForm ()
    else:
        form = UserCreationForm (data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to the hompage
            authenticated_user = authenticate(username = new_user.username,
                password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect( reverse('kashkolk_online:index'))
            
    context = {'form':form}
    return render(request,'users/register.html',context)


