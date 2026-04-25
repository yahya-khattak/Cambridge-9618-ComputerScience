DEFAULT_SIZE = 10

class Queue:
    def __init__(self):
        self.Size = 0
        self.Head = 0
        self.Tail = 0
        self.Array = [None] * DEFAULT_SIZE

    def Peek(self):
        return self.Array[self.Head]
    
    def Enqueue(self, Data):
        if (self.Size >= DEFAULT_SIZE):
            return
        
        self.Array[self.Head] = Data

        self.Head = (self.Head + 1) % DEFAULT_SIZE
        self.Size += 1

    def Dequeue(self):
        if (self.Size == 0):
            return
        
        Value = self.Array[self.Tail]

        self.Tail = (self.Tail + 1) % DEFAULT_SIZE
        self.Size -= 1

        return Value
    


def Main():
    MyQueue = Queue()

    MyQueue.Enqueue("G")
    MyQueue.Enqueue("F")
    MyQueue.Enqueue("C")

    print( MyQueue.Dequeue() )
    print( MyQueue.Dequeue() )
    print( MyQueue.Dequeue() )

Main()