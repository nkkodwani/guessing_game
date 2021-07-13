import math

n = int(input("Enter a number: "))
prime_numbers = [2, 3]
i = 3

if(n<1):
    print("Your number is invalid. Please try again.")

elif(1<=n<3): 
    print(f"{n}st Prime number is : {prime_numbers[n-1]}")

elif (n>2):
    while (True):
        i += 1
        status = True
        #for j in range(2, int(math.sqrt(n) + 1)): #this tests if i is prime and resets the while loop if not prime
        #for j in range(2, int(n/2 + 1)):
        for j in range(2, int(n/2 + 1)): #CHECK
            if (i % j == 0):
                status = False
                break

        if (status == True): #if the number passes the above test, it is prime. we add the number to our prime numbers list
            prime_numbers.append(i)

        if (len(prime_numbers) == n):
            print(f"The {n}th prime number is {prime_numbers[-1]}.")
            break
        
            
        
