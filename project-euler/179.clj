
(def smallest-div
     (memoize (fn [n]
		(loop [i 2]
		  (if (zero? (rem n i)) i
		      (recur (inc i)))))))

(def factorize 
     (memoize (fn [n]
	     (if (<= n 1) nil
		 (let [d (smallest-div n)]
		   (concat [d] (factorize (/ n d))))))))

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
    (divisors i)
    (if (> i max) true
	(recur (inc i)))))

(many-divisors 1000)