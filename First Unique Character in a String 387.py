from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i in freq:
            if freq[i] == 1:
                return s.index(i)

        return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar('dddccdbba'))