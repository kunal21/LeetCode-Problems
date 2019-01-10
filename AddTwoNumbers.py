class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def AddTwoNumbers(root):
    stack = []
    while(root):
        stack.append(root.val)
        root = root.next
    return stack[::-1]


linkedlist = Node(2)
linkedlist.next = Node(4)
linkedlist.next.next = Node(3)

print(AddTwoNumbers(linkedlist))
