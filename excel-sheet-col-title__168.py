class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            s = chr(ord('A') + (columnNumber-1) % 26) + s
            columnNumber = (columnNumber-1)//26
        
        return s
    
    
if __name__ == "__main__":
    print(Solution().convertToTitle(900))