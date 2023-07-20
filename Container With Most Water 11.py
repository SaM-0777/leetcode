class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        for i in range(len(height)):
            h = max(arg1, arg2)
            k = (i + 1) * h
            area = max(area, k)


if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))