**QUESTION**
147. Implement Queue using Arrays
Implement a First-In-First-Out (FIFO) queue using an array. The implemented queue should support the following operations: push, peek, pop, and isEmpty.
Implement the ArrayQueue class:
void push(int x): Adds element x to the end of the queue.
int pop(): Removes and returns the front element of the queue.
int peek(): Returns the front element of the queue without removing it.
boolean isEmpty(): Returns true if the queue is empty, false otherwise.

**CODE**
class ArrayQueue:
    def __init__(self):
        self.queue=[]
    def push(self, x):
        return self.queue.append(x)
    def pop(self):
        if self.queue==[]:
            return 0
        a=self.queue[::-1]
        z=a.pop()
        self.queue=a[::-1]
        return z
    def peek(self):
        if self.queue==[]:
            return 0
        return self.queue[0]
    def isEmpty(self):
        if self.queue==[]:
            return True
        else:
            return False
