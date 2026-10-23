a=int(input())
v=0
b=input()
c=b.split(',')
for i in range(len(c)):
    if int(c[i])%10==4 and int(c[i])%6==0:
        v+=int(c[i])
print(v)
