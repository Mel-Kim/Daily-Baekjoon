count=int(input())  # 전체 받아오는 숫자의 개수
num=list(map(int,input().split(' ')))  # 여러 개의 숫자를 한 번에 받아오는 방법
prime=0  # 전체 소수의 개수

for i in num:
    total=0  # 리스트 안의 숫자가 1부터 자기자신까지 나누어 떨어지는 경우의 수
    for j in range(1,i+1):
        if i % j == 0: 
            total+=1
    if total == 2:  # 1과 자기자신으로만 나누어진다면 소수
        prime+=1
print(prime)
    
# 소수: 1과 자기자신으로만 나누어지는 수
