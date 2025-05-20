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

// Recalculate sidebar position on window resize
window.addEventListener('resize', debounce(() => {
  updateSidebarPosition();
}, 100));

// Call updateSidebarPosition and updateContentMargin on page load to adjust them correctly
window.addEventListener('load', () => {
  updateSidebarPosition();  // Adjust sidebar position based on header height
  updateContentMargin();    // Adjust content margin based on header height
});