
; problem set http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html

; problem 1
(defn my-last [list]
  (if (next list)
    (recur (next list))
    (first list)))

(println (my-last '(1 2 3 4 5)))
