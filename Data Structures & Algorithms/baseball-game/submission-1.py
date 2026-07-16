class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        for op in operations:
            print(op)
            if op == "+":
                one = stack[-1]
                two = stack[-2]
                stack.append(one + two)
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)