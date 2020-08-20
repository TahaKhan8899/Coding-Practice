class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        group = [0] * num_people
        give = 1
        haveCandiesLeft = True
        while haveCandiesLeft:
            for i in range(0, len(group)):
                print(group)
                if candies - give > 0:
                    group[i] += give
                    candies -= give
                else:
                    group[i] += candies
                    haveCandiesLeft = False
                    break
                give += 1
        return group


obj = Solution()
ans = obj.distributeCandies(7, 4)
print(ans)
