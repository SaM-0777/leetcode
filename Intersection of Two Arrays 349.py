class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))

if __name__ == "__main__":
    print(Solution().intersection([1,2,2,1], [2,2]))