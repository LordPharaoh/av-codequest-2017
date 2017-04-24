n = 0
with open("in.txt", "r") as f:
	for idx, l in enumerate(f):
		if idx == 0:
			n = int(l)
		elif idx < n + 1:
			num = int(l)
			for i in range(num):
				line = "# " * num
				print(line)	
