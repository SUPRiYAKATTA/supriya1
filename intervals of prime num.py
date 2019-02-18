L,U=input().split()
L=int(L)
U=int(U)
for i in range(L+1,U):
    if(i>1):
        for j in range(2,i):
            if((i%j)==0):
                break
            else:
                print(i,end="")
