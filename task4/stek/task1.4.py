class task4:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move_in_to_out()
        return self.out_stack.pop()

    def peek(self):
        self.move_in_to_out()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def move_in_to_out(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
myQueue = task4()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
