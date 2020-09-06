<?php
include "connection.php";

$val = $_POST['surl'];

$sql = "INSERT INTO links (tgturl)
VALUES ('$val')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

header("location:index.php")
?>