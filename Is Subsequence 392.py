class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)

        if len(s) == 0:
            return True

        for i in range(len(t_arr)):
            if i < len(s_arr):
                if t_arr[i] != s_arr[i]:
                    s_arr.insert(i, t_arr[i])
            else:
                s_arr.append(t_arr[i])

        if ''.join(s_arr) == t:
            return True
        return False


if __name__ == "__main__":
    print(Solution().isSubsequence('b', 'abc'))