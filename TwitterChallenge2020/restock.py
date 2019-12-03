#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#


def restock(itemCount, target):

    purchased = 0
    diff = 0
    for i in range(len(itemCount)):
        purchased += itemCount[i]
        print(purchased)

        if purchased > target or purchased == target:
            diff = purchased - target
            break
        elif (purchased < target) and (i == len(itemCount)-1):
            diff = target - purchased

    return diff


itemsCount = [1]
target = 1
ans = restock(itemsCount, target)
print(ans)
