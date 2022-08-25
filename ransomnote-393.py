class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_chars = [*ransomNote]
        magazine_chars = [*magazine]
        count = 0
        
        for _ in ransomNote_chars:
            if _ in magazine_chars:
                magazine_chars.remove(_)
                count += 1
        
        if count == len(ransomNote_chars):
            return True
        return False


if __name__ == '__main__':
    S = Solution()
    ransomNote, magazine = input().split()
    
    print(S.canConstruct(ransomNote, magazine))