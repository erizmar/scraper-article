<?php
include "connection.php";

$val = $_POST['murl'];

$val_array = explode("\n", $val);

foreach ($val_array as $key) {
    $key = preg_replace('/\s+/', '', $key);

    $sql = "INSERT INTO links (tgturl)
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