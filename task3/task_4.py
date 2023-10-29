class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next or not head.next.next:
        return

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow.next
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    slow.next = None

    first, second = head, prev
    while second:
        next_temp = first.next
        first.next = second
        first = second
        second = next_temp

def createList(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def printList(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

head1 = createList([1,2,3,4])
reorderList(head1)
printList(head1)
head2 = createList([1,2,3,4,5])
reorderList(head2)
printList(head2)
