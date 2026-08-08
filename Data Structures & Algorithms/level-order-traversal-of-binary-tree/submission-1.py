# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level_order = []

        while queue:
            level_size = len(queue)
            sublevel = []
            for i in range(level_size):
                node = queue.popleft()

                if not node:
                    continue
                
                sublevel.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            if sublevel:
                level_order.append(sublevel)

        return level_order