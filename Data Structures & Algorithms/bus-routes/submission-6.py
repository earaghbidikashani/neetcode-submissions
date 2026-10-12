class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = defaultdict(list) # stop : [(stop, bus)]
        if source == target:
            return 0
        i = 0
        while i < len(routes):
            route = routes[i]
            stop = 0
            while stop < len(route) - 1:
                fromStop = route[stop] 
                toStop = route[stop + 1]
                adj[fromStop].append((toStop, i))

                stop += 1
            
            adj[route[stop]].append((route[0], i))
            i += 1
        
        #heap = [(0, r, source)] # dist, bus num, node
        #dist = {source: 0}
        # adj: fromStop : [(toStop, bus)]

        heap = [(1, x, source) for x in range(len(routes)) if source in routes[x]]
        dist = {source: 1}

        while heap: 
            print(heap)
            currDist, busNum, currStop = heapq.heappop(heap)

            if currDist > dist[currStop]:
                continue

            for toStop, nextBus in adj[currStop]:
                newDist = currDist
                if nextBus != busNum:
                    newDist += 1

                if newDist < dist.get(toStop, float("inf")):
                    dist[toStop] = newDist
                    heapq.heappush(heap, (newDist, nextBus, toStop)) # dist, bus num, node

            

        if target not in dist.keys():
            return -1
        return dist[target]




