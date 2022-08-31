class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        def divide(a, b):
            while a % b == 0:
                a = a / b
            return a
        
        n = divide(n, 2)
        n = divide(n, 3)
        n = divide(n, 5)
        
        return True if n == 1 else False

        
        
    
if __name__ == "__main__":
    print(Solution().isUgly(14))