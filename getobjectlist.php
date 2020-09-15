<?php
include 'connection.php';

$filename = 'tourism_object.csv';
$file = fopen($filename, "r");
    
while (($row = fgetcsv($file, 10000, ";")) !== FALSE) {
    // skip header
    if ($row[1] == 'Nama Tempat Wisata') {
        continue;
    }

    $name = "";
    if (isset($row[1])) {
        $name = $row[1];
    }
    $alias = "";
    if (isset($row[2])) {
        $alias = $row[2];
    }
    $category = "";
    if (isset($row[3])) {
        $category = $row[3];
    }
    
    if (strlen($alias) < 1) {
        $sql = "INSERT INTO tourism_object (name, category)
        values ('$name', '$category')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } else {
        $sql = "INSERT INTO tourism_object (name, alias, category)
            values ('$name', '$alias', '$category')";
    
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
}

$conn->close();
?>