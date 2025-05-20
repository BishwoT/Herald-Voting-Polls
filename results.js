// Function to dynamically load the header
window.addEventListener('load', () => {
  // Load the header content from 'header.html'
  fetch('header.html')
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition();  // Adjust sidebar position after header is loaded
      updateContentMargin();    // Adjust content margin based on header height and sidebar width
    })
    .catch(err => console.error('Failed to load header:', err));

  // Dynamically load poll results
  loadResults();
});

// Function to dynamically load poll results
function loadResults() {
  const resultsList = document.getElementById('results-list');

  // Sample poll data (replace this with actual API call for results)
  const results = [
    { title: 'Poll 1', option1: 'Option 1: 70%', option2: 'Option 2: 30%' },
    { title: 'Poll 2', option1: 'Option 1: 50%', option2: 'Option 2: 50%' },
    { title: 'Poll 3', option1: 'Option 1: 85%', option2: 'Option 2: 15%' },
    { title: 'Poll 4', option1: 'Option 1: 60%', option2: 'Option 2: 40%' },
  ];

  // Loop through results data and create HTML dynamically
  results.forEach(result => {
    const resultItem = document.createElement('div');
    resultItem.classList.add('result-item');
    resultItem.innerHTML = `
      <h2>${result.title}</h2>
      <p>${result.option1}</p>
      <p>${result.option2}</p>
    `;
    resultsList.appendChild(resultItem);
  });
}

// Function to update the content margin based on header height and sidebar width
function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.results-page');
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