
reverse' = read . reverse . show

palindrome n = n == reverse' n

-- max denotes max recursion depth
lychrel n max
  | max <= 0 = True
  | palindrome$n+r = False
  | otherwise = lychrel (n+r) (max-1)
    where r = reverse' n

lychrels max =
  length [x | x <- [1..max], lychrel x 50]
