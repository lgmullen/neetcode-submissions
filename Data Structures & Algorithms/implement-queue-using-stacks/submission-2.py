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
        while len(self.stackA) > 1:
            print(self.stackA)
            self.stackB.append(self.stackA.pop())
        result = self.stackA.pop()
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        return result
        

    def peek(self) -> int:
        while len(self.stackA) > 1:
            print(self.stackA)
            self.stackB.append(self.stackA.pop())
        res = self.stackA.pop()
        self.stackB.append(res)
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        return res

        

    def empty(self) -> bool:
        print(self.stackA)
        return len(self.stackA) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()