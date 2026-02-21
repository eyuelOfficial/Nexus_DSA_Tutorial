# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True  # empty or single node is always palindrome

        # Step 1: Find the middle using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev now points to the head of reversed second half

        # Step 3: Compare first half and reversed second half
        first = head
        second = prev
        while second:  # only need to check second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
