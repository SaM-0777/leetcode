class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit_sum = 0
            while num >= 1:
                digit_sum += num % 10
                num = num // 10
            num = digit_sum
        
        return num
            
        
        
        
if __name__ == "__main__":
    print(Solution().addDigits(10))