def solution(S, C):

    emailList = []
    personInfo = []
    emailDict = {}
    finalStr = ""

    #parse string S:
    s = S.split('; ')
    print(s)

    prefix = ""
    #read fname, mid(if possible) and last into an array
    for name in s:
        fullName = name.split()

        #mid name
        if len(fullName) > 2:
            c1 = fullName[0][0].lower()
            c2 = fullName[1][0].lower()
            c3 = fullName[2].lower()
            if "-" in c3:
                c3 = c3.replace("-", "")
            prefix = c1 + "_" + c2 + "_" + c3
        #no midname
        else:
            c1 = fullName[0][0].lower()
            c2 = fullName[1].lower()
            prefix = c1 + "_" + c2

        #create email and add count to dictionary
        email = prefix + "@" + C.lower() + ".com"

        #check for duplicate emails
        if email in emailDict:
            num = emailDict[email] + 1
            emailDict[email] += 1
            email = prefix + str(num) + "@" + C.lower() + ".com"
        else:
            emailDict[email] = 1

        emailList.append(email)

    for i in range(0, len(emailList)):
        if i == len(emailList) - 1:
            thing = s[i].lower() + " <" + emailList[i] + ">"
            finalStr = finalStr + thing
        else:
            thing = s[i].lower() + " <" + emailList[i] + ">; "
            finalStr = finalStr + thing

    return(finalStr)
print(solution("John Doe; Peter Parker; Mary Jane Watson-Parker; James Doe; John Elvis Doe; Jane Doe; Penny Parker", "Example"))
