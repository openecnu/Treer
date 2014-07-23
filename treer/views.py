#coding=utf-8
from django.shortcuts import render_to_response
from treer.forms import ContactForm
from django.core.mail import send_mail
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect

def index(request):
	return render_to_response('index.html',{})

def log(request):
	return render_to_response('log.html',{})

# def email(request):
#     return render_to_response('email.html',{})

def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            theme = form.cleaned_data['subject'] 
            message = form.cleaned_data['message'] 
            sender = form.cleaned_data['email']
            send_mail( 
                "From[Treer] : %s" % theme, 
                "By: %s , Message: %s" % (sender,message), 'pytreer@163.com', 
                ['pytreer@163.com'],
            ) 
            return HttpResponseRedirect('/thanks/') 
    else: 
        form = ContactForm() 
    return render_to_response('contact.html',locals(), context_instance=RequestContext(request))

def thanks(request): 
    return render_to_response('thanks.html', {}, context_instance=RequestContext(request))

def error_404(request):
    return render_to_response('404.html',{})

def error_500(request):
    return render_to_response('500.html',{})

