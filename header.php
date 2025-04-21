<head>
   <meta charset="UTF-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <link rel="stylesheet" href="header.css" />  <!-- Link to the header CSS file -->
</head>

<header class="header">
   <div class="hamburger-menu" id="hamburger-menu" onclick="toggleMenu()">
      <span id="hamburger-icon" class="hamburger-icon">&#9776;</span> <!-- Hamburger Icon -->
   </div>
   
   <!-- Logo with link to Browse page -->
   <div class="logo-text">
         <img src="images/white_voting_logo.png" alt="Voting Icon" class="voting-icon" />
         <a href="browse.php"> <!-- Link the logo text to Browse page -->
         <span>Online Voting System</span>
      </a>
   </div>
   
   <nav class="sidebar" id="sidebar" class="active"> <!-- Sidebar is open by default -->
      <ul class="nav-menu">
         <li class="nav-item">
            <a href="browse.php"><img src="images/browse.png" alt="Browse" class="nav-icon" />
            <span>Browse</span></a>
         </li>
         <li class="nav-item">
            <a href="favorites.php"><img src="images/favorites.png" alt="Favorites" class="nav-icon" />
            <span>Favorites</span></a>
         </li>
         <li class="nav-item">
            <a href="mypoll.php"><img src="images/mypoll.png" alt="My Poll" class="nav-icon" />
            <span>My Poll</span></a>
         </li>
         <li class="nav-item">
            <a href="results.php"><img src="images/results.png" alt="Results" class="nav-icon" />
            <span>Results</span></a>
         </li>
         <li class="nav-item">
            <a href="settings.php"><img src="images/settings.png" alt="Settings" class="nav-icon" />
            <span>Settings</span></a>
         </li>
         <li class="nav-item">
            <a href="helpcenter.php"><img src="images/help.png" alt="Help Center" class="nav-icon" />
            <span>Help Center</span></a>
         </li>
      </ul>
   </nav>

   <!-- Profile with link to Profile page -->
   <div class="header-actions">
      <div class="search-container">
         <input type="text" class="search-input" placeholder="Search..." />
         <img src="images/search-icon-png-9982.png" alt="Search" class="search-icon" />
      </div>
      <div class="profile-container">
            <img src="images/no-profile-picture-15257.png" alt="Profile" class="profile-icon" />
            <a href="profile.php"> <!-- Link the profile section to Profile page -->
            <span>Profile</span>
         </a>
      </div>
   </div>
</header>

<script>
   // Function to toggle the sidebar visibility
   function toggleMenu() {
      const sidebar = document.getElementById('sidebar');
      sidebar.classList.toggle('active'); // This toggles the 'active' class
   }
</script>
