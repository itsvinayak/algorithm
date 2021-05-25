class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in nums:
            ans |= i
        return ans * pow(2, n - 1)
