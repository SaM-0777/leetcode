class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        nums = [str(i) for i in nums]
        s = ''.join(nums)
        ones = s.split('0')
        
        return max([len(i) for i in ones])
        
        


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,0,1,1,1]))

