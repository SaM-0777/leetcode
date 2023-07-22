class Solution {
  int finalValueAfterOperations(List<String> operations) {
    int x = 0;
    for (String op in operations) {
      switch (op) {
        case "++X":
          ++x;
          break;
        case "X++":
          x++;
          break;
        case "--X":
          --x;
          break;
        case "X--":
          x--;
          break;
        default:
          break;
      }
    }

    return x;
  }
}

void main(List<String> args) {
  print(Solution().finalValueAfterOperations(["++X","++X","X++"]));
}
