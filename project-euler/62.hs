
-- The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

-- Find the smallest cube for which exactly five permutations of its digits are cube.

import Data.List

cubes::(Num a) => a -> [(String, a)]
cubes 1 = [(show 1, 1)]
cubes n = (sort$show(n^3), n):(cubes $ n-1)


sortStrNum (s1, n1) (s2, n2)
  | length s1 == length s2 = compare s1 s2
  | otherwise = compare (length s1) (length s2)

permuted_cubes n =
  groupBy (\a b -> fst a == fst b) $ sortBy sortStrNum $ cubes n

fives n =
  filter (\xs -> length xs == 5) $ permuted_cubes n

threes n =
  filter (\xs -> length xs == 3) $ permuted_cubes n

comparing p x y = compare (p x) (p y)

smallest =
  head $ sortBy (comparing snd) $ head $ fives 100000
