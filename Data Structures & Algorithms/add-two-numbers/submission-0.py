# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        r_prev = None
        c1, c2 = l1, l2
        carry = 0

        while c1 and c2:
            my_sum = c1.val + c2.val
            if carry:
                my_sum += carry
            carry = my_sum // 10
            my_sum %= 10
            

            my_node = ListNode(my_sum)
            if res:
                r_prev.next = my_node
                r_prev = r_prev.next
            else:
                r_prev = my_node
                res = my_node
            
            c1 = c1.next
            c2 = c2.next

        # catch remainder
        while c1 or c2:
            if c1:
                my_sum = c1.val
                if carry:
                    my_sum += carry
                carry = my_sum // 10
                my_sum %= 10
                my_node = ListNode(my_sum)
                r_prev.next = my_node
                r_prev = r_prev.next
                c1 = c1.next
            else:
                my_sum = c2.val
                if carry:
                    my_sum += carry
                carry = my_sum // 10
                my_sum %= 10
                my_node = ListNode(my_sum)
                r_prev.next = my_node
                r_prev = r_prev.next
                c2 = c2.next
            
        if carry:
            my_node = ListNode(carry)
            r_prev.next = my_node

        return res