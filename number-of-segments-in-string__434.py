class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split())


if __name__ == "__main__":
    print(Solution().countSegments(""))

