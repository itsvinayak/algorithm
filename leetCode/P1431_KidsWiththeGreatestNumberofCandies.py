from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        compCandies = max(candies) - extraCandies
        ans = []
        for i in candies:
            if i >= compCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
