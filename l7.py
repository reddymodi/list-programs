n=list(map(int,input("enter ur list:").split()))
k={}
for i in n:
    c = n.count(i)
    k[i] = c 
for i,v in k.items():
    print(i," is repeted in",v,"times")