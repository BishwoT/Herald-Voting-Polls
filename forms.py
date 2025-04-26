
from django import forms

class OTPForm(forms.Form):
    otp_code = forms.CharField(max_length=6, label="Enter OTP")




class OTPForm(forms.Form):
    otp_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))


from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
