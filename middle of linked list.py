# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need to use the rabit and the turtle way
        # where the rabbit will go twice as fast and when it reaches the end 
        # that means , we are at a null on the rabit , we will return the counter of the turtle 

        rabit = head 
        turtle = head 

        while rabit and rabit.next :
            rabit = rabit.next.next 
            turtle = turtle.next 

        return turtle
