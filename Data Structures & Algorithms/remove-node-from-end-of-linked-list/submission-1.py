# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def len_linkedlist(self, head) -> int:
            curr = head
            length = 0
            while curr:
                length += 1
                curr = curr.next
            
            return length
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of linked list O(n)
        # go to node len(linked_list) - n O(n)
            # remove it, wire the prev node to the next node
            
        length = self.len_linkedlist(head)

        curr = head
        prev = None
        for _ in range(length - n):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
            return head
        else:
            return head.next
