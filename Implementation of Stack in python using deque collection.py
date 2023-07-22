# Implementation of Stack in python using deque collection

from collections import deque;

stack = deque()

stack.append("Rahul");
stack.append("Suresh");
stack.append("Borkar");

print('size of the stack is ', len(stack));
print('Top element : ', stack[-1]);


print('stack Element');

while stack:
    print(stack[-1])
    stack.pop();

 

