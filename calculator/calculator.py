import math
import sys

def toPostfix(toSolve):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []
    stack = []
    for char in toSolve:
        if char == " ":
            continue
        if char.isalnum():  #operand
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop() #pop opening parentheses
        else:  #operator
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)
        

def calculator(toSolveuation):
    stack = []
    for i in toSolveuation:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            first, second = stack.pop(), stack.pop()
            stack.append(second - first)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            first, second = stack.pop(), stack.pop()
            stack.append(second / first)
        else:
            stack.append(int(i))
    return stack[-1]

if __name__ == "__main__":
    equation = sys.argv[1]
    toSolve = toPostfix(equation)
    answer = calculator(toSolve)
    print(equation + ' = ' + str(answer))