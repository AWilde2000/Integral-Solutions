from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

def register(request):
    register_form = SignUpForm()
    context = {}
    baseActFields = []
    otherFields = []
    baseActFieldNames = ['username', 'password1', 'password2']
    for field in register_form:
        if(field.name in baseActFieldNames):
            baseActFields.append(field)
        else:
            otherFields.append(field)
    context['baseFields'] = baseActFields
    context['otherFields'] = otherFields
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #User model fields will go here, underlying principle of this
            #page now works.

            form.save()

            return HttpResponseRedirect('/')    #We will send the user to a verification notification
                                                #page, in the future, for now we send them to home page
        else:
            errors = []

            for field in form:
                if(field.errors):
                    errors.append(field.errors)
            
            context['errors'] = errors

            
            return render(request,'registration/register.html',context=context)
    else:
        context['form'] = register_form
        return render(request,'registration/register.html',context=context)