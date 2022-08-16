# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        head.next = l1
        prev = head
        change_flag = False
        while l1 or l2:
            val1 = 0
            if l1:
                val1 = l1.val
            val2 = 0
            if l2:
                val2 = l2.val
            tmp = val1 + val2 + carry
            carry = tmp // 10
            tmp = tmp % 10
            if l1:
                l1.val = tmp
                l1 = l1.next
            else:
                if not change_flag:
                    prev.next = l2
                    change_flag = True
            if l2:
                if change_flag:
                    l2.val = tmp
                l2 = l2.next
            prev = prev.next
        if carry:
            prev.next = ListNode(1)
        return head.next
