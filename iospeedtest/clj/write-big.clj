
;(require 'clojure.contrib.duck-streams)

;(clojure.contrib.duck-streams/spit "./big.txt", "test")

(ns tokenize
  (:import (java.io BufferedWriter FileWriter)))

(require 'clojure.contrib.duck-streams)

(defn write-a-lot [file-name]
  (with-open [wtr (BufferedWriter. (FileWriter. file-name))]
    (loop [i 0]
      (.write wtr i)
      (if (< i 1024)
	(recur (inc i))))))

(write-a-lot "./crap/big.txt")

(defn write-a-lot2 [file-name]
  (spit file-name
	       (loop [i 0 acc []]
		 (if (> i 10240000) acc
		     (recur (inc i) (cons i acc))))))

(println (write-a-lot2 "./crap/bla.txt"))
;(write-a-lot2 "./crap/bla.txt")