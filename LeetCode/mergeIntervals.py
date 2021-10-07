class Solution:
    def merge(self, intervals):
        firstMergeList = []

        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals)
        print("sorted = " + str(intervals))

        firstMergeList = doMergeList(intervals)

        print("first time merged: " + str(firstMergeList))

        secondMergeList = doMergeList(firstMergeList)

        while firstMergeList != secondMergeList:
            print("first: " + str(firstMergeList) +
                  " second: " + str(secondMergeList))
            firstMergeList = secondMergeList
            secondMergeList = doMergeList(secondMergeList)

        print("final? " + str(secondMergeList))

        return secondMergeList


def doMergeList(intervals):
    mergedList = []
    i = 0
    while i < len(intervals):
        currentPair = intervals[i]
        print("currentPair: " + str(currentPair))
        j = i
        maxSecondNum = currentPair[1]
        while j < len(intervals) - 1 and intervals[j + 1][0] <= currentPair[1]:
            maxSecondNum = max(maxSecondNum, intervals[j + 1][1])
            j += 1
        if j > i:
            print("merging from index " +
                  str(intervals[i]) + " to " + str(intervals[j]))
            # mergedPairs = [currentPair[0], max(
            #     currentPair[1], intervals[j][1])]
            print("max second num is: " + str(maxSecondNum))
            mergedPairs = [currentPair[0], maxSecondNum]
            mergedList.append(mergedPairs)
            print("merged: " + str(mergedList))
            i = j + 1
        else:
            # print("just appending " + str(currentPair))
            mergedList.append(currentPair)
            i += 1
    return mergedList


l1 = [[1, 3], [8, 10], [2, 6], [15, 18]]
l2 = [[1, 4], [4, 5]]
l3 = [[1, 4]]
l4 = [[1, 4], [3, 5], [4, 10], [10, 15], [9, 20]]
l5 = [[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]]
ans = Solution().merge(l5)
print("ans is: " + str(ans))
