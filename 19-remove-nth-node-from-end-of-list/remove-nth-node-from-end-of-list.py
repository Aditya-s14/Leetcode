class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # delete node
        slow.next = slow.next.next

        return dummy.next
