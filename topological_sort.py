class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses

        for source, dest in prerequisites:
            adjList[source].append(dest)
            inDegree[dest] += 1

        q = [i for i in range(numCourses) if inDegree[i] == 0]

        # list to store sorted elements
        L = []

        # q -> set of nodes with no incoming edges
        while q:
            node = q.pop()
            L.append(node)
            for m in adjList[node]:
                inDegree[m] -= 1
                if inDegree[m] == 0:
                    q.append(m)

        return len(L) == numCourses
