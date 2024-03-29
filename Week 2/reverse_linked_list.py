# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        current = head

        while current.next is not None:

            temp = current.next
            current.next = current.next.next
            temp.next = head
            head = temp
        
        return head