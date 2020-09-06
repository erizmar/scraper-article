<?php
require_once "htmlpurifier/library/HTMLPurifier.auto.php";
// require_once "vendor/soundasleep/html2text/html2text.php";
require "vendor/autoload.php";

//Get the file
// $file = "download/stripped/222-stripped.html";
$file = "download/html/222.html";

$doc = fopen($file, "r") or die("Unable to open file!");
$html = fread($doc,filesize($file));
echo "success";

// $html = <<<HTML
// ...
// HTML;

// $dom = new DOMDocument();

// $dom->loadHTML($html);

// $script = $dom->getElementsByTagName('script');

// $remove = [];
// foreach($script as $item)
// {
//   $remove[] = $item;
// }

// foreach ($remove as $item)
// {
//   $item->parentNode->removeChild($item); 
// }

// $html = $dom->saveHTML();

// $config = HTMLPurifier_Config::createDefault();
// $purifier = new HTMLPurifier($config);

// $text = $purifier->purify($data);

// $text = preg_replace("/\n\s+/", " ", rtrim(html_entity_decode(strip_tags($text))));

// $text = strip_tags($html, "<p>");
$text = preg_replace('#<script(.*?)>(.*?)</script>#isu', '', $html);
// $text = preg_replace("/\n\s+/", " ", rtrim(html_entity_decode(strip_tags($text))));
// $text = preg_replace('/<script(.*?)>(.*?)<\/script>/isu', '', $html);

// echo "$text";
// $text = strip_tags($text);
// $giant_string = "";

// foreach($dom->getElementsByTagName('p') as $paragraph) {
//     // echo $paragraph->textContent."<br/><br/><br/>"; // for text only
//     // $string = $paragraph->textContent;
//     $giant_string .= $paragraph->textContent." ";
//   } 

$options = array(
    'ignore_errors' => true,
    'drop_links' => true,
  );

$text = \Soundasleep\Html2Text::convert($text, $options);
// $text = preg_replace("/\n\s+/", "\n", $text);

//Save as?
$filename = "test.txt";

//Save the file
$fh = fopen($filename, "w");
fwrite($fh, $text);
fclose($fh);
fclose($doc);

?>