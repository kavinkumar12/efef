u,v=input().split()
P=0
for i in range(int(u),int(v)+1):
    S=1
    N=0
    while S<=i:
        if i%S==0:
            N+=1
        S+=1
    if N==2:
        P+=1
print(P)
