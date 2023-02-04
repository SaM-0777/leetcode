import re

class Solution:
    def myAtoi(self, s: str) -> int:
        """s = s.strip()

        if s[0] == '-':
            k = -1
        else:
            k = 1

        num_string = re.sub(r'[^\d]', "", s)

        result = int(num_string) * k

        if result > (2 ** 31) - 1:
            return (2 ** 31) - 1
        
        elif result < -(2 ** 31):
            return -(2 ** 31)
        
        return result"""

        s=s.lstrip()
        sign,res,i=1,0,0
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res = max(min(res * sign, 2**31 - 1), -2**31)
        return res


if __name__ == "__main__":
    print(Solution().myAtoi('words and 987'))