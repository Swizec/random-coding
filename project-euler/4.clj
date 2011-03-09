;A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

;Find the largest palindrome made from the product of two 3-digit numbers.

(defn palindrome? [n]
  (let [s (Integer/toString n)]
    (= (seq s) (reverse s))))

(defn explore1 [left right]
  (loop [r right]
    (if (< r 100) 0)
    (if (palindrome? (* left r)) (* left r)
	(recur (dec r)))))

(defn explore [left]
  (loop [l left acc []]
    (if (< l 100) (apply max acc)
	(recur (dec l) (concat acc [(explore1 l left)])))))

(println (explore 999))