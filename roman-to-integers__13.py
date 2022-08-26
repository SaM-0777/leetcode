class Solution:
    def __init__(self, symbols): 
        self.symbols = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i > 0 and self.symbols[s[i]] > self.symbols[s[i - 1]]:
               res += self.symbols[s[i]] - 2 * self.symbols[s[i - 1]]
            else:
                res += self.symbols[s[i]]
        
        return res 




if __name__ == '__main__':
    S = Solution([])
    s = input()
    
    print(S.romanToInt(s))