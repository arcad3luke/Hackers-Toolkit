<?php

// Start the session
session_start();

// Check if the user is already logged in, redirect to home page
if(isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true){
    header('location: home.php');
    exit;
}

// Check if the login form was submitted
if($_SERVER['REQUEST_METHOD'] == 'POST'){
    // Get the username and password from the form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Check if the username and password are correct
    if($username == 'myusername' && $password == 'mypassword'){
        // Login successful, set session variables and redirect to home page
        $_SESSION['loggedin'] = true;
        $_SESSION['username'] = $username;

        // Get the user's hostname/IP address and store it in a session variable
        $ipaddress = $_SERVER['REMOTE_ADDR'];
        $_SESSION['ipaddress'] = $ipaddress;

        header('location: home.php');
    }else{
        // Login failed, show error message
        $error = 'Invalid username or password.';
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
</head>
<body>
    <h2>Login Form</h2>
    <?php
    // Show error message if login failed
    if(isset($error)){
        echo '<p>' . $error . '</p>';
    }
    ?>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username" required><br><br>
        <label>Password:</label>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
