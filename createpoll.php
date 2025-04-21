<?php include('header.php'); ?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Create Poll</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="createpoll.css" /> <!-- Link to your CSS file -->
  </head>
  <body>
    <div class="create-poll-page">
      <!-- Create Poll Heading -->
      <section class="create-poll-header">
        <h1>Create Poll</h1>
        <p>Complete the below fields to create your poll</p>
      </section>

      <!-- Create Poll Form -->
      <section class="create-poll-form">
        <form action="create_poll_backend.php" method="POST">
          <!-- Poll Title -->
          <div class="form-group">
            <label for="poll-title">Title</label>
            <input type="text" id="poll-title" name="poll-title" placeholder="Enter poll title" required />
          </div>

          <!-- Answer Options -->
          <div class="form-group">
            <label>Answer options</label>
            <div class="answer-options">
              <input type="text" name="option[]" placeholder="Option A" required />
              <input type="text" name="option[]" placeholder="Option B" required />
            </div>
            <button type="button" id="add-option" class="add-option-btn">+ Add Option</button>
          </div>

          <!-- Privacy -->
          <div class="form-group">
            <label>Category</label>
            <div class="privacy-options">
              <input type="radio" id="private" name="privacy" value="private" required />
              <label for="private">Private</label>
              <input type="radio" id="public" name="privacy" value="public" />
              <label for="public">Public</label>
            </div>
          </div>

          <!-- Submit Buttons -->
          <div class="form-actions">
            <button type="submit" class="submit-btn">Create Poll</button>
            <button type="button" class="save-btn">Save as draft</button>
          </div>
        </form>
      </section>
    </div>
  </body>
</html>
