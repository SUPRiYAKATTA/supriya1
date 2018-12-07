n,m=map(int,input().split())
l=[]
for i in range(n+1,m):
	if(i%2==0):
		l.append(i)
s=" ".join(map(str,l))
print(s)
