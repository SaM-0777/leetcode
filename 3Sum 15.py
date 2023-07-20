from itertools import permutations, combinations, combinations_with_replacement


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        combo_3 = set(list(combinations(nums, r=3)))
        op = []
        for pair in combo_3:
            if sum(pair) == 0:
                op.append(pair)

        for o in op:
            print("Hello")

        return o


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
