num=int(input())
num_list=[]
while num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            num_list.append(i)
            num = num // i
            break
for i in num_list:
    print(i)