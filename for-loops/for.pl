
$i = 5;

for (local $i=0; $i<2; $i++) {
  print "for:$i\n";
}

print "after:$i\n";

$i = 5;

for ($j=0; $j<2; $j++) {
  local $i = $j+1;
  print "for2:$i\n";
}

print "after:$i\n";
