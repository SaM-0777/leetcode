import collections

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elem_freq = dict(collections.Counter(nums))
        return int(*[x for x in elem_freq if elem_freq[x] > len(nums) / 2])
    

if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))