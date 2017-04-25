n = 0
with open("in.txt", "r") as f:
	for idx, line in enumerate(f):
		if idx == 0:
			n = int(line.strip())
		else:
			word1, word2 = line.split("|")
			w1 = list(word1)
			w2 = list(word2)
			ana = True
			for c in w1:
				if c not in w2:
					print(line.strip() + " = NOT AN ANAGRAM")	
					ana = False
					break
				w2.remove(c)
			if ana:
				print(line.strip() + " = ANAGRAM")
