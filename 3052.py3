arr=[]

for i in range(10):
    a=int(input())
    arr.append(a%42)
    
arr=set(arr)
print(len(arr))

# set()함수: 집합 자료형 함수, 중복을 허락하지 않는다, 순서가 없다
# 참고: https://wikidocs.net/1015
