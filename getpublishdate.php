<?php
include "connection.php";

$path = 'download/html';
    if (!is_dir($path)) {
        die;
    }

$files = scandir($path);

foreach ($files as $val) {
    if ($val != "." && $val != "..") {
        $file = fopen($path.DIRECTORY_SEPARATOR.$val, 'r') or die("Unable to open file!");
        $html = fread($file,filesize($path.DIRECTORY_SEPARATOR.$val));
        
        // get publication time
        $tags = getMetaTags($html);

        if (!isset($tags['article:published_time'])) {
            continue;
        }

        $pubdate = $tags['article:published_time'];
        echo "$pubdate<br>";

        // get id
        $id = preg_replace('/.html/', '', $val);

        // update db
        $sql = "UPDATE links SET pubdate='$pubdate' WHERE id=$id";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        fclose($file);
    }
}

function getMetaTags($str)
{
    $pattern = '
    ~<\s*meta\s

    # using lookahead to capture type to $1
        (?=[^>]*?
        \b(?:name|property|http-equiv)\s*=\s*
        (?|"\s*([^"]*?)\s*"|\'\s*([^\']*?)\s*\'|
        ([^"\'>]*?)(?=\s*/?\s*>|\s\w+\s*=))
    )

    # capture content to $2
    [^>]*?\bcontent\s*=\s*
        (?|"\s*([^"]*?)\s*"|\'\s*([^\']*?)\s*\'|
        ([^"\'>]*?)(?=\s*/?\s*>|\s\w+\s*=))
    [^>]*>

    ~ix';
    
    if(preg_match_all($pattern, $str, $out))
        return array_combine($out[1], $out[2]);
    return array();
}

$conn->close();
?>