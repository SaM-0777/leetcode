class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).replace('0b', '')
        
if __name__ == "__main__":
    print(Solution().addBinary('11', '1'))