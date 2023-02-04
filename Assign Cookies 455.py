class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        children, i, j = 0, 0, 0

        g.sort()
        s.sort()

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i, children = i + 1, children + 1
            j += 1

        return children

if __name__ == "__main__":
    print(Solution().findContentChildren([10,9,8,7], [5,6,7,8]))