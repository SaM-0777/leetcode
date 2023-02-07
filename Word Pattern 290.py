class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k = {}

        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in k:
                if len(k) != 0:
                    for key, value in k:
                        if value == s[i] and key != pattern[i]:
                            return False
                k.update({pattern[i]: s[i]})
            else:
                if k[pattern[i]] != s[i]:
                    return False



if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat dog"))