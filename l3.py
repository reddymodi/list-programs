n=list(map(int,input("enter ur list: ").split()))
k=sorted(n)
e=[]
o=[]
for i in k:
    if i%2==0:
        e += [i]
    else:
        o += [i]
print("even largest no:",e[len(e)-1])
print("odd largest no: ",o[len(o)-1])