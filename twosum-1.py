import numpy as np

class Solution:
    def twoSum(self, nums: List(int), target: int) -> List[int]:
        for i in range(len(nums)): 
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if i == j:
                    continue
                return [i, j]
                
    
    
if __name__ == '__main__':
    S = Solution()
    nums, target = np.array(input().split(','), int), int(input())
    
    print(S.twoSum(nums, target))