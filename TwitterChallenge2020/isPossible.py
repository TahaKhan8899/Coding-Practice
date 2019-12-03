#
# Complete the 'isPossible' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY calCounts
#  2. INTEGER requiredCals
#


def isPossible(calCounts, requiredCals):

    calCounts.sort()

    for i in range(0, len(calCounts)-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = {}
        curr_sum = requiredCals - calCounts[i]
        print("Required: ", requiredCals, "calCounts ",
              calCounts[i], "curr_sum: ", curr_sum)
        for j in range(i + 1, len(calCounts)):
            print("calCounts[j] = ", calCounts[j], "s = ", s)
            if (curr_sum - calCounts[j]) in s:
                print("Triplet is", calCounts[i],
                      ", ", calCounts[j], ", ", curr_sum-calCounts[j])
                return True
            s[calCounts[j]] = 1

    return False


calCounts = [3, 9, 5, 1, 6]
required = 12
ans = isPossible(calCounts, required)
print(ans)
