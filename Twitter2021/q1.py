def processLogs(logs, threshold):

    transCounts = {}
    print("herre")

    for i in range(0, len(logs)):
        transInfo = logs[i].split(" ")
        uid1 = transInfo[0]
        uid2 = transInfo[1]
        amount = transInfo[2]

        if (uid1 == uid2):
            if (uid1 not in transCounts):
                transCounts[uid1] = 1
            else:
                transCounts[uid1] += 1
        else:
            if (uid1 not in transCounts):
                transCounts[uid1] = 1
            else:
                transCounts[uid1] += 1
            if (uid2 not in transCounts):
                transCounts[uid2] = 1
            else:
                transCounts[uid2] += 1

    res = []
    print("hrere")
    for uid in transCounts:
        if transCounts[uid] >= threshold:
            print(uid)
            print(res)
            res.append(uid)

    res = sorted(res)
    print(res)
    return res


ans = processLogs(["88 99 200", "88 99 300", "99 32 100"], 2)
print(ans)
