class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        k = 1
        i = 1
        if n == 1:
            return True
        while k < n / 2:
            k = 4 ** i
            if k == n:
                return True
            i += 1
        return  False


if __name__ == "__main__":
    print(Solution().isPowerOfFour(16))