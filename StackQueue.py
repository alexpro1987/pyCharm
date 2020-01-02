from collections import deque

letters = []

letters.append('a')
letters.append('b')
letters.append('c')

letters.append('d')

# Observing stack behavior
out = letters.pop()

print(out)
print(letters)

out = letters.pop(0)
print("Queue")
print(out)
print(letters)

numbers = deque()
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)

last = numbers.pop()
first = numbers.popleft()
print('Deck results')
print(last)
print(first)


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            print("Stack is empty")
            return None
        return self.stack.pop()

    def push(self, item):
        return self.stack.append(item)

    def size(self):
        return len(self.stack)

    def display(self):
        print('Stack: ', *self.stack)

class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        return self.stack.append(item)

    def dequeue(self):
        if len(self.stack) < 1:
            print("Empty queue")
            return None
        return self.stack.pop(0)

    def size(self):
        return len(self.stack)

    def display(self):
        print("Queue: ", *self.stack)


print("Stack example")
nums = Stack()
nums.pop()
nums.push(1)
nums.push(2)
nums.push(3)
nums.push(4)
nums.push(5)
last = nums.pop()
print('LIFO: ', last)
nums.display()
print(nums.size())

print("Queue example")
lets = Queue()

lets.dequeue()
lets.enqueue('a')
lets.enqueue('b')
lets.enqueue('c')
lets.enqueue('d')
first = lets.dequeue()
print('FIFO:', first)
lets.display()
print(lets.size())
