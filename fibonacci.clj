

(defn fibonacci [max]
  (loop [a 0 b 1 i 1]
    (println i b)
    (if (== b i) (println "YAY!" b))
    (if (<= i max)
      (recur b (+ a b) (inc i)))))

(fibonacci 20000)