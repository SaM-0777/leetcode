class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = ''.join([str(i) for i in num])
        return list([int(i) for i in str(int(n) + k)])


if __name__ == "__main__":
    print(Solution().addToArrayForm([1,2,0,0], 34))