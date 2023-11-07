def task7(s):
    max_length = 0
    stack = [-1]
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)
    return max_length

print(task7("(()"))
print(task7(")()())"))
print(task7("")) 
