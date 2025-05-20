// Function to dynamically load the header
window.addEventListener('load', () => {
  fetch('header.html') // Load the header content from 'header.html'
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition(); // Adjust sidebar position after header is loaded
      updateContentMargin();    // Adjust content margin based on header height
    })
    .catch(err => console.error('Failed to load header:', err));    
});

// Function to update content margin based on header height and sidebar width
function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.create-poll-page');
  const sidebar = document.getElementById('sidebar');

  if (header && content && sidebar) {
    const headerHeight = header.offsetHeight;
    const sidebarWidth = sidebar.offsetWidth;

    // Always apply header height as top margin
    content.style.marginTop = `${headerHeight}px`;

    // Since sidebar is always fixed and visible, apply margin-left unconditionally
    content.style.marginLeft = `${sidebarWidth}px`;

    // Optional: set min height so content doesn't shrink
    content.style.minHeight = `calc(100vh - ${headerHeight}px)`;
  }
}


// Function to add new answer options dynamically
document.getElementById('add-option').addEventListener('click', () => {
  const answerOptions = document.querySelector('.answer-options');
  const newOption = document.createElement('input');
  newOption.type = 'text';
  newOption.name = 'option[]';
  newOption.placeholder = 'Option ' + String(answerOptions.children.length + 1);
  answerOptions.appendChild(newOption);
});

// Function to handle form submission (Create Poll)
document.getElementById('create-poll-form').addEventListener('submit', function(e) {
  e.preventDefault();  // Prevent default form submission

  const formData = new FormData(this);  // Gather form data
  const pollData = {
    title: formData.get('poll-title'),
    options: formData.getAll('option[]'),
    privacy: formData.get('privacy')
  };

  // For now, just log the data (you can send it to a server or API)
  console.log(pollData);

  // Example: Send the data to a server (use actual endpoint)
  fetch('create_poll_backend.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(pollData), // Send the data in JSON format
  })
    .then(response => response.json())
    .then(data => {
      console.log('Poll created:', data);
      alert('Poll created successfully!');
    })
    .catch(error => {
      console.error('Error creating poll:', error);
      alert('Failed to create poll.');
    });
});

// Save as draft functionality
document.getElementById('save-draft').addEventListener('click', function() {
  const pollData = {
    title: document.getElementById('poll-title').value,
    options: Array.from(document.querySelectorAll('input[name="option[]"]')).map(input => input.value),
    privacy: document.querySelector('input[name="privacy"]:checked').value,
  };

  // Example: Save data locally or in a draft state (store in LocalStorage or database)
  localStorage.setItem('draftPoll', JSON.stringify(pollData));
  alert('Poll saved as draft!');
});

// Optional: Update content margin on window resize
window.addEventListener('resize', () => {
  updateContentMargin(); // Recalculate content margin on window resize
});
