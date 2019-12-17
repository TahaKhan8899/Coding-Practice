class Solution:
    def isValid(self, s):

        stk = []
        print(s)

        openParens = ['(', '[', '{']
        closedParens = [')', ']', '}']

        for char in s:
            print("stk ", stk)

            if char in closedParens:
                brackIndex = closedParens.index(char)
                if len(stk) >= 1:
                    if stk[len(stk)-1] == openParens[brackIndex]:
                        print("pair found, popping")
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            else:
                print("appending", char)
                stk.append(char)
        
        if len(stk) == 0:
            return True
        else:
            return False
        
obj = Solution()
s = "[]"
ans = obj.isValid(s)
print(ans)