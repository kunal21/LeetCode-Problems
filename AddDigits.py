def AddDigits(num):
	summation = 0
	if len(str(num)) == 1:
		return num
	else:
		for i in (str(num)):
			summation = summation + int(i)
			# print(summation)
		return AddDigits(summation)

print(AddDigits(0))