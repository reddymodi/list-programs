n=list(map(int,input("enter te list:").split()))
k={}
for i in n:
    if i%2 != 0 :
        c = n.count(i)
        k[i]=c
for i,v in k.items():
    print(i,"repeates in",v)
    