n = 0
with open("in.txt", "r") as f:
	for idx, l in enumerate(f):
		if idx == 0:
			n = int(l)
		elif idx < n + 1:
			nums = l.split(", ")
			is_triangle = True
			for i in range(len(nums)):
				nums[i] = int(nums[i])
			for i in nums:
				s = sum(nums) - i
				if s < i:
					is_triangle = False
					print("Not a Triangle")
					break
			if is_triangle:
				if nums[0] != nums[1] and\
				   nums[1] != nums[2] and\
				   nums[2] != nums[0]:
					print("Scalene")
				elif nums[1] == nums[0] and\
				     nums[0] == nums[2] and\
				     nums[2] == nums[1]:
					print("Equilateral")
				else:
					print("Isoceles")	
