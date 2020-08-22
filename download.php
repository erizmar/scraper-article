<?php
    include "connection.php";
    
    $counter = 1;
    
    $folder_path = 'download/html';
    if (!file_exists($folder_path)) {
        mkdir($folder_path);
    }

    $sql = "SELECT tgturl FROM links";
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
            $fh = fopen($folder_path.DIRECTORY_SEPARATOR.$filename, "w");
            fwrite($fh, $data);
            fclose($fh);

            $counter++;
        }
    } else {
        echo "0 results";
    }
    $conn->close();
?>