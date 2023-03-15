import sys

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()
    for token in reversed(tokens):
        if token.isdigit():
            stack.push(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if operand1 is None or operand2 is None:
                return None
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    return None
                stack.push(operand1 / operand2)
            else:
                return None
    if stack.is_empty():
        return None
    return stack.pop()

# def main():
#     sample1="(+ 1 5)"
#     sample2="(* (+ 1 5) 2)"
#     sample3 = "(- (* 1 3) (/ 6 (+ 1 2)))"
#     print(evaluate(sample1))  # 6
#     print(evaluate(sample2))  # 12
#     print(evaluate(sample3))  # 1


# if __name__ == "__main__":
#     main()