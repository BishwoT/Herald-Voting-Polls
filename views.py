from django.shortcuts import render, redirect
from django.contrib import messages

# ✅ Your verify code view
def verify_code_view(request):
    if request.method == 'POST':
        user_input_code = request.POST.get('code')
        stored_code = request.session.get('verification_code')  # assume this was set earlier

        if user_input_code == stored_code:
            messages.success(request, 'Verification successful! 🎉')
            return redirect('signup')  # or wherever you want to take them next
        else:
            messages.error(request, 'Invalid verification code. Try again.')

    return render(request, 'verify_code.html')
