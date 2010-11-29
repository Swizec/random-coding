
; problem 1
(defn my-last [list]
  (if (next list)
    (recur (next list))
    (first list)))

(println (my-last '(1 2 3 4 5)))