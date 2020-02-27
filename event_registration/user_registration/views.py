from django.shortcuts import redirect, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Role, Config, UserForm, User
from django.urls import reverse
import datetime

def index(request):
    context = {
        'roles': Role.objects.all(),
        'config': Config.objects.all()[:1].get()
    }

    if request.POST:
        form = UserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            data = form.save(commit=False)
            data.registered_date = datetime.datetime.now()
            if User.objects.all().count() >= context['config'].registration_cap:
                data.status = 'Waitlist'
                context['warn'] = "We have reached the maximum capacity for this event. You have been added to the waitlist"
            else:
                data.status = 'Registered'
                context['success'] = "You have been registered!"

            data.save()
    
    return render_to_response('registration_form/index.html', context)