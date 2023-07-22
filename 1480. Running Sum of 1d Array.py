class Solution:
  def runningSum(self, nums: list[int]) -> list[int]:
    op = []

    for i in range(len(nums)):
        op.append(sum(nums[:i + 1]))

    return op
  

if __name__ == "__main__":
  print(Solution().runningSum([1,2,3,4]))
