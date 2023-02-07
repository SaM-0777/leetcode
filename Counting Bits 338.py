class Solution:
    def countBits(self, n: int) -> list[int]:
        op = []

        for i in range(n + 1):
            binary = bin(i).replace('0b', '')
            op.append(binary.count('1'))

        return op




if __name__ == "__main__":
    print(Solution().countBits(5))