
; The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

; Find the sum of all the primes below two million.

(defn any? [l]
  (reduce #(or %1 %2) l))

(defn prime? [n]
  (loop [i (int (Math/sqrt n))]
    (if (zero? (mod n i)) false
	(if (< i 3) true
	    (recur (dec (dec i)))))))

(defn answer []
  (loop [i 2 s 0]
    (println i s)
    (if (> i 2000000) s
	(recur (inc i) (if (prime? i) (+ s i) s)))))

;(println (prime? 19))

(println (answer))


;(println (answer))