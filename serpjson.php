<?php
include "connection.php";

$path = 'download/json';
    if (!file_exists($path)) {
        mkdir($path, 0777, true);
    }

// count json file
$fi = new FilesystemIterator("download/json", FilesystemIterator::SKIP_DOTS);
$file_count = iterator_count($fi);

$counter = 1;

while ($counter <= $file_count) {
    echo "================================================$counter.json================================================<br>";
    
    $file = fopen($path.DIRECTORY_SEPARATOR."$counter-results.json", 'r') or die("Unable to open file!");
    $json = fread($file,filesize($path.DIRECTORY_SEPARATOR."$counter-results.json"));
    $result = json_decode($json);

    $x = 1;
    foreach ($result->organic_results as $val) {
        $link = $val->link;
        $link = preg_replace('/.html/', '', $link);
        
        echo "$x $link<br>";
        $x++;

        // search duplicate
        $sql = "SELECT id, tgturl FROM links WHERE tgturl='$link'";
        $sql_result = $conn->query($sql);
        
        if ($sql_result->num_rows > 0) {
            echo "Duplicate links!<br>";
            continue;
        } else {
            $sql = "INSERT INTO links (tgturl)
            VALUES ('$link')"; // from what json

            if ($conn->query($sql) === TRUE) {
                echo "New record created successfully<br>";
            } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
            }
        }
    }
    $x = 1;
    fclose($file);
    $counter++;
}

$conn->close();
?>