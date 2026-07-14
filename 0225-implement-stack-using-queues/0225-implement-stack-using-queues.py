class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        q_size=len(self.q)
        for i in range(q_size-1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q)==0
        