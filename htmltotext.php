<?php
    include "connection.php";
    
    $counter = 1;

    $stripped_path = 'download/stripped';
    if (!file_exists($stripped_path)) {
        mkdir($stripped_path);
    }

    $text_path = 'download/text';
    if (!file_exists($text_path)) {
        mkdir($text_path);
    }

    $sql = "SELECT id, tgturl FROM links";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            $doc = fopen($stripped_path.DIRECTORY_SEPARATOR."$counter-stripped.html", "r") or die("Unable to open file!");
            $sdoc = fopen($text_path.DIRECTORY_SEPARATOR."$counter-plaintext.txt", "w");
            
            $dhtml = fread($doc,filesize($stripped_path.DIRECTORY_SEPARATOR."$counter-stripped.html"));
            
            $pattern1 = "/<div>|<\/div>|<h2>|<\/h2>/";
            $regex1 = preg_replace($pattern1, "\r\n", $dhtml);
            
            $pattern2 = "/\s+/";
            $regex2 = preg_replace($pattern2, " ", $regex1);

            $chtml = strip_tags($regex2);

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