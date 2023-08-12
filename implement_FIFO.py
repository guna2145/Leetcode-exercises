
class FQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, int):
        self.queue.append(int)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("The Queue is Empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("The Queue is Empty")

    def is_empty(self):
        return self.queue.__len__ == 0
    
    def size(self):
        return len(self.queue)
    
obj = FQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.is_empty())
print(obj.size())