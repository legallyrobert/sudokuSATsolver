# convert base 10 to base 9
def swap_bases(i, j, k):
	return 81*(i-1)+9*(j-1)+(k-1)+1

# clause 1: single-variable clause
def clause_1(buf, table):
	c = 0
	for i in range(1, 10):
		for j in range(1, 10):
			if table[i-1][j-1] is not 0:
				buf.write(str(swap_bases(i, j, int(table[i-1][j-1]))) + ' ' + '0\n')
				c+=1
	return c

# clause 2: every cell contains at least one number
def clause_2(buf):
	c = 0
	for i in range(1, 10):
		for j in range(1, 10):
			for k in range(1, 10):
				buf.write(str(swap_bases(i, j, k)) + ' ')
			buf.write("0\n")
			c+=1
	return c

# clause 3: each number appears at most once in every row
def clause_3(buf):
	c = 0
	for y in range(1, 10):
		for z in range(1, 10):
			for x in range(1, 9):
				for i in range(x+1, 10):
					buf.write("-"+str(swap_bases(x, y, z))+" "+"-"+str(swap_bases(i, y, z))+" "+"0\n")
					c+=1
	return c

# clause 4: each number appears at most once in every column
def clause_4(buf):
	c = 0
	for x in range(1, 10):
		for z in range(1, 10):
			for y in range(1, 9):
				for i in range(y+1, 10):
					buf.write("-"+str(swap_bases(x, y, z))+" "+"-"+str(swap_bases(x, i, z))+" "+"0\n")
					c+=1
	return c

# clause 5: each number appears at most once in every 3x3 subgrid
def clause_5(buf):
	count = 0
	for z in range(1, 10):
		for x_grid in range(0, 3):
			for y_grid in range(0, 3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range(y+1, 4):
							a = x_grid * 3 + x
							b = y_grid * 3 + y
							c = y_grid * 3 + k

							buf.write("-"+str(swap_bases(a, b, z))+" "+"-"+str(swap_bases(a, c, z))+" "+"0\n")
							count += 1
						for k in range(x+1, 4):
							for l in range(1, 4):
								a = x_grid * 3 + x
								b = y_grid * 3 + y
								c = x_grid * 3 + k
								d = y_grid * 3 + l
								buf.write("-"+str(swap_bases(a, b, z))+" "+"-"+str(swap_bases(c, d, z))+" "+"0\n")
								count += 1
	return count
