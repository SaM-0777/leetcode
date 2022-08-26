class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(len(strs[0]) + 1):
            if all(strs[0][:i] == s[:i] for s in strs):
                prefix = strs[0][:i]
            else:
                break
        return prefix

if __name__ == '__main__':
    S = Solution()
    strs = input().split()
    
    print(S.longestCommonPrefix(strs))