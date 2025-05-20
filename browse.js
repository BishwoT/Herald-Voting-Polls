// Function to load the header dynamically into the page
window.addEventListener('load', () => {
  fetch('header.html') // Load the header content from 'header.html'
    .then(response => response.text())
    .then(html => {
      document.getElementById('header-container').innerHTML = html;
      updateSidebarPosition(); // Adjust sidebar position after header is loaded
      updateContentMargin(); // Adjust content margin based on header height and sidebar width
    })
    .catch(err => console.error('Failed to load header:', err));    
});

function updateContentMargin() {
  const header = document.querySelector('.header');
  const content = document.querySelector('.browse-page');
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

// Debounce function to limit the number of times the resize handler is called
function debounce(func, wait) {
  let timeout;
  return function () {
    clearTimeout(timeout);
    timeout = setTimeout(func, wait);
  };
}

// Recalculate sidebar position and content margin on window resize
window.addEventListener('resize', debounce(() => {
  updateSidebarPosition(); // Recalculate sidebar position
  updateContentMargin();   // Recalculate content margin
}, 100));
