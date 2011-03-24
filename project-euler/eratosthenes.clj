
; implementation of eratosthenes sieve to see how fast I can make finding primes

(defn count-by [d n]
  (loop [i d acc []]
    (if (> i n) (next acc)
	(recur (+ i d) (concat acc [i])))))

(defn eratosthenes [n]
  (loop [acc (count-by 1 n) i 0]
    (let [p (nth acc i)]
      (if (> (* p p) n)
	acc
	(let [sieve (set (count-by p n))]
	  (recur (remove #(contains? sieve %1) acc) (inc i)))))))
    
(println (eratosthenes 10000))