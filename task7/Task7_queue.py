    """
    Class queue implementation
    """

class Queue:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def push(self,x):
        self.second.put(x)
    def take(self, first, second):        
        temp=second._stack[0]
        TEMP=first.take()
        first.put(temp)
        arr=[]
        for i in range(1,len(second._stack)):
            arr.append(second._stack[i])
        second._stack=arr
        return TEMP