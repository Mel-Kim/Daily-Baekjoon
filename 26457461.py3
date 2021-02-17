M=int(input())
N=int(input())
prime_list=[]

for i in range(M,N+1):
	count=0
	for j in range(1, i+1):
		if i % j == 0:
			count+=1
	if count == 2:
		prime_list.append(i)
	
if len(prime_list) != 0:
	print(sum(prime_list))
	print(min(prime_list))
else:
	print(-1)