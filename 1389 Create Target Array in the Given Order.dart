class Solution {
  List<int> createTargetArray(List<int> nums, List<int> index) {
    List<int> op = [];

    for (int i = 0; i < nums.length; i++) {
      op.insert(index[i], nums[i]);
    }

    return op;
  }
}

void main(List<String> args) {
  final Stopwatch stopwatch = new Stopwatch()..start();
  print(Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]));
  print("Time elapsed: ${stopwatch.elapsedMilliseconds}");
}
