s,r=map(int,input().split())
l=[]
count=0
if(s<=2<=r):
        l.append(2)
        count=count+1
if(s<=3<=r):
        l.append(3)
        count=count+1
if(s<=5<=r):
        l.append(5)
        count=count+1
if(s<=7<=r):
        l.append(7)
        count=count+1
for x in range(s,r+1):
    if(x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0):
        l.append(x)
        count=count+1
print(count)
