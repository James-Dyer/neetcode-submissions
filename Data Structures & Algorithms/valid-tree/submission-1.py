from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree:
            # With V vertices, there are V - 1 edges
            # The tree is not disconencted anywhere

        # This confirms all requirements of a valid tree:
            # A cycle will result in > V-1 edges
            # A unconnected subgraphs will result in < V-1 edges
            # Therefor we only need to confirm # edges and 
            # that every node is reachable from any node in the tree

        if n - 1!= len(edges):
            return False

        if not edges:
            return True

        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        stack = deque()
        stack.append(edges[0][0])
        visited = set()
        visited.add(edges[0][0])
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
            
