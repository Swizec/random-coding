<?php

$i = 5;

for ($i=0; $i<2; $i++) {
  echo "for:$i\n"; // prints 0, 1
}

echo "after:$i\n"; // prints 2

$i = 5;

for ($j=0; $j<2; $j++) {
  $i = $j+1;
  echo "for:$i\n"; // prints 1, 2
}

echo "after:$i\n"; // prints 2

?>