class DynamicArray:
    
    def __init__(self, capacity: int):
        self.index = 0
        self.arr = [None] * (capacity+1)
        self.capacity = capacity


    def get(self, i: int) -> int:

        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.index:
            print("here")
            self.resize()
        self.arr[self.index] = n
        self.index += 1
        return

    def popback(self) -> int:
        temp = self.arr[self.index-1]
        self.arr[self.index-1] = None
        self.index -=1
        return temp
 

    def resize(self) -> None:
        new_arr = [None] * (self.capacity * 2)
        for i in range(self.index):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2


    def getSize(self) -> int:
        return self.index
        
    
    def getCapacity(self) -> int:
        return self.capacity
