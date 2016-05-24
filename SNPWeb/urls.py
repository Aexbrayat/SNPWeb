"""SNPWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from SNP import views
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth.decorators import login_required

urlpatterns = patterns ('',
    url( r'^admin/', admin.site.urls ),
    url( r'^$', 'SNP.views.home', name='home' ),
    url( r'^login/$', 'SNP.views.login' ),
    url( r'^auth/$', 'SNP.views.auth_view' ),
    url( r'^logout/$', 'SNP.views.logout' ),
    url( r'^logoutchoice/$', 'SNP.views.logoutchoice' ),
    url( r'^invalidaccount/$', 'SNP.views.invalidaccount'),
#~ Registration
	url( r'^register/$', 'SNP.views.register_user'),
	url( r'^register_success/$', 'SNP.views.register_success'),
	
    url( r'^userhomepage/$', 'SNP.views.userhome' ),
    url( r'^allsnp/$', 'SNP.views.allsnp' ),
    url( r'^trait/$', 'SNP.views.trait' ),
    url( r'^schizophrenia/$', 'SNP.views.schizophrenia' ),
    url( r'^blond_hair/$', 'SNP.views.blondhair' ),
    url( r'^cleft_palate/$', 'SNP.views.cleftpalate' ),
#~ BOITE MAIL
    url( r'^contact/$', 'SNP.views.contact'),
    url( r'^contactlog/$', 'SNP.views.contactlog'),
	url(r'^mailsend/$', 'SNP.views.mailsend'),
	url(r'^mailsendlog/$', 'SNP.views.mailsendlog'),
#~ resetpassword
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
        
    
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
