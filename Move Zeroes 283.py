class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                start = i

                for j in range(start, len(nums)):
                    if nums[j] != 0:
                        # swap
                        temp = nums[start]
                        nums[start] = nums[j]
                        nums[j] = temp
                        break
        
        return nums



if __name__ == "__main__":
    print(Solution().moveZeroes([0,1,0,3,0,12,15]))

