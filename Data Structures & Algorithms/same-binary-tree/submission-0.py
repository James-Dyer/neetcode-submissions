# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(np, nq):
            if not np and not nq:
                return True
            elif np and not nq or nq and not np:
                return False

            return np.val == nq.val and dfs(np.left, nq.left) and dfs(np.right, nq.right)

        return dfs(p, q)

            