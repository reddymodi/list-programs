n=list(input("enter the list").split())
k = input("enter the word:")
m = int(input("enter the occurance"))
c =[]
count =0 
for i in n:
    if i == k:
        count += 1
        if(count != m):
            c.append(i)
    else:
        c.append(i)
if count == 0:
    print("item not found")
else:
    print("upfated list is:",c)
        