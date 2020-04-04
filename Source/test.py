import sys
import io
from utils import *

def check_cols(cols):
    for line in cols:
        sum = 0
        for i in line:
            sum = sum + int(i)
        if sum is not 45:
            return False
            break
    return True

def check_rows(rows):
    for line in rows:
        sum = 0
        for i in line:
            sum = sum + int(i)
        if sum is not 45:
            return False
            break
    return True

def main():
    with open(sys.argv[1], 'r') as f:
        L = [line.strip() for line in f]
    rows = L
    cols = zip(*L)
    if check_rows(rows) and check_cols(cols):
        print("true")
    
if __name__ == "__main__":
    main()
