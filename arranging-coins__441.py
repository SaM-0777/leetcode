import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2 * n + 0.25) - 0.5)


if __name__ == "__main__":
    print(Solution().arrangeCoins(1804289383))