from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        #print(indegree)
        #print(adj)
        #print(q)
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            
            for nei in adj[curr]:
                indegree[nei] -= 1
                #print(indegree)
                if indegree[nei] == 0 and nei not in visited:
                    q.append(nei)
                    visited.add(nei)
                print(q)

        #print("")
        #print(indegree)
        #print(res)


        return len(res) == numCourses

        
        