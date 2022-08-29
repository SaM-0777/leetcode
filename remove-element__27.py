class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        
        print(nums)
    
    
if __name__ == "__main__":
    print(Solution().removeElement([3, 2, 2, 3], 3))
    