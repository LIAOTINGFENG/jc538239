sum=0
with open("number.txt","r") as f:
    for ls in f.readlines():
        sum+=int(ls)
    print("The result is",sum)