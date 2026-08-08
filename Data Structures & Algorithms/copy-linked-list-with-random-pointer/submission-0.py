"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_curr = head
        new_head = None
        curr = None
        prev = None
        random = {}

        # first wire up the next
        while old_curr:
            curr = Node(old_curr.val, None)
            random[old_curr] = curr
            if prev:
                prev.next = curr
            else:
                new_head = curr

            prev = curr
            old_curr = old_curr.next

        # then wire up the random pointers
        old_curr = head
        curr = new_head
        while old_curr:
            if old_curr.random:
                curr.random = random[old_curr.random]
            else:
                curr.random = None

            old_curr = old_curr.next
            curr = curr.next

        return new_head
            
