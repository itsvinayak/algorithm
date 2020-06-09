# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

memo = [[None for _ in range(1001)] for _ in range(1001)]


def isPalindrome(x):
    return x == x[::-1]


def PalindromePartitioningRec(string, i, j):
    if i >= j or isPalindrome(string[i : j + 1]):
        return 0
    ans = float("inf")
    for k in range(i, j):
        count = (
            1
            + PalindromePartitioningRec(string, i, k)
            + PalindromePartitioningRec(string, k + 1, j)
        )
        ans = min(ans, count)
    return ans


def PalindromePartitioningDp(string, i, j):
    if i >= j or isPalindrome(string[i : j + 1]):
        return 0
    if memo[i][j] is not None:
        return memo[i][j]

    ans = float("inf")
    for k in range(i, j):
        count = (
            1
            + PalindromePartitioningDp(string, i, k)
            + PalindromePartitioningDp(string, k + 1, j)
        )
        ans = min(ans, count)
    memo[i][j] = ans
    return memo[i][j]


def PalindromePartitioningDpImprove(string, i, j):
    if i >= j or isPalindrome(string[i : j + 1]):
        return 0
    if memo[i][j] is not None:
        return memo[i][j]
    ans = float("inf")
    for k in range(i, j):
        if memo[i][k] is not None:
            return memo[i][k]
        else:
            memo[i][k] = PalindromePartitioningDpImprove(string, i, k)
            return memo[i][k]
        if memo[k - 1][j] is not None:
            return memo[k - 1][j]
        else:
            memo[k - 1][j] = PalindromePartitioningDpImprove(string, k - 1, j)
            return memo[k - 1][j]
        count = 1 + memo[i][k] + memo[k - 1][j]
        ans = min(ans, count)
    memo[i][j] = ans
    return memo[i][j]


def main():
    string = "aab"
    print(
        "Min cuts needed for Palindrome Partitioning is ",
        PalindromePartitioningRec(string, 0, len(string) - 1),
    )
    print(
        "Min cuts needed for Palindrome Partitioning is ",
        PalindromePartitioningDp(string, 0, len(string) - 1),
    )
    print(
        "Min cuts needed for Palindrome Partitioning is ",
        PalindromePartitioningDpImprove(string, 0, len(string) - 1),
    )


if __name__ == "__main__":
    main()
