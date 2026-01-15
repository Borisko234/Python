# print numbers from 1 to 100
# if the number is prime, it prints "Pime"
# if the number is divisible by 3, it prints "Buzz"
# if the number is divisible by 5, it prints "Fizz"

def buzz_prime():
    for i in range(1, 101):
        # For first 3 and 5 Buzz and Fizz
        # if i % 3 == 0:
        #     print("Buzz")
        #     continue
        # elif i % 5 == 0:
        #     print("Fizz")
        #     continue
        isPrime = True
        if i <= 1:
            isPrime = True
        elif i == 2:
            isPrime = True
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            print("Pime")
        # For first 3 and 5 Prime
        elif i % 3 == 0:
            print("Buzz")
            continue
        elif i % 5 == 0:
            print("Fizz")
            continue
        else:
            print(i)



buzz_prime()


