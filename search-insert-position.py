class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        if target >= nums[-1]:
            return len(nums)
        
        if target < nums[0]:
            return 0
        
        for i in range(len(nums) - 1):
            if target > nums[i] and target < nums[i + 1]:
                return i + 1
    
    
if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 7))