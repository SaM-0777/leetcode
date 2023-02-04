class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        op = ''
        d = [[] for i in range(numRows)]
        oprnSwitch = 0  # 0 -> add, 1 -> sub
        k = 0
        for char in s:
            if k == 0:
                oprnSwitch = 0
            elif k == numRows - 1:
                oprnSwitch = 1

            d[k].append(char)
            
            if oprnSwitch:
                k = k - 1
            else:
                k = k + 1

        for arr in d:
            op = op + "".join(arr)

        return op


if __name__ == "__main__":
    print(Solution().convert('AB', 2))

