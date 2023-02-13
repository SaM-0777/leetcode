class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_arr = list(s)
        t_arr = list(t)
        op = []

        for i in t_arr:
            if i not in s_arr and i not in op:
                op.append(i)
            else:
                s_arr.remove(i)


        return "".join(op)


if __name__ == "__main__":
    print(Solution().findTheDifference("abcd", "abcde"))