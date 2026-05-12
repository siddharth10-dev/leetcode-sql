class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            coins = mid * (mid + 1) // 2

            if coins <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans