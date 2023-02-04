class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary_x = bin(x).replace('0b', '')
        binary_y = bin(y).replace('0b', '')

        if len(binary_x) < len(binary_y):
            binary_x = '0' * (len(binary_y) - len(binary_x)) + binary_x
        elif len(binary_y) < len(binary_x):
            binary_y = '0' * (len(binary_x) - len(binary_y)) + binary_y

        count, i = 0, 0

        while i < len(binary_x):
            if binary_x[i] != binary_y[i]:
                count += 1

            i += 1
        
        return count

if __name__ == "__main__":
    print(Solution().hammingDistance(3, 1))