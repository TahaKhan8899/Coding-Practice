def isPrime(num):
    for i in range(2, num):
        if num % i == 0 and i < num:
            return False
    return True


def countPrimes(num):

    # STRATEGY:
    # Assume all numbers are prime in isPrime (not 0 and 1)
    # go through list, if a number is prime, mark all the
    # multiple of that number as notPrime

    isPrime = [True if i > 1 else False for i in range(0, num)]
    # print(isPrime)
    for i in range(2, num):
        if (isPrime[i]):
            # print(i, " is Prime")
            for j in range(i, num, i):
                if j == i:
                    continue
                else:
                    # print(j, "is NOT prime")
                    isPrime[j] = False
            # print(isPrime)

    count = 0
    for prime in isPrime:
        if prime:
            count += 1

    return count


def test():
    for i in range(10, 30, 2):
        print(i)


print("There are ", countPrimes(10000000), " primes.")
# test()
