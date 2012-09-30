
import Data.List
import Data.HashMap as Map
import Data.Maybe

dictionary::[String]
dictionary = ["he", "she", "his", "hers"]

text::String
text = "ushers" -- expect output: she, he, hers

goto::Map (Int, Char) Int -> (Int, Char) -> Int
goto m (state, c) = fromMaybe (failure state) $ Map.lookup (state, c) m

output::Int -> [String]
output 2 = ["he"]
output 5 = ["she", "he"]
output 7 = ["his"]
output 9 = ["hers"]
output _ = []

failure::Int -> Int
failure 0 = 0
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

add_one::Int -> Map (Int, Char) Int -> [Char] -> Map (Int, Char) Int
add_one _  m [] = m
add_one state m (c:rest)
  | member key m = add_one (fromMaybe 0 $ Map.lookup key m) m rest
  | otherwise = add_one max (Map.insert key max m) rest
  where key = (state, c)
        max = (size m)+1

main = do
  let m = fst $ mapAccumL build_goto empty dictionary
  print $ ahocorasick m text 0
