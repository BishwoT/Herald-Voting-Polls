<!-- favorites.php -->
<?php include('header.php'); ?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Favorites</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="favorites.css" /> <!-- Link to your CSS file -->
  </head>
  <body>
    <div class="favorites-page">
      <!-- Favorites Heading -->
      <section class="favorites-header">
        <h1>Favorites</h1>
      </section>

      <!-- Favorites List (Dynamically Generated) -->
      <section class="favorites-list">
        <!-- Dummy content for favorite polls. Replace this with backend code to fetch favorite polls -->
        <div class="favorite-item">
          <h2>Favorite Poll 1</h2>
          <p>Description or additional info about the poll.</p>
        </div>
        <div class="favorite-item">
          <h2>Favorite Poll 2</h2>
          <p>Description or additional info about the poll.</p>
        </div>
        <div class="favorite-item">
          <h2>Favorite Poll 3</h2>
          <p>Description or additional info about the poll.</p>
        </div>
        <div class="favorite-item">
          <h2>Favorite Poll 4</h2>
          <p>Description or additional info about the poll.</p>
        </div>
        <!-- End of dummy content -->

        <!-- Replace the above dummy content with actual backend code to fetch favorite polls -->
      </section>
    </div>
  </body>
</html>
