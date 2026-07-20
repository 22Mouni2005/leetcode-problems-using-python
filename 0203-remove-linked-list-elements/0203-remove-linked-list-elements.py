# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if not head:
            return None
        slow=head
        while slow.next:
            if slow.next.val==val:
                slow.next=slow.next.next
            else:
                slow=slow.next
        return head

        