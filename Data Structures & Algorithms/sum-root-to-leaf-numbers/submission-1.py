# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, number):
            if not node:
                return 0

            number = (number * 10) + node.val
            
            if not node.left and not node.right:
                return number
            
            return dfs(node.left, number) + dfs(node.right, number)

        return dfs(root, 0)