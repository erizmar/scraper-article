<?php
    include "connection.php";

    $sql = "SELECT id, tgturl FROM list";
    $result = $conn->query($sql);

    echo "<a href='index.html'>Home</a> <br>";

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            echo "<tr> <td> ID: ".$row["id"]." URL: ".$row["tgturl"]."</td>";
            echo "<td> <a href='delete.php?id=".$row["id"]."'>Delete</a> <br> </td> </tr>";
        }
    } else {
        echo "0 results";
    }
    $conn->close();
?>