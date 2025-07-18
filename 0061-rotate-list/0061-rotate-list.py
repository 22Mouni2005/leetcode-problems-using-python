# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        temp=head
        l=1
        while temp.next:
            temp=temp.next
            l+=1
        temp.next=head
        k=k%l
        s=l-k
        temp=head
        for i in range(s-1):
            temp=temp.next
        n_head=temp.next
        temp.next=None
        return n_head
        