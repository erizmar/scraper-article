<?php
include "connection.php";

$sql = "SELECT id, word FROM stopwords";
$result = $conn->query($sql);

echo "<a href='index.php'>Home</a> <br>";

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr> <td> ID: ".$row["id"]." URL: ".$row["word"]."</td>";
        echo "<td> <a href='deletestopwords.php?id=".$row["id"]."'>Delete</a> <br> </td> </tr>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>