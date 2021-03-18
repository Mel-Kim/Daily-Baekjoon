n=int(input())
count=0
for _ in range(n):
    word=input()
    for i in range(len(word)-1):    # 0부터 시작하니까 글자 개수는 len(word)-1
        if word[i]!=word[i+1]:      # 만약에 현재 글자가 다음 글자와 같지않다면
            if word[i] in word[i+1:]:   # 만약 그 글자가 나중에 또 나온다면
                n-=1                    # 전체 글자수 - 1
                break
print(n)
