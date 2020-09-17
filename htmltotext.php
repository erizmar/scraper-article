<?php
require "vendor/autoload.php";

// $stripped_path = 'download/stripped';
// if (!is_dir($stripped_path)) {
//     die;
// }

$stripped_path = 'download/html';
if (!is_dir($stripped_path)) {
    die;
}

$text_path = 'download/text';
if (!file_exists($text_path)) {
    mkdir($text_path, 0777, true);
}

$files = scandir($stripped_path);

foreach ($files as $val) {
    if ($val != "." && $val != "..") {
        $file = fopen($stripped_path.DIRECTORY_SEPARATOR.$val, 'r') or die("Unable to open file!");
        $html = fread($file,filesize($stripped_path.DIRECTORY_SEPARATOR.$val));

        // Method 1
        // $dom = new DOMDocument();
        // $dom->loadHTML($html);

        // $giant_string = "";

        // foreach($dom->getElementsByTagName('p') as $paragraph) {
        //     $giant_string .= $paragraph->textContent."\n";
        // }

        // $id = preg_replace('/-stripped.html/', '', $val);

        // $text_file = fopen($text_path.DIRECTORY_SEPARATOR."$id-plaintext.txt", "w");
        // fwrite($text_file, $giant_string);

        // Method 2
        $text = preg_replace('#<script(.*?)>(.*?)</script>#isu', '', $html);

        $options = array(
            'ignore_errors' => true,
            'drop_links' => true,
            );
        
        $text = \Soundasleep\Html2Text::convert($text, $options);

        $id = preg_replace('/.html/', '', $val);

        $text_file = fopen($text_path.DIRECTORY_SEPARATOR."$id-plaintext.txt", "w");
        fwrite($text_file, $text);

        echo "ID: $id plained<br>";

        fclose($file);
        fclose($text_file);
    }
}
?>