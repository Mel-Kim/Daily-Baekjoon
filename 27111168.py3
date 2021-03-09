num=list(range(1,10001))
remove_list=[]

for i in num:
	for j in str(i):  # 숫자 쪼개기
		i += int(j) # 생성자가 있는 숫자
	if i <= 10000:
		remove_list.append(i) # 생성자 리스트에 추가

for k in set(remove_list):
	num.remove(k) # 생성자 제거
for l in num:
	print(l)

# https://ooyoung.tistory.com/64
