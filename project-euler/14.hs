
-- which starting number under 1M produces the longest Collatz chain

import Data.Function.Memoize
import Data.List
import Data.Ord

collatz :: Integer -> [Integer]
collatz = memoize col where
  col 1 = []
  col n
    | odd n = 3*n+1:collatz(3*n+1)
    | even n = div n 2:collatz(div n 2)

collatz_len :: Integer -> Integer
collatz_len = memoize len where
  len 1 = 0
  len n
    | odd n = 1+len(3*n+1)
    | even n = 1+len(div n 2)


chains = [collatz x | x <- [1..]]
chains' from = map collatz [from..]
chains'' = map collatz_len [1..]

longest' (max_i, max_l) =
  let l = head $ dropWhile (\(i,l) -> l <= max_l) $ zip [max_i..] $ map length $ chains' max_i
  in l:longest' l

longest max =
  last $ sortBy (comparing snd) $ zip [1..] $ map length $ take max chains

--main = do
--  putStrLn $ show $ last $ sortBy (comparing snd) $ zip [1..] $ take 1000000 chains''
--  putStrLn $ show $ head $ reverse $ sortBy (comparing snd) $ zip [1..] $ take 1000000 chains''
--  putStrLn $ show $ head $ reverse $ takeWhile (\(i,l) -> i <= 1000000) $ longest' (1,1)
--  putStrLn $ show $ longest 1000000
