class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.Precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"  # return something to indicate error

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()  # Return True if the character is an operand (letter)

    def notGreater(self, i):
        try:
            a = self.Precedence[i]
            b = self.Precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False  # If the operator is not in Precedence dictionary

    def infix_to_postfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':  # Left parenthesis, just push to stack
                self.push(i)
            elif i == ')':  # Right parenthesis, pop till '('
                while not self.isEmpty() and self.peek() != '(':
                    self.output.append(self.pop())
                if not self.isEmpty() and self.peek() != '(':
                    return -1  # Invalid expression (mismatched parentheses)
                else:
                    self.pop()  # Pop '('
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)
        
        while not self.isEmpty():  # Pop all remaining operators from stack
            self.output.append(self.pop())

        # Print the output postfix expression
        for ch in self.output:
            print(ch, end="")

# Main function
if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    obj = Conversion(len(exp))
    obj.infix_to_postfix(exp)