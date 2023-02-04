class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num).replace('0b', '')
        result = []

        for i in binary_num:
            if i == '0':
                result.append('1')
            else:
                result.append('0')
        
        print(result)

        return int(''.join(result), 2)



if __name__ == "__main__":
    print(Solution().findComplement(5))

