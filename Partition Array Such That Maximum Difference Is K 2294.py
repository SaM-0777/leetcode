class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = 1
        mn = mx = nums[0]
        for n in nums:
            mn = min(mn, n)
            mx = max(mx, n)
            if mx - mn > k:
                count += 1
                mn = mx = n
        return count


if __name__ == "__main__":
    print(Solution().partitionArray([3,6,1,2,5], 2))