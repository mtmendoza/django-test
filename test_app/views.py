from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import forms

def home(request):
    return render(request, 'index.html', {'header': 'Welcome!'})

def index(request):
    # check if request is post
    if request.method == 'POST':

        # get values from post form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # assign  values to context var to pass
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        # getting template
        template = loader.get_template('show.html')

        return HttpResponse(template.render(context, request))
    else:

        # if not a post request
        # go to form - before submit
        form = forms.PersonalDataForm()

        #template = loader.get_template('form.html')
        #return HttpResponse(template.render())

        return render(request, 'form.html' , {'form' : form})

def signup(request):
    #if post submit
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            context = {
                'header': 'Thanks for signing up!',
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email'],
                'phone' : request.POST.get('phone')
            }

            return render(request, 'index.html', context)

    else:
        #creating new form
        form = forms.SignUpForm()

        return render(request,'signupform.html', {'form':form})