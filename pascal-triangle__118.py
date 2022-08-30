class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row_num_list = []
        sum = 0
        for i in range(2, numRows):
            row = []
            for j in range(row_num_list[i]):
                if j == 0 or j == len(row_num_list[i]) - 1:
                    row.append(1)
                else:
                    row.append()


if __name__ == "__main__":
    print(Solution().generate(5))
