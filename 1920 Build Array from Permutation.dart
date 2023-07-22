class Solution {
  List<int> getConcatenation(List<int> nums) {
    return nums + nums;
  }
}

void main(List<String> args) {
  print(Solution().getConcatenation([1, 2, 1]));
}
