<?php include('header.php'); ?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Your Profile</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="profile.css" /> <!-- Link to your CSS file -->
  </head>
  <body>
    <div class="profile-page">
      <!-- Profile Heading -->
      <section class="profile-header">
        <h1>Your Profile</h1>
      </section>

      <!-- Profile Information -->
      <section class="profile-info">
        <div class="profile-picture">
          <img src="images/no-profile-picture-15257.png" alt="Profile Picture" id="profile-img" />
        </div>
        <div class="profile-details">
          <p><strong>Name:</strong> John Doe</p>
          <p><strong>Email:</strong> john.doe@example.com</p>
        </div>
      </section>

      <!-- Edit Profile Section -->
      <section class="edit-profile">
        <h2>Edit Profile</h2>
        <form action="update_profile.php" method="POST" enctype="multipart/form-data">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="John Doe" required />
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="john.doe@example.com" required />
          </div>
          <div class="form-group">
            <label for="profile-pic">Profile Picture:</label>
            <input type="file" id="profile-pic" name="profile-pic" accept="image/*" />
          </div>
          <button type="submit" class="submit-btn">Save Changes</button>
        </form>
      </section>
    </div>
  </body>
</html>
