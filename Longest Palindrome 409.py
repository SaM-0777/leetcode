import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        print(collections.Counter(s).values())
        for i in collections.Counter(s).values():
            res += i // 2 * 2
        return min(res+1, len(s))



if __name__ == "__main__":
    print(Solution().longestPalindrome('abccccdd'))