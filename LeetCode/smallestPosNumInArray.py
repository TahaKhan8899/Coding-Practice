def solution(A):
    A.sort()
    print(A)

    if len(A) == 1:
        if A[0] > 0:
            return (A[0]+1)
        else:
            return 1

    lowestNum = 0
    for i in range(0, len(A)-1):
        if (abs(A[i+1] - A[i]) != 1) and (abs(A[i+1] - A[i]) != 0) and A[i] > 0:
            lowestNum = A[i] + 1
            break
        elif (i == len(A)-2) and ((abs(A[i] - A[i+1]) != 0) or (abs(A[i] - A[i+1]) != 1)) and A[i] > 0:
            lowestNum = A[i+1] + 1
        elif ((i == len(A)-2) and (abs(A[i] - A[i+1]) != 0 or abs(A[i] - A[i+1]) != 1) and A[i+1] < 0):
            lowestNum = 1
    return(lowestNum)

print(solution([1]))
