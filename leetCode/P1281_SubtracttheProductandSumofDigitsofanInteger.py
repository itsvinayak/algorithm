class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n:
            r = n % 10
            product *= r
            sum += r
            n //= 10
        return product - sum
        