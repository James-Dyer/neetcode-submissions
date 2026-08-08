# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # (node, depth)
        if not root:
            return 0

        max_depth = 0

        queue = deque()
        queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        
        return max_depth

        