class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        from collections import Counter
        
        elem_freq = Counter(nums)
        for i in elem_freq:
            if elem_freq[i] > 1:
                return True
        return False
    
    
if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3,]))