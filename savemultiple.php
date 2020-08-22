<?php
    include "connection.php";

    $url = $_POST['murl'];

    $url_array = explode("\n", $url);

    foreach ($url_array as $key) {
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