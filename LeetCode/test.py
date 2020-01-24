def rotateArray(a1, k):

    a2 = [0 for item in a1]

    for i in range(len(a1)):

        newIndex = i + k

        if newIndex > len(a1)-1:
            newIndex = (i+k) % len(a1)
            print("uffo: ", newIndex, "i: ", i, "k: ", k)

        a2[newIndex] = a1[i]
        print("test a2: ", a2)

    a1 = [item for item in a2]

    return a1


a1 = [1, 2, 3, 4, 5, 6]
k = 10
ans = rotateArray(a1, k)
print(ans)
