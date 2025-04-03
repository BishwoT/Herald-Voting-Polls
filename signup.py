from django import forms
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

# Custom form to validate the email domain
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@heraldcollege.edu.np'):
            raise ValidationError("Email must end with '@heraldcollege.edu.np'.")
        return email

# Sign up view function
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Get the cleaned data (just email and username for now)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            # You can choose to save this user in the database later
            # For now, just simulate successful registration
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
