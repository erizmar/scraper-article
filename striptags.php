<?php
require_once "htmlpurifier/library/HTMLPurifier.auto.php";

$config = HTMLPurifier_Config::createDefault();
$purifier = new HTMLPurifier($config);

$html_path = 'download/html';
if (!is_dir($html_path)) {
    die;
}

$stripped_path = 'download/stripped';
if (!file_exists($stripped_path)) {
    mkdir($stripped_path, 0777, true);
}

$files = scandir($html_path);

foreach ($files as $val) {
    if ($val != "." && $val != "..") {
        $file = fopen($html_path.DIRECTORY_SEPARATOR.$val, 'r') or die("Unable to open file!");
        $html = fread($file,filesize($html_path.DIRECTORY_SEPARATOR.$val));
        
        $clean_html = $purifier->purify($html);

        //id for filename
        $id = preg_replace('/.html/', '', $val);

        $stripped_html = fopen($stripped_path.DIRECTORY_SEPARATOR."$id-stripped.html", "w");
        fwrite($stripped_html, $clean_html);

        echo "ID: $id stripped<br>";

        fclose($file);
        fclose($stripped_html);
    }
}
?>