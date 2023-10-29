class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleNumber(head):
    current = head
    number = 0
    while current:
        number = number * 10 + current.val
        current = current.next
    number *= 2
    
    dummy = ListNode(-1)
    current = dummy
    for digit in str(number):
        current.next = ListNode(int(digit))
        current = current.next
    
    return dummy.next

head1 = ListNode(1, ListNode(8, ListNode(9)))
result1 = doubleNumber(head1)
while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next
print("None")
