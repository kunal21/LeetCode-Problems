class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None

class Palindrome(object):
	def __init__(self):
		self.head = None

	def insertnode(self,newnode):
		counter = 0 
		if self.head == None:
			self.head = newnode
		else:
			currentnode = self.head
			while(currentnode.next is not None):
				currentnode = currentnode.next
			currentnode.next = newnode
			# print(currentnode.value)
	def printlist(self):
		currentnode = self.head
		while(currentnode is not None):
			print(currentnode.value)
			currentnode = currentnode.next
	
	def get_length(self):
		currentnode = self.head
		length = 0
		while currentnode is not None:
			currentnode = currentnode.next
			length += 1
		return length


	def check_palindrome(self):
		currentnode = self.head
		currentnode_2 = self.head
		prevnode = self.head
		length = Palindrome.get_length(self)
		for i in range(int(length)):	
			for j in range(length - i - 1):
				currentnode_2 = currentnode_2.next
			try:
				if (currentnode.value != currentnode_2.value):
					return False
			except:
				break
			currentnode_2 = self.head
			currentnode = currentnode.next
		return True


	def checkPalindromeUsingStack(self):
		currentnode = self.head
		l = []
		while currentnode:
			l.append(currentnode.value)
			currentnode = currentnode.next
		print("l =",l)
		currentnode = self.head
		while currentnode:
			if (currentnode.value != l.pop()):
				return False
			else:
				currentnode = currentnode.next
		return True

linkedlist = Palindrome()
firstnode = Node("1")
linkedlist.insertnode(firstnode)
secondnode = Node("2")
linkedlist.insertnode(secondnode)
thirdnode = Node("2")
linkedlist.insertnode(thirdnode)
fourthdnode = Node("1")
linkedlist.insertnode(fourthdnode)
# fifthnode = Node("2")
# linkedlist.insertnode(fifthnode)
# sixthnode = Node("2")
# linkedlist.insertnode(sixthnode)
# seventhnode = Node("2")
# linkedlist.insertnode(seventhnode)
# eighthnode = Node("1")
# linkedlist.insertnode(eighthnode)

(linkedlist.printlist())
print(linkedlist.check_palindrome())
# print(linkedlist.checkPalindromeUsingStack())