num=list(range(1,10001))
remove_list=[]

for i in num:
	for j in str(i):
		i += int(j)
	if i <= 10000:
		remove_list.append(i)

for k in set(remove_list):
	num.remove(k)
for l in num:
	print(l)
