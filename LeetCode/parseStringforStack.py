def solution(S):

    commands = S.split()
    updatedCommands = []
    stk = []

    #update the types of the commands
    for command in commands:
        if command.isdigit():
            updatedCommands.append(int(command))
        else:
            updatedCommands.append((command))

    for command in updatedCommands:

        if isinstance(command, int):
            stk.append(command)

        elif command == "DUP":
            if len(stk) > 0:
                item = stk[len(stk)-1]
                stk.append(item)

        elif command == "POP":
            stk.pop()

        elif command == "+":
            if len(stk) < 2:
                return -1
            else:
                num = stk[len(stk)-1] + stk[len(stk)-2]
                stk.pop()
                stk.pop()
                stk.append(num)

        elif command == "-":
            if len(stk) < 2:
                return -1
            else:
                num = stk[len(stk)-1] - stk[len(stk)-2]
                if num < 0:
                    return -1
                else:
                    stk.pop()
                    stk.pop()
                    stk.append(num)

    if len(stk) > 0:
        return (stk[len(stk)-1])
    else:
        return 0

print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))
