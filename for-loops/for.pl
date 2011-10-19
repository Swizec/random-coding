
$i = 5;

for (local $i=0; $i<2; $i++) {
  print "for:$i\n"; # prints 0, 1
}

print "after:$i\n"; # prints 2

$i = 5;

for ($j=0; $j<2; $j++) {
  local $i = $j+1;
  print "for2:$i\n"; # prints 1, 2
}

print "after:$i\n"; # prints 5
