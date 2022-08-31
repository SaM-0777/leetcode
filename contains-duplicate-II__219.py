class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        elem_indices = {}
        for x in enumerate(nums):
            if x[1] not in elem_indices:
                elem_indices[x[1]] = [x[0]]
            else:
                elem_indices[x[1]].append(x[0])
                
        for x in elem_indices:
            for i in range(1, len(elem_indices[x])):
                if elem_indices[x][i] - elem_indices[x][i - 1] <= k:
                    return True
        
        return False
    
    
if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1,0,1, 1], 1))