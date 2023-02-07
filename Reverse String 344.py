class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[len(s) - i -1]
            s[len(s) - i - 1] = temp

        return s



if __name__ == "__main__":
    print(Solution().reverseString(["h", "a", "i", "r"]))