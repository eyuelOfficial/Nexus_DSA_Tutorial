# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      # having the dummy will help with edge cases , so it is needed 
        dummy = ListNode(0)
        dummy.next = head
        
        
        first = second = dummy
        for _ in range(n + 1):
            first = first.next
          
        # now the pointer is on the nth 
        # and now we go through it , the slow and fast and make the slow to be on the nth from the end 
      
        while first:
            first = first.next
            second = second.next
        
    
        second.next = second.next.next
    
        return dummy.next
