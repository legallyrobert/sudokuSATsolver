#!/bin/bash

for f in $(ls tests); do
    python3 ../Source/sud2sat.py < tests/$f > output.cnf
    time=$(minisat output.cnf solution.txt | grep -E "CPU | Number of clauses" | awk '{$1=$1};1' | tr -d "|\n")
    python3 ../Source/sat2sud.py < solution.txt > solved.txt

    val=$(python3 test.py solved.txt)

    if [[ $val == "true" ]]; then
        echo -e "$f passed!\t$time\t:)"
    else
        echo "$f failed"
    fi
done
