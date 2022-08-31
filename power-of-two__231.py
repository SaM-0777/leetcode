class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        
        if n == 0:
            return False
        
        while n > 0:
            if n % 2 != 0 and n != 1:
                return False
            n = n // 2
            
        return True
        

if __name__ == "__main__":
    print(Solution().isPowerOfTwo(-16))