from collections import deque


class task3:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

task3 = task3()
print(task3.ping(1))  
print(task3.ping(100)) 
print(task3.ping(3001))
print(task3.ping(3002))
