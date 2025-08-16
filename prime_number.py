num = int(input("Enter a number: "))

if num <= 1:
    print("The Number Is Not Prime!")

else:
    for i in range(2,num):
        if (num % i) == 0:
            print("The Number Is Not Prime!")
            break
    else:
        print("The Number Is Prime!")

''' 

the number which is devided by 1 and itself only 
is prime number.
otherwise it is not prime number.

prime number : 7
      7 have only two factors 1 and 7.

Not prime number : 8
      8 have factors 1, 2, 4, and 8.

'''