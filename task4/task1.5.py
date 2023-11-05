def task5(s):
    stack = []
    current_num = 0
    current_string = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string, current_num = '', 0
        elif char == ']':
            last_string, num = stack.pop()
            current_string = last_string + num * current_string
        else:
            current_string += char
    return current_string

print(task5("3[a]2[bc]"))
print(task5("3[a2[c]]"))
print(task5("2[abc]3[cd]ef")) 
