import sys
import io
from utils import *

# Parses stdin into one long string
def parse(stream):
	L = ""
	lines = stream.readlines()
	for line in lines:
		L += ''.join(line.split())
	return L

# Converts long string into 9x9 sudoku table
def convert(line):
	table = [[0 for x in range(9)] for x in range(9)]
	for i in range(9):
		for j in range(9):
			table[i][j] = int(line[ i*9 + j ])
	return table

def write(table):
	stream = io.StringIO()

	count = 0
	count += clause_1(stream, table)
	count += clause_2(stream)
	count += clause_3(stream) # very questionable...
	count += clause_4(stream) # also very questionable...
	count += clause_5(stream) # very questionable. Won't count properly.

	sys.stdout.write("p cnf 729 %d\n" % count)
	sys.stdout.write(stream.getvalue())

	stream.close()

def main():
	line = parse(sys.stdin)	
	table = convert(line)
	write(table)

if __name__ == "__main__":
	main()
