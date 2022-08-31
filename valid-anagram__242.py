class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for x in set(s):
            if s.count(x) != t.count(x):
                return False
            
        return True
    
if __name__ == "__main__":
    print(Solution().isAnagram('anagram', 'nagaram'))
