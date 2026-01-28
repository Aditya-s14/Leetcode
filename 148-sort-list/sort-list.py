class Solution:
    def merge(self, l1, l2):
        dummy = ListNode(0)
        node = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        # attach remaining nodes
        node.next = l1 if l1 else l2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ✅ base case
        if not head or not head.next:
            return head

        slow = fast = head
        prev = None

        # find middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # split list
        prev.next = None

        # recursive sort
        left = self.sortList(head)
        right = self.sortList(slow)

        # merge
        return self.merge(left, right)
