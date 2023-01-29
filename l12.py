n=list(map(int,input("enter ur list:").split()))
l = len(n)
y = n[l-1]
i = n[0]
n[0]=y
n[l-1]=i
print(n)