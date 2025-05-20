document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('otp-form');

  // Helper to get CSRF token from cookie
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');

  // Get email, name, and password from sessionStorage or wherever you stored it from signup form
  const email = sessionStorage.getItem('signupEmail');
  const name = sessionStorage.getItem('signupName');
  const password = sessionStorage.getItem('signupPassword');

  if (!email || !name || !password) {
    alert('Missing signup info. Please start from the signup page.');
    window.location.href = 'signup.html';
    return;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const code = form.elements['otp'].value.trim();

    if (!code) {
      alert('Please enter the OTP.');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/account/signup/complete/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
        body: JSON.stringify({ email, code, name, password }),
      });

      if (response.ok) {
        alert('🎉 Successfully registered! Please login to continue.');
        // Clear sensitive info from storage
        sessionStorage.removeItem('signupEmail');
        sessionStorage.removeItem('signupName');
        sessionStorage.removeItem('signupPassword');
        window.location.href = 'login.html';
      } else {
        const errorData = await response.json();
        alert('Verification failed: ' + JSON.stringify(errorData));
      }
    } catch (error) {
      alert('Network error: ' + error.message);
    }
  });
});
