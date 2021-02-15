count=int(input())
num=list(map(int,input().split(' ')))
prime=0

for i in num:
    total=0
    for j in range(1,i+1):
        if i % j == 0:
            total+=1
    if total == 2:
        prime+=1
print(prime)
    
    