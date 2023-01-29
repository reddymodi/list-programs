n=list(map(int,(input("enter ur list:").split())))
l = int(len(n))
total = 0
for i in n:
    total += i
avg = total/l
print("avarage:",avg)