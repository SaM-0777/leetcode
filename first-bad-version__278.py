# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(0):
            return 0
        start = 1
        end = n
        while start < end:
            mid = start + (end-start)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start


if __name__ == "__main__":
    print(Solution().firstBadVersion(1))
