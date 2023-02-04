class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            k = -1
        else:
            k = 1
        
        y = 0
        z = abs(x)

        while z >= 1:
            y = y * 10 + z % 10
            z = z // 10

        result = y * k

        if -(2 ** 31) < result < (2 ** 31):
            return result
        else:
            return 0

if __name__ == "__main__":
    print(Solution().reverse(1534236469))