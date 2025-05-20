document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.signup-form');

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

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = form.elements['name'].value.trim();
    const email = form.elements['email'].value.trim();
    const password = form.elements['password'].value;

    if (!name || !email || !password) {
      alert('Please enter your name, email, and password.');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/account/otp/request/', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ email, purpose: 'registration' }),
        credentials: 'include',
      });

      if (response.ok) {
        alert('OTP sent to your email. Please check and enter it on the next page.');
        sessionStorage.setItem('signupName', name);
        sessionStorage.setItem('signupEmail', email);
        sessionStorage.setItem('signupPassword', password);
        window.location.href = 'signup-verify.html';
      } else {
        const errorData = await response.json();
        alert('Failed to send OTP: ' + JSON.stringify(errorData));
      }
    } catch (error) {
      alert('Network error: ' + error.message);
    }
  });
});
