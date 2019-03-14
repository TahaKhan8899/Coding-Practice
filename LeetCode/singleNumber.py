class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #loop through list and increase count in dictionary for that element

        #create dictionary
        dict = {}

        for key in nums:
            if key in dict:
                del dict[key]
            else:
                dict[key] = 1

        return dict.keys()[0]


obj = Solution()
print(obj.singleNumber([2,2,1]))
