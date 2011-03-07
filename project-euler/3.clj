
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
    (println p)
    (if (>= (count p) n) p
	(recur (+ cnt 2) (if (prime? cnt p) (concat p [cnt]) p)))))

(defn next-prime [primes]
  (let [n (inc (count primes))]
    (loop [cnt (inc (last primes)) p primes]
      (if (>= (count p) n) (last p)
	  (recur (+ cnt 2) (if (prime? cnt p) (concat p [cnt]) p))))))

(defn factor [n]
  (loop [cnt 1 p (primes 1)]
  (if (== n (reduce * p)) p
      (recur (inc cnt) (concat p (next-prime p))))))

					;(println (factor 13195))

(println (next-prime [2]))