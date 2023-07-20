class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        
        else:
            return sum(nums[(len(nums) // 2) - 1 : len(nums) // 2 + 1]) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3, 4], [2]))