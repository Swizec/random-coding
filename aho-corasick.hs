
import Data.Set

dictionary::Set String
dictionary = fromList ["he", "she", "his", "hers"]

text::String
text = "ushers" -- expect output: she, he, hers

goto::Int -> Char -> Int
goto 0 'h' = 1
goto 0 's' = 3
goto 0 _ = 0
goto 1 'e' = 2
goto 1 'i' = 6
goto 2 'r' = 8
goto 3 'h' = 4
goto 4 'e' = 5
goto 6 's' = 7
goto 8 's' = 9
goto state char = goto (failure state) char

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

ahocorasick::[Char] -> Int -> [[String]]
ahocorasick [] state = [output(state)]
ahocorasick (c:rest) state =
  let next = goto state c
  in if output(state) /= []
     then output(state):(ahocorasick rest next)
     else ahocorasick rest next

main = do
  print $ ahocorasick text 0
