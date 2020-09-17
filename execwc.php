<?php
if (isset($_POST['update']))
{
    exec('python3 /var/www/html/pagedownload/getstopwords.py');
    exec('python3 /var/www/html/pagedownload/createstopwords.py');
    exec('python3 /var/www/html/pagedownload/generatewc.py');
}
?>