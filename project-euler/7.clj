;By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

;What is the 10001st prime number?


(defn any? [l]
  (reduce #(or %1 %2) l))

(defn prime? [n known]
  (loop [cnt (int (Math/sqrt (dec (count known)))) acc []]
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

(defn nth-prime [n]
  (nth (n-primes n) (dec n)))

(println (nth-prime 10001))