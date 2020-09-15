<?php
// composer autoload
require "vendor/autoload.php";

// max result for google
$google_max_result = 100;

$path = 'download/json';
    if (!file_exists($path)) {
        mkdir($path, 0777, true);
    }

// create the serpwow object, passing in our API key
$serpwow = new GoogleSearchResults("8796DFCC11F849F08C8D57E63CA3C83E");

// search something
$val = 'car free day surabaya';

// set up the search parameters
$params = [
    "q" => $val,
    "page" => 1,
    "num" => $google_max_result
];

// retrieve the search results as JSON
$result = $serpwow->json($params);

echo "$val success<br>";

$time = time();
$filename = "$val-$time.json";

$file = fopen($path.DIRECTORY_SEPARATOR.$filename, 'w');
fwrite($file, json_encode($result));
fclose($file);
?>