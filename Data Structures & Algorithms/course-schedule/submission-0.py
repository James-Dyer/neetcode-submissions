from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        dep_graph = defaultdict(list) # course -> [courses it unlocks]
        for course, pre_req in prerequisites:
            dep_graph[pre_req].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            curr = queue.popleft()
            completed += 1
            for next_course in dep_graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses

        