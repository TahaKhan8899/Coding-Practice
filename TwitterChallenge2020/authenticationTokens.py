#
# Complete the 'numberOfTokens' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER expiryLimit
#  2. 2D_INTEGER_ARRAY commands
#


def numberOfTokens(expiryLimit, commands):

    activeTokens = {}
    endingTime = commands[len(commands)-1][2]
    print(endingTime)

    # Look at each command
    for cmd in commands:
        print(cmd)

        # read first command
        if cmd[0] == 0:
            # handle create token
            activeTokens = createToken(cmd, expiryLimit, activeTokens)
            print("Added: ", activeTokens)

        elif cmd[0] == 1:
            # handle reset token
            activeTokens = resetToken(cmd, expiryLimit, activeTokens)
            print("Removed: ", activeTokens)

    numActiveTokens = sum(1 for i in activeTokens.values() if i > endingTime)

    return numActiveTokens


def createToken(tkn, expiryLimit, activeTokens):

    # Token format: [command, ID, T]

    tknID = tkn[1]
    currentTime = tkn[2]

    # check if tokenID is new
    if tknID not in activeTokens:
        # set expiry time and add to activeTokens
        expiryTime = currentTime + expiryLimit
        activeTokens[tknID] = expiryTime

    return activeTokens


def resetToken(tkn, expiryLimit, activeTokens):

    tknID = tkn[1]
    currentTime = tkn[2]

    # check if token exists in the active tokens
    if tknID in activeTokens:

        # check if time has expired
        tknExpireTime = activeTokens[tknID]

        if currentTime <= tknExpireTime:
            # reset tkn timer
            activeTokens[tknID] += expiryLimit

        # time expired, delete token
        else:
            del activeTokens[tknID]

    return activeTokens


expiryLimit = 1
commands = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]
ans = numberOfTokens(expiryLimit, commands)
print(ans)
