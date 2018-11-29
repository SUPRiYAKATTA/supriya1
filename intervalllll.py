a,c=map(int,input().split(' '))
for i in range(a+1,c):
	if i%2!=0:
	    if i<(c-2):
	        print(i,end=' ')
	    else:
	        print(i,end='')
