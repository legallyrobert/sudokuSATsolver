#!/usr/bin/python3

import sys
import io
from utils import *

# Determines validity and parses solution
def parse(stream):
	L = ""
	sat = stream.readline()
	if sat == "SAT\n":
		L = stream.readline()
		return L
	return -1

def trim(line):
	A = list(map(int, line.split(' ')))
	#return [i for i in A if i > 0]
	return A

def convert(A):
	for x in range(9):
		for y in range(9):
			for z in range(9):
				if (A[81*x+9*y+z] >= 0):
					print(z+1, end='')
					break;
		print()

def main():
	SAT = parse(sys.stdin)
	if SAT == -1:
		print("Unsatisfiable")
	else:
		A = trim(SAT)
		convert(A)
		

if __name__ == "__main__":
	main()
