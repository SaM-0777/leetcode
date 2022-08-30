class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        while True:
            for i in str(n):
                res += int(i) ** 2
            n = res
            res = 0
            if n == 1:
                return True
    
    
if __name__ == "__main__":
    print(Solution().isHappy(19))