class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretList = [char for char in secret]
        guessList = [char for char in guess]
        cows = 0
        bulls = 0

        for i in range(0, len(secretList)):
            if secretList[i] == guessList[i]:
                bulls += 1
                secretList[i] = -1
                guessList[i] = -1

        print(secretList)
        print(guessList)
        for i in range(0, len(guessList)):
            print("....")
            print(i)
            print(secretList)
            print(guessList)
            if guessList[i] in secretList and guessList[i] != -1:
                print('removing: ', guessList[i])
                cows += 1
                cowIndex = secretList.index(guessList[i])
                secretList[cowIndex] = -1

        ans = str(bulls) + "A" + str(cows) + "B"

        return ans


ans = Solution().getHint("111023", "100326")
print(ans)
