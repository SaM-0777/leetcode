class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = columnTitle[::-1]
        return sum([(ord(s[i]) - 64) * (26 ** i) for i in range(len(s))])


if __name__ == "__main__":
    print(Solution().titleToNumber('AHP'))