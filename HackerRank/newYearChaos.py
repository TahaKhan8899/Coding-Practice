def minimumBribes(q):
    q = [0] + q
    totalBribes = 0
    for i in range(1, len(q)):
        currPos = i
        startingPos = q[i]
        if currPos == startingPos:
            continue
        elif currPos < startingPos:
            bribes = startingPos - currPos
            if bribes <= 2:
                totalBribes += bribes
                continue
            else:
                return "Too chaotic"
    return totalBribes

# BLAGH I HATE THIS QUESTION.


print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4
                     ]))
