from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        tracker = {}

        # DS: {ID: setOfMinsInActive}

        for i in range(0, len(logs)):
            userID = logs[i][0]
            mins = logs[i][1]
            if (userID not in tracker):
                tracker[userID] = {mins}
            else:
                tracker[userID] = tracker[userID].union({mins})

        print(tracker)

        res = [0] * k
        # find UAM for each user
        for id in tracker:
            uam = len(tracker[id])
            res[uam-1] += 1

        return res
