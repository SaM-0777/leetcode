class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        elem_freq = {}
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in elem_freq:
                elem_freq[nums[i]] = 1
            else:
                del nums[i]
                
        return len(elem_freq)

if __name__ == "__main__":
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))