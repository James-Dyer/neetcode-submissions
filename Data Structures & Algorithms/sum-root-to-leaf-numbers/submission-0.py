# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(node, number):
            nonlocal res
            number = (number * 10) + node.val
            
            if node.left:
                dfs(node.left, number)
            if node.right:
                dfs(node.right, number)
            
            if not node.left and not node.right:
                res += number

        dfs(root, 0)
        return res