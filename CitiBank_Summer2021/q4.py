# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(G):
    pointsWithChoiceR = 0
    pointsWithChoiceP = 0
    pointsWithChoiceS = 0

    for i in range(0, len(G)):
        print(G[i])

        # if he chose Rock
        if G[i] == "S":
            pointsWithChoiceR += 2
        if G[i] == "R":
            pointsWithChoiceR += 1

        # if he chose Paper
        if G[i] == "R":
            pointsWithChoiceP += 2
        if G[i] == "P":
            pointsWithChoiceP += 1

        # if he chose Scissor
        if G[i] == "P":
            pointsWithChoiceS += 2
        if G[i] == "S":
            pointsWithChoiceS += 1
    print("points with R: ", pointsWithChoiceR)
    print("points with P: ", pointsWithChoiceP)
    print("points with S: ", pointsWithChoiceS)
    return max(pointsWithChoiceR, pointsWithChoiceP, pointsWithChoiceS)


ans = solution("PPPPRRSSSSS")
print(ans)
