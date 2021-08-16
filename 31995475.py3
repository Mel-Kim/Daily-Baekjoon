import sys
n = int(sys.stdin.readline())  # 명령의 수
stack = []

for _ in range(n):
    name = sys.stdin.readline().split()  # split으로 order받기
    order = name[0]  # order 하나씩 실행
    
    if order == "push": # 정수 x를 스택에 넣는 연산
        value = name[1]
        stack.append(value)
        
    elif order == "pop":  # 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력, 스택에 정수가 없는 경우 -1 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif order == "size":  # 스택에 들어있는 정수의 개수를 출력
        print(len(stack))
        
    elif order == "empty": # 스택이 비었으면 1, 아니면 0 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order == "top": # 스택의 가장 위에 있는 정수 출력, 스택에 정수가 없는 경우 -1 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])