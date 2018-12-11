numRows = 2
l = []
temp = []
summation = 0
if numRows == 0:
	print([])
for i in range(0,numRows-1):
	for j in range(i):
		summation = l[i][j] + l[i][j+1]
		print(summation)
		temp.append(summation)
	temp.insert(0,1)
	temp.insert(len(temp),1)
	print(temp)
	l.append(temp)
	temp = []
print(l)

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]