# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        temp=head
        fast=head
        n=0
        while temp:
            temp=temp.next
            n+=1
        for i in range(n//2):
            fast=fast.next
        return fast