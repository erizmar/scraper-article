<?php
    include "connection.php";

    $stop = $_POST['stopwords'];

    $stop_array = explode("\n", $stop);

    foreach ($stop_array as $key) {
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