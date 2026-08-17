class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        dep_graph = defaultdict(list)

        for course, prereq in prerequisites:
            dep_graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for course in dep_graph[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return res if len(res) == numCourses else []