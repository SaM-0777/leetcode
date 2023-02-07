class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        k = 1
        i = 1
        if n == 1:
            return True
        while k < n:
            k = 3 ** i
            if k == n:
                return True
            i += 1
        return  False


if __name__ == "__main__":
    print(Solution().isPowerOfThree(1))