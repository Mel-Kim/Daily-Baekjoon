#양의 정수 X의 각 자리가 등차수열을 이룬다
#1. X의 각 자리 분해하기-> nums=list(map(int, str(x)))
#2. 각 자리가 등차수열을 이루는지 
# -> 3자리 수라면 (첫번째자리 수)-(두번째자리 수) = (두번째자리 수)-(세번째자리 수)
#2.1 1부터 99까지는 모두 한수
# 1 <= X <=N 인 한수의 개수?

n=int(input())
sum=0
for x in range(1, n+1):
	if x <= 99:
		sum+=1
	else:
		nums=list(map(int,str(x)))
		if nums[0] - nums[1] == nums[1] - nums[2]:
			sum+=1
print(sum)
