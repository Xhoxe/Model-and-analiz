def reverse_string(s: str, index=None) -> None:
    if index is None:
        index = len(s) - 1
    if index >= 0:
        print(s[index], end="")
        reverse_string(s, index - 1)
    else:
        print()
        
# Приклад використання
reverse_string("apple")
