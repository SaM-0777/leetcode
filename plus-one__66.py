class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_in_str = [str(_) for _ in digits]
        num_str = ''.join(digits_in_str).replace(',', '')
        return ([*str(int(num_str) + 1)])
    

if __name__ == "__main__":
    print(Solution().plusOne([9]))