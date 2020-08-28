<?php

$path = 'download/testjson';
    if (!is_dir($path)) {
        die;
    }

$files = scandir($path);

$time = time();

// print_r($files);

foreach ($files as $val) {
    if ($val != "." && $val != "..") {
        echo "$val<br>";
    }
}
?>