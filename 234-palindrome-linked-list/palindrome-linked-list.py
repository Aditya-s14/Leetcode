# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        slow = head
        fast = head

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None

        prev = None
        nextnode = None
        curr  = slow
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        top = head
        while top:
            if top.val != prev.val:
                return False
            top = top.next
            prev = prev.next
        return True

        