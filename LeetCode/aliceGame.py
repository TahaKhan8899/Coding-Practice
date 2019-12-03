class Solution:
    def divisorGame(self, N):

        # alice = 0 bob = 1
        player = 0
        players = ["Alice", "Bob"]

        # check if player can make a move
        while(N >= 1):
            move = chooseNum(N)

            print(players[player], ": ", "N = ", N, " Choose: ", move)

            N -= move

            if N == 1 and player == 1:
                return False
            elif N == 1 and player == 0:
                return True
            elif player == 0:
                player = 1
            else:
                player = 0


def chooseNum(N):

    maxMultiple = 1
    for i in range(1, N):
        if N % i == 0 and i > maxMultiple:
            maxMultiple = i

    return maxMultiple


obj = Solution()
winner = obj.divisorGame(4)
print("Did Alice win? ", winner)
