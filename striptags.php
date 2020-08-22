<?php
    include "connection.php";
    require_once "htmlpurifier/library/HTMLPurifier.auto.php";
    
    $counter = 1;

    $config = HTMLPurifier_Config::createDefault();
    $purifier = new HTMLPurifier($config);

    $html_path = 'download/html';
    if (!file_exists($html_path)) {
        mkdir($html_path);
    }

    $stripped_path = 'download/stripped';
    if (!file_exists($stripped_path)) {
        mkdir($stripped_path);
    }

    $sql = "SELECT id, tgturl FROM links";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            $doc = fopen($html_path.DIRECTORY_SEPARATOR."$counter.html", "r") or die("Unable to open file!");
            $sdoc = fopen($stripped_path.DIRECTORY_SEPARATOR."$counter-stripped.html", "w");
            
            $dhtml = fread($doc,filesize($html_path.DIRECTORY_SEPARATOR."$counter.html"));
            
            $chtml = $purifier->purify($dhtml);

            fwrite($sdoc, $chtml);

            fclose($doc);
            fclose($sdoc);

            echo "URL: ".$row["tgturl"]." stripped<br>";
            
            $counter++;
        }
    } else {
        echo "nothing to strip";
    }
    $conn->close();
?>