from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsSum = 0
        for i in range(n):
            numsSum += nums[i]
            nums[i] = numsSum
        return nums
