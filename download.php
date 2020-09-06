<?php
include "connection.php";

// set script run time unlimited
set_time_limit(0);

$path = 'download/html';
if (!file_exists($path)) {
    mkdir($path, 0777, true);
}

$sql = "SELECT id, tgturl FROM links";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        //Link to download file
        $url = $row["tgturl"];
        $id = $row["id"];
        
        //Get the file
        $data = file_get_contents($url);
        echo "ID: $id URL: $url downloaded<br>";

        //Save as?
        $filename = "$id.html";

        //Save the file
        $fh = fopen($path.DIRECTORY_SEPARATOR.$filename, "w");
        fwrite($fh, $data);
        fclose($fh);
    }
} else {
    echo "0 results";
}
$conn->close();
?>