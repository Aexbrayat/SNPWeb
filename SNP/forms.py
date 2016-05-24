from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ConnexionForm(forms.Form):
	username = forms.CharField(label="User name", max_length=30)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	
#~ BOITE MAIL 
class ContactForm(forms.Form):
	required_css_class = 'required'
	Your_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea)

#~ registration
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
		
