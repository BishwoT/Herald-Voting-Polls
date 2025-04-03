from django import forms
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

# Custom form to validate the email domain during login
class LoginEmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@heraldcollege.edu.np'):
            raise ValidationError("Email must end with '@heraldcollege.edu.np'.")
        return email

# Login view function
def user_login(request):
    if request.method == 'POST':
        form = LoginEmailForm(request.POST)
        if form.is_valid():
            # Get the cleaned data (just email for now)
            email = form.cleaned_data['email']
            
            # Simulate a successful login (no password check)
            return redirect('home')  # Redirect to home page after successful login
    else:
        form = LoginEmailForm()

    return render(request, 'accounts/login.html', {'form': form})
