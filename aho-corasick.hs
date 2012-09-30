
import Data.List as List
import Data.HashMap as Map
import Data.Maybe
import qualified Data.Set as Set

dictionary::[String]
dictionary = ["he", "she", "his", "hers"]

text::String
text = "ushers" -- expect output: she, he, hers

goto::Map (Int, Char) Int -> (Int, Char) -> Int
goto m (state, c)
  | member (state, c) m = fromMaybe 0 $ Map.lookup (state, c) m
  | otherwise = if state == 0 then 0 else goto m (failure state, c)

output::Int -> [String]
output 2 = ["he"]
output 5 = ["she", "he"]
output 7 = ["his"]
output 9 = ["hers"]
output _ = []

failure::Int -> Int
failure 1 = 0
failure 2 = 0
failure 3 = 0
failure 4 = 1
failure 5 = 2
failure 6 = 0
failure 7 = 3
failure 8 = 0
failure 9 = 3

ahocorasick::Map (Int, Char) Int -> [Char] -> Int -> [[String]]
ahocorasick _ [] state = [output(state)]
ahocorasick m (c:rest) state =
  let next = goto m (state, c)
  in if output(state) /= []
     then output(state):(ahocorasick m rest next)
     else ahocorasick m rest next


build_goto::Map (Int, Char) Int -> String -> (Map (Int, Char) Int, String)
build_goto m s = (add_one 0 m s, s)

-- adds one string to goto function
add_one::Int -> Map (Int, Char) Int -> [Char] -> Map (Int, Char) Int
add_one _  m [] = m
add_one state m (c:rest)
  | member key m = add_one (fromMaybe 0 $ Map.lookup key m) m rest
  | otherwise = add_one max (Map.insert key max m) rest
  where key = (state, c)
        max = (size m)+1

-- this doesn't fully work
build_output::Map (Int, Char) Int -> Map Int [String] -> String -> Map Int [String]
build_output m out s = insertWith (\a b -> a++b) state [s] out
  where state = fin m 0 s

-- returns the state in which an input string ends
fin::Map (Int, Char) Int -> Int -> [Char] -> Int
fin m state [] = state
fin m state (c:rest) = fin m next rest
  where next = fromMaybe 0 $ Map.lookup (state, c) m

-- returns the path to traverse a string
path::Map (Int, Char) Int -> Int -> [Char] -> [Int]
path m state [c] = [fin m state [c]]
path m state (c:rest) =
  let state' = (fin m state [c])
  in state':path m state' rest

--build_fail::Map (Int, Char) Int -> Map Int Int

-- tells us which nodes in the goto state machine are at which traversal depth
nodes_at_depths::Map (Int, Char) Int -> [[Int]]
nodes_at_depths m =
  List.map (\i ->
                  List.filter (>0) $
                  List.map (\l -> if i < length l then l!!i else -1)
                  paths)
           [0..(maximum $ List.map length paths)-1]
  where paths = List.map (path m 0) dictionary

build_fail::Map (Int, Char) Int -> [[Int]] -> Int -> Map Int Int
build_fail m ns 0 = fst $ mapAccumL (\f state ->
                                      (Map.insert state 0 f, state))
                          empty (ns!!0)
build_fail m ns d = fst $
                    mapAccumL (\f state ->
                                (Map.insert state (decide_fail state m lower) f, state))
                    lower (ns!!d)
  where lower = build_fail m ns (d-1)

decide_fail::Int -> Map (Int, Char) Int -> Map Int Int -> Int
decide_fail state m lower = findWithDefault 0 (s, c) m
  where (s', c) = key' state $ assocs m
        s = findWithDefault 0 s' lower


key'::Int -> [((Int, Char), Int)] -> (Int, Char)
key' _ [] = (-1, '_') -- this is ugly, Maybe would be better
key' state ((k, v):rest)
  | state == v = k
  | otherwise = key' state rest

main = do
  let m = fst $ mapAccumL build_goto empty dictionary
--  print build_fail m
--  print $ m
--  print $ key' 3 $ assocs m
  print $ build_fail m (nodes_at_depths m) $ (length $ nodes_at_depths m)-1
--  print $ ahocorasick m text 0
