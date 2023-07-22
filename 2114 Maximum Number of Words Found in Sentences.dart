class Solution {
  int mostWordsFound(List<String> sentences) {
    int max = -1;

    for (String s in sentences) {
      int len = s.split(" ").length;
      if (len > max) max = len;
    }

    return max;
  }
}

void main(List<String> args) {
  print(Solution().mostWordsFound([
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
  ]));
}
