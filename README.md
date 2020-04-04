# SAT Sudoku Solver
### CSC320 Spring 2020; Rob Wood V00888252 and Liam Franke V00887604

## Contents
Directory `Source` contains executable Python files `sud2sat.py` and `sat2sud.py`. File `util.py`, also in `Source`, was created for code readability.

Directory `Test` contains unsolved `.txt` sudoku puzzles curled from `projecteuler.net/project/resources/p096_sudoku.txt`. Inside 

## Usage:
### To Solve:
Both python3 programs read files from STDIN and write to STDOUT, e.g.

`./sud2sat.py < input.txt > output.cnf`

`minisat output.cnf solution.txt > stat.txt`

`./sat2sud.py < solution.txt > solved_puzzle.txt`

Note: `chmod +x` is needed to make file executable. Otherwise, `python3 ssat2sud.py|sud2sat.py` will suffice.

### To Test:
Test file `test.py` takes a solved `.txt` sudoku puzzle as input, i.e. `solved_puzzle.txt` as created above, e.g.

`./test.py solved_puzzle.txt`

Bash script `all_tests.sh` requires no input, though is dependant on this directory structure. Produced output is of the form "test-n failed/passed num_clauses cpu_time :)". Smiley face serves no informational purpose and is for emotional support only.
