
; The prime factors of 13195 are 5, 7, 13 and 29.

; What is the largest prime factor of the number 600851475143 ?

(defn any? [l]
  (reduce #(or %1 %2) l))

(defn prime? [n known]
  (loop [cnt (dec (count known)) acc []]
    (if (< cnt 0) (not (any? acc))
	(recur (dec cnt) (concat acc [(zero? (mod n (nth known cnt)))])))))

(defn next-prime [primes]
  (let [n (inc (count primes))]
    (let [lk (if (even? (inc (last primes))) (+ 2 (last primes)) (inc (last primes)))]
      (loop [cnt lk p primes]
	(if (>= (count p) n) (last p)
	    (recur (+ cnt 2) (if (prime? cnt p) (concat p [cnt]) p)))))))

(memoize next-prime)

(defn n-primes [n]
  (loop [cnt 1 p [2]]
    (if (>= cnt n) p
	(recur (inc cnt) (concat p [(next-prime p)])))))

(defn factor [n factors primes]
  (if (== n 1) factors
      (loop [p primes]
	(if (== 0 (mod n (last p))) (factor
				     (/ n (last p))
				     (concat [(last p)] factors)
				     p)
	    (recur (concat p [(next-prime p)]))))))

(println (factor 600851475143 [] (n-primes 1)))