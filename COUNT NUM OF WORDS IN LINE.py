y=input()
count=1
for x in range(0,len(y)):
    if(y[x]==" "):
        count=count+1
    else:
        count=count
print(count)
