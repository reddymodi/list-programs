n=list(map(int,input("enter ur list:").split()))
k = []
for i in n:
    if i not in k:
        k.append(i)
print("uniqe list:",k)
        