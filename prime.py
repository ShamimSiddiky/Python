x= int(input("Enter your number: "))
count=0
if x>1:
    for i in range(2,x+1):
        if(x%i==0):
            count+=1;
    if(count==1):
        print(x, "is a prime number.")
    else:
        print(x,"is not a prime number.")
else:
    print("Change your number")

