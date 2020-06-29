from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from formapp.models import Question

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    
    return render(request,'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    request.session['password']=password
    
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        
        auth.login(request, user)
        return HttpResponseRedirect('/que1')
    else:
        messages.add_message(request,messages.WARNING,'Invalid Login Details')
        return render(request,'login.html')

@login_required(login_url='/login')
def que1(request):
    return render(request,'que1.html')

@login_required(login_url='/login')
def que2(request):
    return render(request,'que2.html')

@login_required(login_url='/login')
def que3(request):
    return render(request,'que3.html')

def ans1(request):
    u = User.objects.get(id = request.user.id)
    que=Question()
    que.user=u
    que.Question1=request.POST['answer1']   
    # que.save()
    return redirect('/que2')

def ans2(request):
    u = User.objects.get(id = request.user.id)
    que=Question.objects.get(user=u)    
    que.Question2=request.POST['answer2']
    # que.save()
    return redirect('/que3')

def ans3(request):
    u = User.objects.get(id = request.user.id)
    que=Question.objects.get(user=u)    
    que.Question3=request.POST['answer3']
    # que.save()
    return redirect('/thanks')

def thanks(request):
    return render(request,'thanks.html')

def logout_request(request):
    logout(request)
    return redirect('/login')