class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        reverse = 0
        while (x > 0):
            reverse = reverse * 10 + x % 10
            x = x // 10
        if org == reverse:
            return True
        return False
    
if __name__ == '__main__':
    S = Solution()
    x = int(input())
    
    print(S.isPalindrome(x))