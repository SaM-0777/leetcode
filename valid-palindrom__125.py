class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(c for c in s if c.isalnum())).lower()
        if s == s[::-1]:
            return True
        else:
            return False
    
    
if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))