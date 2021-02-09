num=int(input())

for i in range(num):
    floor=int(input())
    ho=int(input())
    f0=[x for x in range(1, ho+1)] # 0층 리스트
    for j in range(floor): # 층
        for k in range(1,ho): # 호
            f0[k]+=f0[k-1]
    print(f0[-1])
