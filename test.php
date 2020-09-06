<?php
$prefix = ["wisata hits", "wisata instagramable", "wisata terbaik"];
$suffix = ["surabaya", "terbaik"];

foreach ($prefix as $val1) {
    foreach ($suffix as $val2) {
        $string = "$val1 $val2";
        echo $string;
        echo "<br>";
    }
}
?>