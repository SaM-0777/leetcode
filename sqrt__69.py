class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))
        
        
if __name__ == "__main__":
    print(Solution().mySqrt(8))