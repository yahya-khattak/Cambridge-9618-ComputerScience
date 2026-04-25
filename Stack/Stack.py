DEFAULT_SIZE = 15


class Stack:
    def __init__(self):
        self.Array = [None] * DEFAULT_SIZE
        self.Head = -1

    def Push(self, Data):
        if (self.Head == DEFAULT_SIZE):
            return
        
        self.Head += 1
        self.Array[self.Head] = Data

    def Pop(self):
        if (self.Head == -1):
            return None
        
        Value = self.Array[self.Head]

        self.Array[self.Head] = None
        self.Head -= 1

        return Value
    
    def GetSize(self):
        if (self.Head == -1):
            return 0
        
        # You would do TopPointer - BasePointer to get the number of elements in the stack
        # Since our BasePointer is 0 though, we just return Head + 1 (because Head starts at 0)

        return self.Head + 1;

    def Peek(self):
        if (self.Head == -1):
            return None


        return self.Array[self.Head]
    


def Main():
    MyStack = Stack()

    MyStack.Push(5)
    MyStack.Push(10)
    MyStack.Push(15)

    print( MyStack.Peek() )
    print( MyStack.GetSize() )

    print(MyStack.Pop())
    print(MyStack.Pop())
    print(MyStack.Pop())

Main()