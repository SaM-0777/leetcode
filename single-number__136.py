class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        elem_freq = {}
        
        for n in nums:
            if n not in elem_freq:
                elem_freq[n] = 1
            else:
                elem_freq[n] += 1
        
        return int(*[x for x in elem_freq if elem_freq[x] == 1])



if __name__ == "__main__":
    print(Solution().singleNumber([4,1,2,1,2]))