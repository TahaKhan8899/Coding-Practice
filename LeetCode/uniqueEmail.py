class Solution:
    def numUniqueEmails(self, emails):

        emailsSeen = {}

        for email in emails:
            # format email
            formattedEmail = formatEmail(email)

            if emailsSeen.get(formattedEmail):
                emailsSeen[formattedEmail] += 1
            else:
                emailsSeen[formattedEmail] = 1
            
        return len(emailsSeen)



            # see if it has been seen before

def formatEmail(email):

    splitEmail = email.split('@')[0]

    splitEmail = splitEmail.split('.')

    splitEmail = ''.join(splitEmail)


    splitEmail = splitEmail.split('+')[0]


    splitEmail += '@' + email.split('@')[1]


    return splitEmail



        

obj = Solution()
emails = ["test.email+alex+uzair@leetcode.com","test.e.mai.l+bob.cathy@l.eetcode.com","testemail+david@lee.tcode.com"]
print(obj.numUniqueEmails(emails))