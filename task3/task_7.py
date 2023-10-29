class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq


def mergeKLists(lists):
    min_heap = []
    for head in lists:
        while head:
            heapq.heappush(min_heap, head.val)
            head = head.next
            
    dummy = ListNode(-1)
    current = dummy
    while min_heap:
        current.next = ListNode(heapq.heappop(min_heap))
        current = current.next
        
    return dummy.next

list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
result = mergeKLists(lists)

while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
