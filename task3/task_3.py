class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

def createLinkedListWithCycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]

    return head

head1 = createLinkedListWithCycle([3,2,0,-4], 1)
print(hasCycle(head1))
head2 = createLinkedListWithCycle([1,2], 0)
print(hasCycle(head2))
head3 = createLinkedListWithCycle([1], -1)
print(hasCycle(head3))
