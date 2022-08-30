class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(format(n, 'b')).zfill(32)[:: -1], 2)


if __name__ == "__main__":
    print(Solution().reverseBits('00000010100101000001111010011100'))
