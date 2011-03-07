
; The prime factors of 13195 are 5, 7, 13 and 29.

; What is the largest prime factor of the number 600851475143 ?

(defn any? [l]
  (reduce #(or %1 %2) l))

(defn prime? [n known]
  (loop [cnt (dec (count known)) acc []]
    (if (< cnt 0) (not (any? acc))
	(recur (dec cnt) (concat acc [(zero? (mod n (nth known cnt)))])))))
				       
	

(defn primes [n]
  (loop [cnt 3 p [2]]
    (if (>= (count p) n) p
      (recur (+ cnt 2) (if (prime? cnt p) (concat p [cnt]) p)))))

(println (primes 50))