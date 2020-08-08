<?php
    include "connection.php";
    
    $counter = 1;
    
    $folderPath = 'download';
    if (!file_exists($folderPath)) {
        mkdir($folderPath);
    }

    $sql = "SELECT tgturl FROM list";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            //Link to download file
            $url = $row["tgturl"];
            
            //Get the file
            $data = file_get_contents($url);
            echo "URL: ".$url." downloaded<br>";

            //Save as?
            $filename = "$counter.html";

            //Save the file
            $fh = fopen($folderPath.DIRECTORY_SEPARATOR.$filename, "w");
            fwrite($fh, $data);
            fclose($fh);

            $counter++;
        }
    } else {
        echo "0 results";
    }
    $conn->close();
?>