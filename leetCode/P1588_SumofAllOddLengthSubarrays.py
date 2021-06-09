class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i,len(arr)):
                sum += arr[j]
                if (j - i) % 2 == 0:
                    res += sum
        return res


# using dp https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854608/Python-O(N)-dp
# Explanation:
#     - dp[i] is the sum of all arrays that end at index i.
#     - i // 2 is how many subarrays of odd length end at index i - 2.

def sumOddLengthSubarrays(self, arr: List[int]) -> int:
	dp = list(arr)
	for i, a in enumerate(arr):
		if i > 1: dp[i] += (i // 2) * (arr[i] + arr[i-1]) + dp[i - 2]
	return sum(dp)
