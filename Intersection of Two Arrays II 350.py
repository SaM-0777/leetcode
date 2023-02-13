class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op = []
        if len(nums1) > len(nums2):
            n = len(nums2)
            temp = nums1
        else:
            n = len(nums1)
            temp = nums2
        i = 0
        while i <= n:
            if nums1[i] in nums2:
                op.append(nums1[i])
            i += 1

        op.append(temp[i:])

        return op


if __name__ == "__main__":
    print(Solution().intersection([1,2,2,1], [2,2]))

