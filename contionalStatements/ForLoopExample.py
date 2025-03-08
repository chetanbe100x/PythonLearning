for i in range(1, 11):
    print(i)

str="Chetan"
for i in str:
    print(i) 

count=0
while count<10:
    print(count)
    count+=1

for i in range(0, 10):
    if i%2==0:
        continue
    print(i)

for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")