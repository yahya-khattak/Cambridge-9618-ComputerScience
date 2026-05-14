from typing import List

DEFAULT_SIZE = 10



class Queue:
    Size: int
    MaximumSize: int
    Tail: int
    Head: int
    Array: List[any]

    def __init__(self, Size=DEFAULT_SIZE):
        self.Size = 0
        self.MaximumSize = Size
        self.Tail = 0
        self.Head = 0
        self.Array = [ None ] * Size

    def Peek(self):
        return self.Array[self.Head]
    
    def Enqueue(self, Element: any):
        if (self.Size >= self.MaximumSize):
            return
        
        self.Array[self.Tail] = Element

        self.Tail = ( self.Tail + 1 ) % self.MaximumSize
        self.Size += 1

    def Dequeue(self):
        if (self.Size == 0):
            return None
        
        Element = self.Array[self.Head]

        self.Array[self.Head] = None
        self.Head = ( self.Head + 1 ) % self.MaximumSize
        self.Size -= 1

        return Element


def Main():
    MyQueue = Queue()

    MyQueue.Enqueue("G")
    MyQueue.Enqueue("F")
    MyQueue.Enqueue("C")

    print( MyQueue.Peek() )

    print( MyQueue.Dequeue() )
    print( MyQueue.Dequeue() )
    print( MyQueue.Dequeue() )

Main()