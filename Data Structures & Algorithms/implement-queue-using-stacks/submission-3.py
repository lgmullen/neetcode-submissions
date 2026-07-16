class MyQueue:
#first in first out AxxxxxxB
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)

    #  pop should take longer?
    def pop(self) -> int:
        #basically delete stackA front and return it 
        # have pop be really slow lol 
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

        

    def peek(self) -> int:
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]

        

    def empty(self) -> bool:
        return len(self.stackB) == 0 and len(self.stackA) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()