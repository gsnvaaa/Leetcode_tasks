class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            next = curr.next

            if curr.val == val:
                prev.next = next
            else:
                prev = curr

            curr = next
        return dummy.next