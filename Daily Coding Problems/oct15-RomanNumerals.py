class Solution():
  def romanToInt(self, s):
    
    # I = before V or X
    # X = before L or C
    # C = before D or M
    romanDict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

    chars = [char for char in s]
    print(chars)

    romanSum = 0

    for charIndex in range(len(s)-1, -1, -1):
        print(romanSum)
        
        currentRoman = s[charIndex]
        nextRoman = ''

        # if in at the end or beginnning, there is a nextRoman
        if charIndex < len(s)-1 and charIndex > -1:
            nextRoman = s[charIndex+1]

        decimal = romanDict[currentRoman] 

        print("Current:", currentRoman, "Next:", nextRoman)
        
        if currentRoman == "I" and nextRoman == "V" or currentRoman == "I" and nextRoman == "X":
            romanSum -= decimal
        elif currentRoman == "X" and nextRoman == "L" or currentRoman == "X" and nextRoman == "C":
            romanSum -= decimal
        elif currentRoman == "C" and nextRoman == "D" or currentRoman == "C" and nextRoman == "M":
            romanSum -= decimal
        else:
            romanSum += decimal
        
    return romanSum

    
n = 'II'
ans = Solution().romanToInt(n)
print(ans)
# 1910