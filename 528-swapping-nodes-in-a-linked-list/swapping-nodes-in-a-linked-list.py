class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k - 1):
            first = first.next

        left = first
        right = head

        while left.next:
            left = left.next
            right = right.next

        first.val, right.val = right.val, first.val
        return head
