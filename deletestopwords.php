<?php
include "connection.php";

$id = $_GET['id'];

$sql = "DELETE FROM stopwords WHERE id=$id";
$result = $conn->query($sql);

$conn->close();

echo "deleted";

header("location:showstopwords.php");
?>