class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set([x for x in range(1, len(nums) + 1)]).difference(set(nums)))



if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([1,1]))