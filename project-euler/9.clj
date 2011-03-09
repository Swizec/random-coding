;A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

;a2 + b2 = c2
;For example, 32 + 42 = 9 + 16 = 25 = 52.

;There exists exactly one Pythagorean triplet for which a + b + c = 1000.
;Find the product abc.


(defn pythagorean? [a b c]
  (= (+ (Math/pow a 2) (Math/pow b 2)) (Math/pow c 2)))

(defn on-plane? [a b c d]
  (= (+ a b c) d))

(defn explore [d]
  (loop [a 1 acc-a []]
    (if (> a d) acc-a
	(recur (inc a) (loop [b a acc-b acc-a]
			 (if (> b d) acc-b
			     (recur (inc b) (loop [c b acc-c acc-b]
					      (if (> c d) acc-c
						  (recur (inc c) (if (and (pythagorean? a b c)
									  (on-plane? a b c d))
								   (concat [a b c])
								   acc-c)))))))))))
(defn answer []
  (apply * (explore 1000)))

(println (answer))