# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        # preorder
        # O(n)

        def dfs(node, seen) -> int:
            if not node:
                return 0
            
            good = 1 if node.val >= seen else 0
            seen = max(seen, node.val)
            
            return good + dfs(node.left, seen) + dfs(node.right, seen)

        
        return dfs(root, float('-inf'))
