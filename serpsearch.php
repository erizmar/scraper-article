<?php
// composer autoload
require "vendor/autoload.php";

// php timeout
set_time_limit(0);

// max result for google
$google_max_result = 100;

$path = 'download/json';
    if (!file_exists($path)) {
        mkdir($path, 0777, true);
    }

// create the serpwow object, passing in our API key
$serpwow = new GoogleSearchResults("8796DFCC11F849F08C8D57E63CA3C83E");

// $short_tail = ['wisata hits surabaya', 'wisata instagramable surabaya', 'wisata terbaik surabaya', 'car free day surabaya'];

$short_tail = ['Car free day surabaya',
            'Cafe Kekinian di Surabaya',
            'Cafe Surabaya',
            'Explore Surabaya',
            'Kuliner Favorit di Surabaya',
            'Kuliner Surabaya',
            'Mall di Surabaya',
            'Rekomendasi Kuliner Surabaya',
            'Rekomendasi Tempat Makan di Surabaya',
            'Rekomendasi Wisata Surabaya',
            'Tempat Wisata Surabaya',
            'Wisata Alam di Surabaya',
            'Wisata Budaya di Surabaya',
            'Wisata di Surabaya',
            'Wisata Hits Surabaya',
            'Wisata Instagramable Surabaya',
            'Wisata Kuliner Surabaya',
            'Wisata Sby',
            'Wisata Surabaya',
            'Wisata Terbaik di Surabaya'
            ];


foreach ($short_tail as $val) {
    // set up the search parameters
    $params = [
        "q" => $val,
        "page" => 1,
        "num" => $google_max_result
    ];

    // retrieve the search results as JSON
    $result = $serpwow->json($params);

    echo "$val search success<br>";

    $time = time();
    $filename = "$val-$time.json";

    $file = fopen($path.DIRECTORY_SEPARATOR.$filename, 'w');
    fwrite($file, json_encode($result));
    fclose($file);
}
?>