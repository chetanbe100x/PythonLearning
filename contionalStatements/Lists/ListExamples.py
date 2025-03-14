mylist=["Chetan","patel",9]
for i in mylist:
    print(i)

mylist.append("Hello")
print(mylist)

newlist=[x**2 for x in range(0,10) if x%2==0]
print(newlist)