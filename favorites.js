// Function to dynamically load the header
window.addEventListener('load', () => {
  fetch('header.html') // Load the header content from 'header.html'
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition(); // Adjust sidebar position after header is loaded
      updateContentMargin();    // Adjust content margin based on header height and sidebar width
    })
    .catch(err => console.error('Failed to load header:', err));    

  // Dynamically load favorite polls
  loadFavorites();
});

// Function to dynamically load favorite polls
function loadFavorites() {
  const favoritesList = document.getElementById('favorites-list');

  // Sample favorite polls (replace this with backend API call)
  const favoritePolls = [
    { title: 'Favorite Poll 1', description: 'Description or additional info about the poll.' },
    { title: 'Favorite Poll 2', description: 'Description or additional info about the poll.' },
    { title: 'Favorite Poll 3', description: 'Description or additional info about the poll.' },
    { title: 'Favorite Poll 4', description: 'Description or additional info about the poll.' },
  ];

  // Loop through favorite polls and create HTML dynamically
  favoritePolls.forEach(poll => {
    const pollItem = document.createElement('div');
    pollItem.classList.add('favorite-item');

    pollItem.innerHTML = `
      <h2>${poll.title}</h2>
      <p>${poll.description}</p>
    `;

    favoritesList.appendChild(pollItem);
  });
}

function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.favorites-page');
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
