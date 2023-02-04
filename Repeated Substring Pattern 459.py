from itertools import combinations

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))