# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        merged_head = ListNode()
        merged_current = merged_head

        while list1 and list2:
            if list1.val <= list2.val:
                merged_current.val = list1.val
                list1 = list1.next
            else:
                merged_current.val = list2.val
                list2 = list2.next
            if list1 or list2:
                merged_current.next = ListNode()
                merged_current = merged_current.next
        
        if list1 is not None:
            merged_current.val = list1.val
            merged_current.next = list1.next
        else:
            merged_current.val = list2.val
            merged_current.next = list2.next

        return merged_head