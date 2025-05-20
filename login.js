document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.login-form');

  // Function to get CSRF token from cookies
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

    const email = form.elements['email'].value.trim();
    const password = form.elements['password'].value;

    const data = { email, password };

    try {
      const response = await fetch('http://localhost:8000/account/login/', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken  // Include CSRF token here
        },
        body: JSON.stringify(data),
        credentials: 'include', // Include cookies for session auth
      });

      if (response.ok) {
        const result = await response.json();
        alert('Login successful! Welcome, ' + (result.name || result.email));
        window.location.href = 'browse.html'; // change to your dashboard URL
      } else {
        const errorData = await response.json();
        alert('Login failed: ' + (errorData.error || 'Unknown error'));
      }
    } catch (error) {
      alert('Network error: ' + error.message);
    }
  });
});
