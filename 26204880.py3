num=int(input())

for i in range(num):
    floor=int(input())
    ho=int(input())
    f0=[x for x in range(1, ho+1)] # 0층 리스트
    for j in range(floor): # 층
        for k in range(1,ho): # 호
            f0[k]+=f0[k-1]
    print(f0[-1])
    
    #https://ooyoung.tistory.com/89
    #규칙찾는 문제가 어렵다..
    #0층 리스트를 만들어서 누적하여 합하는 방법
