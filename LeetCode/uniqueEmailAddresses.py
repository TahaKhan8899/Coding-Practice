class Solution:
    def numUniqueEmails(self, emails):

        sendToDict = {}
        for email in emails:
            print(email)
            cleanEmail(email)


def cleanEmail(email):
    cleanedEmail = ""
    for i in range(0, len(email)):

        # take the '.' out of the string
        if email[i] == '.':
            subString = email[:i]
            # print(subString)
            cleanedEmail += subString
        elif email[i] == '+':
            indexOfAt = email.find('@')
            # ignore everything after the + to the @
            subString = email[indexOfAt:]
            cleanedEmail += subString
            break
    print(cleanedEmail)


obj = Solution()
emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
obj.numUniqueEmails(emails)
