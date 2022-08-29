class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    

if __name__ == "__main__":
    print(Solution().climbStairs(45))