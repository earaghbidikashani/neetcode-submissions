class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return (x ** 2 + y ** 2) ** 0.5

        res = []

        for point in points:
            x, y = point[0], point[1]
            currDist = -1 * dist(x, y)

            if len(res) < k:
                heapq.heappush(res, (currDist, point))
                continue

            smallest = res[0][0]

            if smallest < currDist:
                heapq.heappop(res)
                heapq.heappush(res, (currDist, point))

        return [x[1] for x in res]