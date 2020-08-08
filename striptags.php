<?php
    include "connection.php";
    require_once "htmlpurifier/library/HTMLPurifier.auto.php";
    
    $counter = 1;

    $config = HTMLPurifier_Config::createDefault();
    $purifier = new HTMLPurifier($config);

    $folderPath = 'download';
    if (!file_exists($folderPath)) {
        mkdir($folderPath);
    }

    $sql = "SELECT id, tgturl FROM list";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            $doc = fopen($folderPath.DIRECTORY_SEPARATOR."$counter.html", "r") or die("Unable to open file!");
            $sdoc = fopen($folderPath.DIRECTORY_SEPARATOR."$counter-stripped.html", "w");
            
            $dhtml = fread($doc,filesize($folderPath.DIRECTORY_SEPARATOR."$counter.html"));
            
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