from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        
        for pre in prerequisites: 
            a, b = pre[0], pre[1]
            adj[b].append(a)
            indegree[a] += 1

        q = deque()
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)

        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0 and nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        
        if len(res) == numCourses:
            return res
        return []
