class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candySet = set(candyType)
        return int(min(len(candySet), len(candyType) / 2))




if __name__ == "__main__":
    print(Solution().distributeCandies([6,6,6,6]))