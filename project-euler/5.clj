;2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

;What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


; this answer doesn't actually work, wolfram alpha was an easier solution :)
(defn answer []
  (loop [cur 3 acc 2]
    (if (>= cur 20) acc
	(recur (inc cur) (let [m (mod acc cur)]
			   (if (zero? m) acc
			       (* acc cur)))))))


(println (answer))