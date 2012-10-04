
{-# LANGUAGE ImplicitParams #-}

import Data.List as List
import Data.HashMap as Map
import Data.Maybe
import qualified Data.Set as Set

dictionary::[String]
dictionary = ["he", "she", "his", "hers"]

text::String
text = "ushers" -- expect output: she, he, hers

type Goto = Map (Int, Char) Int
type Failure = Map Int Int
type Output = Map Int [String]

-- the main function of the algorithm
ahocorasick::(?m::Goto, ?f::Failure, ?out::Output) =>
             String -> [(Int, [String])]
ahocorasick text = ahocorasick' text 0 0

-- real implementation
ahocorasick'::(?m::Goto, ?f::Failure, ?out::Output) =>
             [Char] -> Int -> Int -> [(Int, [String])]
ahocorasick' [] state pos = [(pos, output state)]
ahocorasick' (c:rest) state pos =
  if output state /= []
     then (pos, output state):(ahocorasick' rest next (pos+1))
     else ahocorasick' rest next (pos+1)
  where next = goto (state, c)

-- helper function for the parser state machine
goto::(?m::Goto, ?f::Failure) => (Int, Char) -> Int
goto (state, c)
  | member (state, c) ?m = fromMaybe 0 $ Map.lookup (state, c) ?m
  | otherwise = if state == 0 then 0
                else goto (fromMaybe 0 $ Map.lookup state ?f, c)

-- helper function to call the output "function"
output::(?out::Output) => Int -> [String]
output state = fromMaybe [] $ Map.lookup state ?out


-- builds the goto function
build_goto::Goto -> String -> (Goto, String)
build_goto m s = (add_one 0 m s, s)

-- adds one string to goto function
add_one::Int -> Goto -> [Char] -> Goto
add_one _  m [] = m
add_one state m (c:rest)
  | member key m = add_one (fromMaybe 0 $ Map.lookup key m) m rest
  | otherwise = add_one max (Map.insert key max m) rest
  where key = (state, c)
        max = (size m)+1

-- builds the output function
build_output::(?m::Goto) => [String] -> Output
build_output [] = empty
build_output (s:rest) = Map.insert (fin 0 s)
                          (List.filter (\x -> elem x dictionary) $ List.tails s) $
                          build_output rest

-- returns the state in which an input string ends without using failures
fin::(?m::Goto) => Int -> [Char] -> Int
fin state [] = state
fin state (c:rest) = fin next rest
  where next = fromMaybe 0 $ Map.lookup (state, c) ?m

-- returns the path to traverse a string
path::(?m::Goto) => Int -> [Char] -> [Int]
path state [c] = [fin state [c]]
path state (c:rest) =
  let state' = (fin state [c])
  in state':path state' rest

-- tells us which nodes in the goto state machine are at which traversal depth
nodes_at_depths::(?m::Goto) => [[Int]]
nodes_at_depths =
  List.map (\i ->
                  List.filter (>0) $
                  List.map (\l -> if i < length l then l!!i else -1)
                  paths)
           [0..(maximum $ List.map length paths)-1]
  where paths = List.map (path 0) dictionary


-- builds the failure function
build_fail::(?m::Goto) => [[Int]] -> Int -> Failure
build_fail nodes 0 = fst $
                  mapAccumL (\f state ->
                              (Map.insert state 0 f, state))
                  empty (nodes!!0)
build_fail nodes d = fst $
                  mapAccumL (\f state ->
                              (Map.insert state (decide_fail state lower) f, state))
                  lower (nodes!!d)
  where lower = build_fail nodes (d-1)

-- inner step of building the failure function
decide_fail::(?m::Goto) => Int -> Failure -> Int
decide_fail state lower = findWithDefault 0 (s, c) ?m
  where (s', c) = key' state $ assocs ?m
        s = findWithDefault 0 s' lower


-- gives us the key associated with a certain state (how to get there)
key'::Int -> [((Int, Char), Int)] -> (Int, Char)
key' _ [] = (-1, '_') -- this is ugly, Maybe would be better
key' state ((k, v):rest)
  | state == v = k
  | otherwise = key' state rest

main = do
  let ?m = fst $ mapAccumL build_goto empty dictionary
  let ?f = build_fail nodes_at_depths $ (length $ nodes_at_depths)-1
      ?out = build_output dictionary

  print $ ahocorasick text
