<?php include('header.php'); ?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Help Center</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="helpcenter.css" /> <!-- Link to your CSS file -->
  </head>
  <body>
    <div class="help-center-page">
      <!-- Help Center Heading -->
      <section class="help-center-header">
        <h1>Help Center</h1>
      </section>

      <!-- Problem Description Text Box -->
      <section class="help-center-form">
        <textarea class="problem-textbox" placeholder="Please describe your problem..." rows="6"></textarea>
        <button class="submit-btn">Submit</button>
      </section>
    </div>
  </body>
</html>
