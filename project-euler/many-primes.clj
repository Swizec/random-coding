
; The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

; Find the sum of all the primes below two million.

(defn prime? [n]
  (if (even? n) false
      (let [root (num (int (Math/sqrt n)))]
	(loop [i 3]
	  (if (> i root) true
	      (if (zero? (mod n i)) false
		  (recur (+ i 2))))))))

(defn primes [n]
  (loop [i 2 acc [2]]
    (if (> i n) acc
	(if (prime? i)
	  (recur (inc i) (cons i acc))
	  (recur (inc i) acc)))))

(println (reverse (primes 4000000)))
