
(require 'primes)

(def smallest-div
     (memoize (fn [n]
		(if (<= n 1) nil
		    (let [sqrt (Math/sqrt n)]
		      (loop [i 0]
			(let [p (nth first-1k-primes i)]
			  (if (> i sqrt) p
			      (if (zero? (rem n p)) p
				  (recur (inc i)))))))))))

(defn factorize [n]
  (loop [acc [] num n]
    (if (<= num 1) acc
	(let [f (smallest-div num)]
	  (recur (concat acc [f]) (/ num f))))))

;(println (factorize 28))

(defn divisors [n]
  (let [facts (factorize n)]
    (loop [n 1
	   last 0
	   f facts
	   acc 1]
      (let [f1 (first f)]
	(if (empty? f) acc
	    (if (or (= f1 last) (= nil f1))
	      (recur (inc n) f1 (next f) acc)
	      (recur 1 f1 (next f) (* acc (inc n)))))))))
  
;(println (divisors 28))

;(memoize divisors)

(defn many-divisors [max]
  (loop [i 2]
    (factorize i)
    (if (> i max) true
	(recur (inc i)))))

(many-divisors 2000000)