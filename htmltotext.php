<?php
    include "connection.php";
    
    $counter = 1;

    $stripped_path = 'download/stripped';
    if (!file_exists($stripped_path)) {
        mkdir($stripped_path, 0777, true);
    }

    $text_path = 'download/text';
    if (!file_exists($text_path)) {
        mkdir($text_path, 0777, true);
    }

    $sql = "SELECT id, tgturl FROM links";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            $doc = fopen($stripped_path.DIRECTORY_SEPARATOR."$counter-stripped.html", "r") or die("Unable to open file!");
            $sdoc = fopen($text_path.DIRECTORY_SEPARATOR."$counter-plaintext.txt", "w");
            
            $dhtml = fread($doc,filesize($stripped_path.DIRECTORY_SEPARATOR."$counter-stripped.html"));
            
            $regex = preg_replace("/<div>|<\/div>|<h2>|<\/h2>/", "\r\n", $dhtml);
            $regex = preg_replace("/\s+/", " ", $regex);

            $chtml = strip_tags($regex);

            fwrite($sdoc, $chtml);

            fclose($doc);
            fclose($sdoc);

            echo "URL: ".$row["tgturl"]." plained<br>";
            
            $counter++;
        }
    } else {
        echo "nothing to convert";
    }
    $conn->close();
?>