n=list(map(int,input("enter ur list: ").split()))
k=sorted(n)
e=[]
o=[]
for i in k:
    if i%2==0:
        e += [i]
    else:
        o += [i]
print("enter even list:",e)
print("enter odd list:",o)