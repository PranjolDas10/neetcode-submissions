# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        slowCurr = head

        while current and current.next: # for the fast pointer you need to make sure that the curr.next is not NONE
            if current.next == slowCurr:
                return True
            else:
                slowCurr = slowCurr.next
                current = current.next.next
        return False