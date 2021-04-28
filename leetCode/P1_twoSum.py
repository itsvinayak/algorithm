class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        for i in range(len(nums)):
            if target - nums[i] not in Hmap:
                Hmap[nums[i]] = i
            else:
                return [Hmap[target - nums[i]], i]
