import 'dart:math';

class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    List<bool> op = [];

    for (int i in candies) {
      i + extraCandies >= candies.reduce(max) ? op.add(true) : op.add(false);
    }

    return op;
  }
}

void main(List<String> args) {
  print(Solution().kidsWithCandies([4,2,1,1,2], 1));
}
