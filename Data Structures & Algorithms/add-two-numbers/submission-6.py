# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        r_prev = dummy
        c1, c2 = l1, l2
        carry = 0

        while c1 and c2:
            total = c1.val + c2.val
            if carry:
                total += carry
            carry = total // 10
            total %= 10
            

            node = ListNode(total)
            r_prev.next = node
            r_prev = r_prev.next
            
            c1 = c1.next
            c2 = c2.next

        # catch remainder
        while c1 or c2 or carry:
            x = c1.val if c1 else 0
            y = c2.val if c2 else 0

            total = x + y + carry
            carry = total // 10
            total %= 10

            node = ListNode(total)
            r_prev.next = node
            r_prev = r_prev.next
            
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return dummy.next