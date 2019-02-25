r,s=map(str,input().split())
t=0
for x in range(0,len(r)):
    if((ord(r[x])-ord(r[x-1]))!=(ord(s[x])-ord(s[x-1]))):
        t=t+1
if(t>0):
    print("no")
else:
    print("yes")
