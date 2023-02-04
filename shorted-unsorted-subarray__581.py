from itertools import combinations

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        arr = [list(i) for i in combinations(nums, len(nums))]
        
        shorted_subarray = min(arr, key= lambda x: len(x))

        return shorted_subarray


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2,6,3,8,7]))