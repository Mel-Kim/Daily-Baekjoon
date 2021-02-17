M=int(input())
N=int(input())
prime_list=[]  # 소수 리스트

for i in range(M,N+1): # M이상 N이하의 숫자
	count=0
	for j in range(1, i+1):
		if i % j == 0:
			count+=1
	if count == 2: # 1과 자기자신만으로 나눠지면 소수
		prime_list.append(i) # 소수인 경우 리스트에 추가
	
if len(prime_list) != 0: # M이상 N이하의 숫자 중 소수의 개수가 0이 아니라면
	print(sum(prime_list)) # 소수 전체 합 출력
	print(min(prime_list)) # 소수 중 최소값 출력
else:
	print(-1) # M이상 N이하의 숫자 중 소수의 개수가 0이라면 -1 출력
