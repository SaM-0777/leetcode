class Solution {
  List<int> decode(List<int> encoded, int first) {
    List<int> op = [];
    op.add(first);

    for (int i = 0; i < encoded.length; i++) {
      op.add(encoded[i] ^ op[i]);
    }

    return op;
  }
}

void main(List<String> args) {
  final Stopwatch stopwatch = new Stopwatch()..start();
  print(Solution().decode([1, 2, 3], 1));
  print("Time elapsed: ${stopwatch.elapsedMilliseconds}");
}
