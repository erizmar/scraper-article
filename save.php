<?php
    include "connection.php";
    
    $url = $_POST['surl'];

    $sql = "INSERT INTO list (tgturl)
    VALUES ('$url')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();

    header("location:index.php")
?>