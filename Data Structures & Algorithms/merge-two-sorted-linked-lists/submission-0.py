# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # like 2 pointers for LL
        # always compare the current node of L1 & L2
        #while current
        # if L2 >= L1 then L1.next() = L2
        # YOU CAN CREATE NEW LIST
        newList = Node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                Node.next = list1
                list1 = list1.next
            else:
                Node.next = list2
                list2 = list2.next
            Node = Node.next
        
        Node.next = list1 or list2 #whatever head not empty and uses other to fill up
        return newList.next
