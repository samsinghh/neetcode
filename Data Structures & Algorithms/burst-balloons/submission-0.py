class Solution:
    def maxCoins(self, nums):
        balloons = [1] + nums + [1]
        n = len(nums)

        best = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1

                for last in range(left, right + 1):
                    coins = balloons[left - 1] * balloons[last] * balloons[right + 1]
                    coins += best[left][last - 1] + best[last + 1][right]

                    best[left][right] = max(best[left][right], coins)

        return best[1][n]