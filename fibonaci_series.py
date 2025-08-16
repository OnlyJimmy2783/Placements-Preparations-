#take Input from user
n = int(input("Enter The Number of Terms:"))    

#Hardcoded value alredy set for a and b
a = 0  
b = 1

if n < 0:   #if n is less than 0 the value will be negative
    print("Enter The Integer Value Only")
elif n == 1:    #if n is 1 then only it will print 1 value which is 0(Zero)
    print(a)
else:
    print("Fibonaci Series:")
    for _ in range(n):  #this loop runs n times
        print(a,end=" ")    #print the current value of a and stay at same line
        a,b=b,a+b   #here a = 0 , b = 1 , 0 + 1 = 1 and so on.....