from collections import Counter

class Solution:
    def hammingWeight(self, n) -> int:
        res = Counter(n)
        print(str(n))
        print('res', res)
        return res['1']
    
if __name__ == "__main__":
    print(Solution().hammingWeight('00000000000000000000000010000000'))
