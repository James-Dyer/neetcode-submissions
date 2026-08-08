# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        pval, qval = min(p.val, q.val), max(p.val, q.val)

        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                continue

            if node.val == pval or node.val == qval:
                return node
                
            if node.val > qval:
                queue.append(node.left)
            elif node.val < pval:
                queue.append(node.right)
            else:  
                return node
