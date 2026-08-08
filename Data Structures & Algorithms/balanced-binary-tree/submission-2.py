# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for every node, check height left, check height right, if ofo by more than one, return false

        def height(node):
            if node == None:
                return 0, True
            
            hl, bl = height(node.left)
            hr, br = height(node.right)
            balance = abs(hl - hr) <= 1 and br and bl
            return (1 + max(hl, hr), balance)

        _, bal = height(root)
        return bal
            
