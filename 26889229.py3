while True :
	a,b,c = map(int,input().split())
	m=max(a,b,c)
	n=min(a,b,c)

	if a+b+c == 0:
		break

	else:
	
		if (a+b+c-m-n)**2 + n**2 == m**2:
			print("right")
		else:
			print("wrong")