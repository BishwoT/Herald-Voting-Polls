<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="mypoll.css" />
  </head>
  <body>
    <?php include('header.php'); ?>  <!-- Include the header -->

    <div class="dashboard-layout">
      <nav class="sidebar">
        <!-- Sidebar content remains the same -->
      </nav>

      <main class="main-content">
        <section class="dashboard-header">
          <h1>My Polls</h1>
          <button class="create-poll-btn">Create Poll</button>
        </section>

        <section class="polls-section">
          <h2>Polls</h2>
          <?php
            // Example PHP code to fetch polls from the database
            $polls = []; // Replace with your actual database query

            if (!empty($polls)) {
              foreach ($polls as $poll) {
                echo "<div class='poll-item'>";
                echo "<div class='poll-info'>";
                echo "<h3>{$poll['title']}</h3>";
                echo "<time>{$poll['date']}</time>";
                echo "</div>";
                echo "<div class='poll-participants'>Participants: {$poll['participants']}</div>";
                echo "<div class='poll-deadline'>Deadline: {$poll['deadline']}</div>";
                echo "</div>";
              }
            } else {
              echo "<p>No polls created yet.</p>";
            }
          ?>
        </section>
      </main>
    </div>
  </body>
</html>
