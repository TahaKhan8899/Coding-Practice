#
# Complete the 'maximumTotalWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER_ARRAY tasks
#  3. INTEGER p
#


def maximumTotalWeight(weights, tasks, p):

    doubleTasks = [i*2 for i in tasks]
    print(doubleTasks)

    possibleCombos = []
    maxWeight = 0

    for i in range(len(tasks)):
        # task[i] is already too long, cant do it
        if doubleTasks[i] > p:
            break
        else:
            remainingTime = p - doubleTasks[i]
            print("Remaining Time Outer: ", remainingTime)

            oneCombo = []
            taskAndIndex = {doubleTasks[i]: i}
            oneCombo.append(taskAndIndex)

            if remainingTime > 0:
                # keep processing
                # while remainingTime > 0:
                for j in range(i+1, len(doubleTasks)):
                    print("Tasks j: ", doubleTasks[j])
                    print("Remaining Time: ", remainingTime)
                    if doubleTasks[j] <= remainingTime:
                        taskAndIndex = {doubleTasks[j]: j}
                        oneCombo.append(taskAndIndex)
                        print("oneCombo: ", oneCombo)
                        remainingTime -= doubleTasks[j]
                        print("Remaining Time: ", remainingTime)
                print(oneCombo)
                possibleCombos.append(oneCombo)

            else:
                # This task takes all the time
                if weights[i] > maxWeight:
                    taskAndIndex = {doubleTasks[i]: i}
                    oneCombo.append(taskAndIndex)
                    possibleCombos.append(oneCombo)
                    maxWeight = weights[i]

    print(possibleCombos)

    # now find the max weight
    for combo in possibleCombos:

        # calculate weight of combo
        weight = 0
        for taskAndIndex in combo:
            index = list(taskAndIndex.values())[0]
            weight += weights[index]

        if weight > maxWeight:
            maxWeight = weight

    return maxWeight


weights = [1, 4, 2, 5, 3]
tasks = [2, 6, 4, 7, 1]
# weights = [10]
# tasks = [13]
p = 13
ans = maximumTotalWeight(weights, tasks, p)
print(ans)
