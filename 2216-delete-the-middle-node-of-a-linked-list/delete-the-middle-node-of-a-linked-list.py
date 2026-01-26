# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        slow,fast = head,head

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = slow.next
        return dummy.next
        