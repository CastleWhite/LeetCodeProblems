class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sa = []
        self.sb = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.sa.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.sb: 
            while self.sa:
                i = self.sa.pop()
                self.sb.append(i)

        return self.sb.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.sb: 
            while self.sa:
                i = self.sa.pop()
                self.sb.append(i)

        return self.sb[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.sa and not self.sb


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
