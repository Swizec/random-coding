
;If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

;Find the sum of all the multiples of 3 or 5 below 1000.

(defn nums [max n]
  (loop [cnt (+ n n) acc [n]]
    (if (>= cnt max) acc
	(recur (+ cnt n) (concat acc [cnt])))))

(defn answer [max]
  (println (reduce + (set (concat (nums max 3) (nums max 5))))))

(answer 1000)
