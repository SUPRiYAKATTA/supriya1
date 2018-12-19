A=int(raw_input())
b=A%10
e=A/10
c=e%10
d=e/10
x=b**3+c**3+d**3
if(x==A):
	print("armstrong number")
else:
	print("not an armstrong number")
