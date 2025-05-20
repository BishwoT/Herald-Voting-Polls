// Helper to get a cookie value by name (used for CSRF token)
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

// Load the header dynamically and then load profile data
window.addEventListener('load', () => {
  fetch('header.html')
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition();
      updateContentMargin();
      loadProfile();  // Load profile data after header loads
    })
    .catch(err => console.error('Failed to load header:', err));
});

// Update content margin based on header height and sidebar width
function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.profile-page');
  const sidebar = document.getElementById('sidebar');

  if (header && content && sidebar) {
    const headerHeight = header.offsetHeight;
    const sidebarWidth = sidebar.offsetWidth;

    content.style.marginTop = `${headerHeight}px`;
    content.style.marginLeft = `${sidebarWidth}px`;
    content.style.minHeight = `calc(100vh - ${headerHeight}px)`;
  }
}

// Update sidebar position and height based on header height
function updateSidebarPosition() {
  const header = document.querySelector('.header');
  const sidebar = document.getElementById('sidebar');

  if (header && sidebar) {
    const headerHeight = header.offsetHeight;
    sidebar.style.top = `${headerHeight}px`;
    sidebar.style.height = `calc(100vh - ${headerHeight}px)`;
  }
}

// Adjust layout on window resize
window.addEventListener('resize', () => {
  updateContentMargin();
  updateSidebarPosition();
});

// Load profile data and populate form & info section
async function loadProfile() {
  try {
    const response = await fetch('http://localhost:8000/account/account', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
    });

    if (!response.ok) throw new Error('Failed to load profile data');
    const data = await response.json();

    // Update info section
    document.getElementById('profile-name').textContent = data.name || '';
    document.getElementById('profile-email').textContent = data.email || '';
    if (data.profile_pic_url) {
      document.getElementById('profile-img').src = data.profile_pic_url;
    }

    // Update edit form fields
    document.getElementById('name').value = data.name || '';
    document.getElementById('email').value = data.email || '';

  } catch (error) {
    console.error('Error loading profile:', error);
  }
}

// Handle form submit for profile update
document.getElementById('profile-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData();
  formData.append('name', document.getElementById('name').value);
  formData.append('email', document.getElementById('email').value);

  const fileInput = document.getElementById('profile-pic');
  if (fileInput.files.length > 0) {
    formData.append('profile_pic', fileInput.files[0]);
  }

  try {
    const response = await fetch('http://localhost:8000/account/account/edit/', {
      method: 'PUT',
      credentials: 'include',
      headers: {
        'X-CSRFToken': csrftoken,  // Include CSRF token header
      },
      body: formData,
      // Note: Do NOT set Content-Type header with FormData — browser sets it automatically
    });

    if (!response.ok) {
      const errData = await response.json();
      throw new Error(errData.error || 'Failed to update profile');
    }

    const updated = await response.json();

    // Update info section to reflect changes immediately
    document.getElementById('profile-name').textContent = updated.name || '';
    document.getElementById('profile-email').textContent = updated.email || '';
    if (updated.profile_pic_url) {
      document.getElementById('profile-img').src = updated.profile_pic_url;
    }

    alert('Profile updated successfully!');
  } catch (err) {
    alert('Error updating profile: ' + err.message);
    console.error(err);
  }
});

// Initial load
window.addEventListener('load', loadProfile);

