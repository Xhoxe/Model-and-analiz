class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    if not head or not head.next:
        return head

    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

def linkedListToArray(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head1 = ListNode(1, ListNode(1, ListNode(2)))
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

print(linkedListToArray(removeDuplicates(head1))) 
print(linkedListToArray(removeDuplicates(head2))) 
