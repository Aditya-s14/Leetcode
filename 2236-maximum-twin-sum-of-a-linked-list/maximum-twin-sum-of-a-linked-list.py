# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        slow,fast = head,head

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None

        prev = None
        curr = slow
        nextNode = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        top = dummy.next
        bottom = prev
        curr_sum = 0
        maxsum = 0
        while top and bottom:
            curr_sum = top.val+bottom.val
            maxsum = max(curr_sum,maxsum)
            top = top.next
            bottom = bottom.next

        return maxsum
        