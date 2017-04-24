n = 0
with open("in.txt", "r") as f:
	n = int(f.readline())
line = "# " * n
for i in range(n):
	print(line)	
