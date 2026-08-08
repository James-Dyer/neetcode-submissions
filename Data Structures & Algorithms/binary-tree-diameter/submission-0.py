# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for each node, diameter = height left + height right

        def height(node) -> (int, int):
            if node == None:
                return 0, 0
                
            lh, ld = height(node.left)
            rh, rd = height(node.right)
            diameter = max(ld, rd, lh + rh)
            return (1 + max(lh, rh), diameter)

        _, diameter = height(root)
        return diameter