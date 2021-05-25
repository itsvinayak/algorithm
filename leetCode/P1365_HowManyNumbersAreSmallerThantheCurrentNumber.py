from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tempList = sorted(nums)  # O(nlogn)

        return [tempList.index(num) for num in nums]
