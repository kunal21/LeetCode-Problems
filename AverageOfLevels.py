class Node(object):
	def __init__(self,val):
		self.val = val
		self.left =  None
		self.right = None

def Average(root):
	if root is None:
		return 
	queue = []
	avg = []
	temp = []
	summation = 0
	counter = 0
	queue.append(root)
	while(len(queue) > 0):
		while(len(queue)>0):
			node = queue.pop(0)
			print(node)
			counter+=1
			summation = summation + node.val
			print(summation)
			if(node.left):	
				temp.append(node.left)
			if(node.right):
				temp.append(node.right)
		avg.append(float(summation/counter))
		queue = temp
		print("queue = ",queue)
		temp = []
		counter = 0
		summation = 0
	print(avg)
	
root = Node(3)				
root.left = Node(9)
root.right = Node(20)
# root.left.left = Node(0)
# root.left.right = Node(2)
root.right.left = Node(15)
root.right.right = Node(7)
# root.left.left.left = Node(2)
Average(root)

