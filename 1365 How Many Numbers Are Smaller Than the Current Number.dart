class Solution {
  List<int> smallerNumbersThanCurrent(List<int> nums) {
    List<int> op = [];

    for (int i = 0; i < nums.length; i++) {
      int count = 0;
      for (int j = 0; j < nums.length; j++) {
        if (i != j && nums[j] < nums[i]) {
          count++;
        }
      }
      op.add(count);
    }
    return op;
  }
}

void main(List<String> args) {
  final Stopwatch stopwatch = new Stopwatch()..start();
  print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]));
  print("Time elapsed: ${stopwatch.elapsed.inMilliseconds}");
}
