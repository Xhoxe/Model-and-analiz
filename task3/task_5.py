class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

node4 = ListNode(4)
node5 = ListNode(5)
node1 = ListNode(1)
node9 = ListNode(9)
node4.next = node5
node5.next = node1
node1.next = node9

deleteNode(node5)
current = node4
while current:
    print(current.val, end=" -> ")
    current = current.next
