// Function to dynamically load the header into the page
window.addEventListener('load', () => {
  fetch('header.html') // Load the header content from 'header.html'
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition(); // Adjust sidebar position after header is loaded
      updateContentMargin();    // Adjust content margin based on header height and sidebar width
    })
    .catch(err => console.error('Failed to load header:', err));
  
  // Initialize form submission
  initializeFormSubmission();
});

// Function to update content margin based on header height and sidebar width
function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.help-center-page');
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


// Function to handle form submission (Send data to server or log it)
function initializeFormSubmission() {
  const submitButton = document.getElementById('submit-btn');
  
  if (submitButton) {
    submitButton.addEventListener('click', () => {
      const problemDescription = document.querySelector('.problem-textbox').value;

      // Basic form validation
      if (problemDescription.trim() === '') {
        alert('Please describe your problem before submitting.');
        return;
      }

      // Example: Log the data to the console (or send to an API endpoint)
      console.log('Problem Description:', problemDescription);

      // Simulate sending the data to the server (use an actual endpoint here)
      fetch('submit_problem_backend.php', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description: problemDescription }),
      })
        .then(response => response.json())
        .then(data => {
          console.log('Problem submitted:', data);
          alert('Thank you for your submission! We will get back to you soon.');
        })
        .catch(error => {
          console.error('Error submitting problem:', error);
          alert('Failed to submit the problem.');
        });
    });
  }
}

// Function to update the sidebar's position dynamically based on the header height
function updateSidebarPosition() {
  const header = document.querySelector('.header');
  const sidebar = document.getElementById('sidebar');
  
  if (header && sidebar) {
    const headerHeight = header.offsetHeight;  // Get the actual height of the header
    sidebar.style.top = `${headerHeight}px`;   // Set sidebar's top position based on header height
    sidebar.style.height = `calc(100vh - ${headerHeight}px)`;  // Set sidebar's height dynamically
  }
}

// Optional: Update content margin on window resize
window.addEventListener('resize', () => {
  updateContentMargin(); // Recalculate content margin on window resize
  updateSidebarPosition();
});
