class Solution {
  int numIdenticalPairs(List<int> nums) {
    int count = 0;

    for (int i = 0; i < nums.length - 1; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] == nums[j]) count++;
      }
    }

    return count;
  }
}

void main(List<String> args) {
  print(Solution().numIdenticalPairs([1,1,1,1]));
}
