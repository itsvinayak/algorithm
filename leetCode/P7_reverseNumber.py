class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -1 * int(str(abs(x))[::-1])

        if ans >= 2 ** 31 or ans <= -(2 ** 31):
            return 0
        else:
            return ans


######################################################


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = "N"
        if x != abs(x):
            x = x * -1
            neg = "Y"

        while x != 0:
            res = res * 10 + x % 10
            x = int(x / 10)

        ans = int(res) * -1 if neg == "Y" else int(res)

        if ans >= 2 ** 31 or ans <= -(2 ** 31):
            return 0
        else:
            return ans
