def solution(A):
    # write your code in Python 3.6

    turbCounts = []
    turb = 1

    if len(A) == 1:
        return turb

    #go through array, if there is a difference
    for i in range(0, len(A)-1):
        if (i == len(A)-2):
            if A[i] > A[i+1] or A[i] < A[i+1]:
                turb += 1
                turbCounts.append(turb)
                break
        #check case 1
        elif A[i] > A[i+1]:
            turb += 1
            if A[i+1] > A[i+2]:
                turbCounts.append(turb)
                turb = 1

        #check case 2
        elif A[i] < A[i+1]:
            turb += 1
            if A[i+1] < A[i+2]:
                turbCounts.append(turb)
                turb = 1

        elif A[i] == A[i+1]:
            turbCounts.append(turb)
            turb = 1

        #check outliers

    #find max turbulence
    max = turbCounts[0]
    for i in range(0, len(turbCounts)):
        if turbCounts[i] > max:
            max = turbCounts[i]

    print(turbCounts)
    print(max)

solution([9, 4, 2, 10, 7, 8, 8, 1, 9])
solution([50,150,50,150])
