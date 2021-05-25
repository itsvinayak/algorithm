from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        Hmap = defaultdict(int)
        for i in nums:
            sum += Hmap[i]
            Hmap[i] += 1
        return sum
