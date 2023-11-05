def task1(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    return -1

print(task1("leopard"))
print(task1("loveleopard")) 
print(task1("aabb"))   
