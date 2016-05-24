#~ BOITE MAIL
from django.shortcuts import render, render_to_response , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from models import SNP
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
#~ BOITE MAIL
from django.core.mail import send_mail, BadHeaderError
from SNP.forms import ContactForm
#~ Registration
from forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext


def home (request) :
	
	return render_to_response("SNP/home.html")
	
def login ( request ) :
	
	c = {}
	c.update( csrf( request) )
	return render_to_response('SNP/registration/login.html', c)
	
def auth_view ( request ) :
	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate( username = username, password = password )
	
	if user is not None : 
		
		auth.login( request, user)
		return HttpResponseRedirect( '/userhomepage/' )
		
	else :	
		
		return HttpResponseRedirect( '/invalidaccount/' )

def loggedin ( request ) :
	
	return render_to_response('SNP/registration/connected.html', { 'full_name' : request.user.username } )
	
def invalidaccount ( request ) :
	
	return render_to_response('SNP/registration/invalidaccount.html' )

def logout ( request ) :
	
	auth.logout( request )
	return render_to_response('SNP/registration/logout.html' )
	
@login_required
def logoutchoice ( request ) :

	return render_to_response('SNP/registration/logoutchoice.html' )

#~ registration
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():           
            form.save()

            return HttpResponseRedirect('/register_success/')
    else:
        args['form'] = RegistrationForm()   

    return render_to_response('SNP/registration/register.html', args, context_instance=RequestContext(request))

def register_success(request):
	return render_to_response('SNP/registration/register_success.html')


@login_required
def userhome ( request ) :
	return render_to_response("SNP/userpart/userhome.html", { 'full_name' : request.user.username } )

@login_required
def allsnp ( request ) :
	all_snps = SNP.objects.all().order_by('trait')
	return render_to_response("SNP/userpart/allsnp.html", {'full_name' : request.user.username, 'all_snps' : all_snps})
	
@login_required
def trait ( request ) :
	all_trait = SNP.objects.values('trait').distinct().order_by('trait')
	return render_to_response("SNP/userpart/alltrait.html", {'full_name' : request.user.username, 'all_trait' : all_trait})
	
@login_required
def schizophrenia ( request ) :
	all_schizophrenia = SNP.objects.all().filter(trait = 'schizophrenia').order_by('type_snps')
	return render_to_response("SNP/userpart/schizophrenia.html", {'full_name' : request.user.username, 'all_schizophrenia' : all_schizophrenia})
	
@login_required
def blondhair ( request ) :
	all_blondhair = SNP.objects.all().filter(trait = 'blond_hair').order_by('type_snps')
	return render_to_response("SNP/userpart/trait_blondhair.html", {'full_name' : request.user.username, 'all_blondhair' : all_blondhair})

@login_required
def cleftpalate ( request ) :
	all_cleftpalate = SNP.objects.all().filter(trait = 'cleft_palate').order_by('type_snps')
	return render_to_response("SNP/userpart/trait_cleftpalate.html", {'full_name' : request.user.username, 'all_cleftpalate' : all_cleftpalate})

#~ BOITE MAIL pip install sendgrid-django
def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['Your_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['snpweb.contact@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render_to_response('SNP/mailsend.html')
	return render(request, "SNP/contact.html", {'form': form})
	
def mailsend(request):
    return render_to_response('SNP/mailsend.html', message='Save complete')	
    
@login_required	
def contactlog(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['Your_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['snpweb.contact@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render_to_response('SNP/mailsendlog.html')
	return render(request, "SNP/contactlog.html", {'form': form,'full_name' : request.user.username})
@login_required		
def mailsendlog(request):
    return render_to_response('SNP/mailsendlog.html', message='Save complete')	
