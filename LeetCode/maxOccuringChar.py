import operator
from collections import OrderedDict

def maximumOccurringCharacter(text):

    dict = OrderedDict()

    #go through string and add count for each char in a dict
    for i in range(0, len(text)):
        if text[i] in dict:
            dict[text[i]] += 1
        else:
            dict[text[i]] = 1

    maxLetter = text[0]

    for key in dict:
        if dict[key] > dict[maxLetter]:
            maxLetter = key

    print(maxLetter)
maximumOccurringCharacter("helloworld")
