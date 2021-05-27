from typing import List


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # eq. of circle : (x-h)^2 + (y-k)^2 = r^2
        ans = []
        for circle in queries:
            count = 0
            h = circle[0]
            k = circle[1]
            r = circle[2]
            for point in points:
                right = (point[0] - h) ** 2 + (point[1] - k) ** 2
                if right <= r ** 2:
                    count += 1
            ans.append(count)
        return ans
