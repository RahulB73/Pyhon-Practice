# Maximum Element (Stack Problem 101)
 
from collections import deque

N = int(input())
stack = deque()
max_stack = deque()

while N:
    q, *values = map(int, input().split())

    if q == 1:
        if len(values) == 1:
            val = values[0]
            stack.append(val)
            if not max_stack or val >= max_stack[-1]:
                max_stack.append(val)
            else:
                max_stack.append(max_stack[-1])

    elif q == 2:
        if stack:
            stack.pop()
            max_stack.pop()
        else:
            print('Stack is empty, cannot pop.')

    elif q == 3:
        if max_stack:
            print(max_stack[-1])
        else:
            print('Stack is empty.')

    else:
        print('Invalid query.')

    N -= 1

        
    



