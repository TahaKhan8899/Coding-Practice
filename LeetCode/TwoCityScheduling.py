class Solution:
    def twoCitySchedCost(self, costs):
        
        # n = len(costs)/2
        # capCityA = 0
        # capCityB = 0
        # totalCost = 0

        # for person in costs:

        #     costA = person[0]
        #     costB = person[1]

        #     if costA <= costB:
        #         if capCityA < n:
        #             print("Add to A")
        #             totalCost += costA
        #             capCityA += 1
        #             continue
        #         else:
        #             print("A is full, add to B")
        #             totalCost += costB
        #             capCityB += 1
        #             continue
        #     if capCityB < n:
        #         print("Add to B")
        #         totalCost += costB
        #         capCityB += 1
        #         continue
        #     else:
        #         print("B is full, add to A")
        #         totalCost += costA
        #         capCityA += 1

        # return totalCost

        # emptyA = []
        # costsOfA = ((person[0]) for person in costs)
        # costsOfB = ((person[0]) for person in costs)
        # print(list(costsOfA))

        print("initial costs: ", costs)
        diffs = (a[1]-a[0] for a in costs)
        print("diffs: ", list(diffs))
        costs.sort(key = lambda e : e[0] - e[1])
        diffs2 = (a[1]-a[0] for a in costs)
        print("diffs2: ", list(diffs2))
        print(costs)
        n = len(costs)
        x = sum(e[0] for e in costs[:int(n/2)])
        y = sum(e[1] for e in costs[int(n/2):])
        return x + y

        # THIS QUESTION IS DUMB

obj = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
ans = obj.twoCitySchedCost(costs)
print(ans)