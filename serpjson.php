<?php
include "connection.php";

$path = 'download/json';
    if (!is_dir($path)) {
        die;
    }

$files = scandir($path);

foreach ($files as $val) {
    if ($val != "." && $val != "..") {

        $file = fopen($path.DIRECTORY_SEPARATOR.$val, 'r') or die("Unable to open file!");
        $json = fread($file,filesize($path.DIRECTORY_SEPARATOR.$val));
        $result = json_decode($json);

        foreach ($result->organic_results as $key) {
            // removing any .html links
            $link = $key->link;
            $link = preg_replace('/.html/', '', $link);
            
            echo "$link<br>";

            // search duplicate
            $sql = "SELECT id, tgturl FROM links WHERE tgturl='$link'";
            $sql_result = $conn->query($sql);
            
            if ($sql_result->num_rows > 0) {
                echo "Duplicate link!<br>";
                continue;
            } else {
                $sql = "INSERT INTO links (tgturl, jsonfile)
                VALUES ('$link', '$val')";

                if ($conn->query($sql) === TRUE) {
                    echo "New record created successfully<br>";
                } else {
                    echo "Error: " . $sql . "<br>" . $conn->error;
                }
            }
        }

        fclose($file);
    }
}

$conn->close();
?>