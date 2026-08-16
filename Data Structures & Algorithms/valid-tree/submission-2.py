from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # An undirected graph is a tree iff:
            # 1. It has exactly V - 1 edges
            # 2. All V vertices are connected

        if n - 1!= len(edges):
            return False

        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        stack = deque()
        stack.append(0)
        visited = set()
        visited.add(0)
        count = 1

        while stack:
            curr = stack.pop()

            for edge in graph[curr]:
                if edge in visited:
                    continue

                visited.add(edge)
                stack.append(edge)
                count += 1


        return count == n
            
