class Solution {
  int maximumWealth(List<List<int>> accounts) {
    int max = -1;

    for (List l in accounts) {
      int sum = 0;
      for (int i in l) sum += i;
      if (sum > max) max = sum;
    }

    return max;
  }
}

void main() {
  print(Solution().maximumWealth([
    [1, 2, 3],
    [3, 2, 1]
  ]));
}
