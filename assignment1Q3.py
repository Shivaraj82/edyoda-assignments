n=(1,2,3,4,5,6,7,8,9)
evencount=0
oddcount=0
for i in n:
    if i%2 == 0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print("Even numbers: ",evencount)
print("odd numbers",oddcount)