def braces(values):

    openBracks = ["[","{","("]
    closeBracks = ["]","}",")"]
    stk = []
    rtn = []

    for str in values:
        print(str)
        for val in str:
            if val in openBracks:
                stk.append(val)

            elif val in closeBracks:
                brackNum = closeBracks.index(val)
                if ((len(stk) > 0) and (openBracks[brackNum] == stk[len(stk)-1])):
                    stk.pop()
                else:
                     rtn.append("NO")
                     break
        if len(stk) == 0:
            rtn.append("YES")
        stk = []

    return rtn

print(braces(["{]", "[}"]))
