<?php
include "connection.php";

$val = $_POST['stopwords'];

$val_array = explode("\n", $val);

foreach ($val_array as $key) {
    $key = preg_replace('/\s+/', '', $key);

    $sql = "INSERT INTO stopwords (word)
    VALUES ('$key')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();

header("location:index.php")
?>