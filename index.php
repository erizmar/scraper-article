<!DOCTYPE html>
<html>
    <head>
        <title>Save HTML</title>
    </head>
    <body>
        <h1>HTML Downloader</h1>
        <a href="show.php">Show All</a> <br><br>
        <a href="serpjson.php">Add From JSON</a> <br><br>
        <a href="download.php">Download All</a> <br><br>
        <a href="getpublishdate.php">Get Date</a> <br><br>
        <a href="striptags.php">Strip All</a> <br><br>
        <a href="htmltotext.php">Plain All</a> <br><br>
        <!-- <fieldset>
            <form method="post" action="save.php">
                <label for="surl">URL: </label>
                <input type="text" id="surl" name="surl" required>
                <button type="submit" value="save">Save</button>
            </form>
        </fieldset> <br>
        <fieldset>
            <form method="post" action="savemultiple.php">
                <label for="murl">URL: </label>
                <textarea id="murl" name="murl" rows="4" cols="50" required></textarea>
                <button type="submit" value="save">Save</button>
            </form>
        </fieldset> <br> -->
        <fieldset>
            <form method="post" action="stopwords.php">
                <label for="stopwords">Stopwords: </label>
                <textarea id="stopwords" name="stopwords" rows="4" cols="50" required></textarea>
                <button type="submit" value="save">Save</button>
            </form>
        </fieldset> <br>
    </body>
</html>