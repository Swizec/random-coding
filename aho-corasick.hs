
import Data.List as List
import Data.HashMap as Map
import Data.Maybe
import qualified Data.Set as Set

dictionary::[String]
dictionary = ["us", "he", "she", "his", "hers"]

text::String
text = "ushers" -- expect output: us, she, he, hers

-- TODO: passing all those maps around is ugly, everything should be put in a monad

goto::Map (Int, Char) Int -> Map Int Int -> (Int, Char) -> Int
goto m f (state, c)
  | member (state, c) m = fromMaybe 0 $ Map.lookup (state, c) m
  | otherwise = if state == 0 then 0 else goto m f (fromMaybe 0 $ Map.lookup state f, c)

output::Map Int [String] -> Int -> [String]
output out state = fromMaybe [] $ Map.lookup state out

ahocorasick::Map (Int, Char) Int -> Map Int Int -> Map Int [String] -> [Char] -> Int -> [[String]]
ahocorasick _ _ out [] state = [output out state]
ahocorasick m f out (c:rest) state =
  let next = goto m f (state, c)
  in if output out state /= []
     then (output out state):(ahocorasick m f out rest next)
     else ahocorasick m f out rest next


-- builds the goto function
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

-- builds the output function
build_output::Map (Int, Char) Int -> [String] -> Map Int [String]
build_output _ [] = empty
build_output m (s:rest) = Map.insert (fin m 0 s)
                          (List.filter (\x -> elem x dictionary) $ List.tails s) $
                          build_output m rest

-- returns the state in which an input string ends without using failures
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

-- tells us which nodes in the goto state machine are at which traversal depth
nodes_at_depths::Map (Int, Char) Int -> [[Int]]
nodes_at_depths m =
  List.map (\i ->
                  List.filter (>0) $
                  List.map (\l -> if i < length l then l!!i else -1)
                  paths)
           [0..(maximum $ List.map length paths)-1]
  where paths = List.map (path m 0) dictionary


-- builds the failure function
build_fail::Map (Int, Char) Int -> [[Int]] -> Int -> Map Int Int
build_fail m ns 0 = fst $ mapAccumL (\f state ->
                                      (Map.insert state 0 f, state))
                          empty (ns!!0)
build_fail m ns d = fst $
                    mapAccumL (\f state ->
                                (Map.insert state (decide_fail state m lower) f, state))
                    lower (ns!!d)
  where lower = build_fail m ns (d-1)

-- inner step of building the failure function
decide_fail::Int -> Map (Int, Char) Int -> Map Int Int -> Int
decide_fail state m lower = findWithDefault 0 (s, c) m
  where (s', c) = key' state $ assocs m
        s = findWithDefault 0 s' lower


-- gives us the key associated with a certain state (how to get there)
key'::Int -> [((Int, Char), Int)] -> (Int, Char)
key' _ [] = (-1, '_') -- this is ugly, Maybe would be better
key' state ((k, v):rest)
  | state == v = k
  | otherwise = key' state rest

main = do
  let m = fst $ mapAccumL build_goto empty dictionary
      f = build_fail m (nodes_at_depths m) $ (length $ nodes_at_depths m)-1
      out = build_output m dictionary

  print $ ahocorasick m f out text 0
