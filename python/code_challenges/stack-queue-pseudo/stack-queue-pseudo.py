class PseudoQueue():
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, value):
        self.stack_1.append(value)

    def dequeue(self):
        if len(self.stack_2) == 0:
            if len(self.stack_1) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        
            while len(self.stack_1) > 0:
                last_stack_1_item = self.stack_1.pop()
                self.stack_2.append(last_stack_1_item) 

        return self.stack_2.pop()
