;The sum of the squares of the first ten natural numbers is,

;12 + 22 + ... + 102 = 385
;The square of the sum of the first ten natural numbers is,

;(1 + 2 + ... + 10)2 = 552 = 3025
;Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

;Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

(defn gen [n]
  (loop [i 1 acc []]
    (if (> i n) acc
	(recur (inc i) (concat acc [i])))))

(memoize gen)

(defn answer []
  (Math/abs (- (apply + (map #(Math/pow %1 2) (gen 100)))
	       (Math/pow (apply + (gen 100)) 2))))

(println (answer))
