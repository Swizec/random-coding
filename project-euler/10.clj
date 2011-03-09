
; The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

; Find the sum of all the primes below two million.

(defn any? [l]
  (reduce #(or %1 %2) l))

(defn prime? [n]
  (if (even? n) false
      (let [root (num (int (Math/sqrt n)))]
	(loop [i 3]
	  (if (> i root) true
	      (if (zero? (mod n i)) false
		  (recur (+ i 2))))))))

(defn answer []
  (loop [i 2 s 0]
    (println i s)
    (if (> i 2000000) s
	(recur (inc i) (if (prime? i) (+ s i) s)))))

;(println (prime? 19))

(println (answer))

;142913828920

;(println (answer))