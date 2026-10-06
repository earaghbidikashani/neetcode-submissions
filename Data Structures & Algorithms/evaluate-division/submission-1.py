class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # var : [(var, ratoio)]

        i = 0
        while i < len(equations):
            a, b = equations[i]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/ values[i]))
            i += 1

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque([(src, 1)])
            visited = set()
            visited.add(src)

            while q:
                curr, currR = q.popleft()
                if curr == target:
                    return currR

                for var, ratio in adj[curr]:
                    if var not in visited:
                        visited.add(var)
                        q.append((var, ratio * currR))

            return -1

        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        return res