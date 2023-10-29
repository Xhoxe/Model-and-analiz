class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse(head, k):
        prev = None
        curr = head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev

    def getLength(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    length = getLength(head)
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while length >= k:
        group_start = prev_group_end.next
        group_end = reverse(group_start, k)
        prev_group_end.next = group_end
        group_start.next = group_end.next
        prev_group_end = group_start
        length -= k

    return dummy.next
    
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = reverseKGroup(list1, 2)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
