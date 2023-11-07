def task6(tokens):
    stack = []
    
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(float(left) / right))
    return stack.pop()

print(task6(["2", "1", "+", "3", "*"]))
print(task6(["4", "13", "5", "/", "+"]))
print(task6(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
