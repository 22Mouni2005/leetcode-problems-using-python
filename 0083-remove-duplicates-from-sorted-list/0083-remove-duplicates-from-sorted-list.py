# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=f=head
        while f and f.next:
            f=f.next
            if f.val==temp.val:
                temp.next=f.next
            else:
                temp=f
        return head