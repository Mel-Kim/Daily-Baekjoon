import sys
n = int(sys.stdin.readline())
ls = list(map(int,sys.stdin.readline().split()))
stack = []

result = [-1]*n

stack.append(0)
for i in range(n):
    while len(stack)!=0 and ls[stack[-1]] < ls[i]:
        result[stack.pop()] = ls[i]
    stack.append(i)
    
print(*result)