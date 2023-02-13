class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        op = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                op.append("FizzBuzz")
            
            elif (i + 1) % 3 == 0:
                op.append("Fizz")
            
            elif (i + 1) % 5 == 0:
                op.append("Buzz")

            else:
                op.append(str(i + 1))

        return op


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))

