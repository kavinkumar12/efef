n=int(input())
l=list(map(int,input().split()))
mi=max(l)
a,b=0,0
for i in range(0,len(l)-1):
   for j in range(i+1,len(l)):
     if abs(l[i]+l[j])<mi:
       a,b=l[i],l[j]
        mi=abs(a+b)
print(a,b)
