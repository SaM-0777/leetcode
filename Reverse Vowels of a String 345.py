class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']

        while i <= j:
            if s[i] in vowels:
                for k in range(j):



if __name__ == "__main__":
    print(Solution().reverseVowels(["h", "a", "i", "r"]))

