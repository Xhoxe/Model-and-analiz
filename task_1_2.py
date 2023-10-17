class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Node) -> Node:
    if not head or not head.next:
        return head
    temp = head.next
    head.next = swapPairs(temp.next)
    temp.next = head
    return temp

def printList(node: Node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4))))
printList(head)
head = swapPairs(head)
printList(head)  
