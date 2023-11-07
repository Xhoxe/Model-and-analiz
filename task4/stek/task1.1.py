def isValid(s: str) -> bool:
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets_map:
            top_element = stack.pop() if stack else '#'
            if brackets_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid("()"))      # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
