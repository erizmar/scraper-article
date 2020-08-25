<?php
// composer autoload
require "vendor/autoload.php";

$google_max_result = 100;

// create the serpwow object, passing in our API key
$serpwow = new GoogleSearchResults("8796DFCC11F849F08C8D57E63CA3C83E");

    // set up the search parameters
    $params = [
        "q" => "wisata kekinian surabaya",
        "page" => 1,
        "num" => $google_max_result
    ];

    // retrieve the search results as JSON
    $result = $serpwow->json($params);

    // pretty-print the JSON result
    // print_r($result);

    echo "$val success<br>";

    $filename = "$counter-results.json";

    $file = fopen($path.DIRECTORY_SEPARATOR.$filename, 'w');
    fwrite($file, json_encode($result));
    fclose($file);
?>