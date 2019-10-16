class Solution(object):
  def compress(self, chars):
    
      for charIndex in range(len(chars)):

        if charIndex <= len(chars):
            if chars[charIndex] != chars[charIndex+1]:
                continue
            else:
                newIndex = charIndex
                count = 0
                while chars[newIndex] == chars[newIndex+1]:
                    count += 1
                    newIndex += 1
                
                chars[charIndex+1] = count+1

Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# ['a', 'a', 'a', 'b', 'c', '3', 'c']
# ['a', '3', 'a', 'b', 'c', '3']