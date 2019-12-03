# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    matches = 0

    for i in range(0, len(ar)-1):
        print(ar)
        for j in range(i+1, len(ar)):
            # check for null
            if ar[i] and ar[j]:
                # check for pair
                if ar[i] == ar[j]:
                    matches += 1
                    ar[i] = None
                    ar[j] = None
                    break

    print(matches)


sockMerchant(6, [1, 2, 1, 3, 2, 1])
