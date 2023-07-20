class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, base=2) + int(b, base=2)).replace("0b", "")


if __name__ == "__main__":
    print(Solution().addBinary('11', '100'))