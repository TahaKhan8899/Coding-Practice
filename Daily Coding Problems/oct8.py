from collections import defaultdict


def chainedWords(words):
    # Fill this in.

    isAChain = True

    wordsInChain = []

    for i in range(0, len(words)):

        outterWord = words[i]
        print("Outer List: ", outterWord)

        lastLetter = outterWord[len(outterWord)-1]
        print("Last Letter: ", lastLetter)

        wordsInChainBefore = len(wordsInChain)

        for j in range(0, len(words)):
            innerWord = words[j]
            firstLetter = innerWord[0]
            print("Inner Word: ", innerWord)

            if innerWord == outterWord:
                continue
            else:
                if firstLetter == lastLetter and innerWord not in wordsInChain:
                    if i == 0 or i == 1:
                        wordsInChain.append(outterWord)
                        wordsInChain.append(innerWord)
                        print(wordsInChain)
                        break
                    else:
                        wordsInChain.append(innerWord)
                        print(wordsInChain)
                        break
                # check if the chain loops back to the first chain word
                if firstLetter == lastLetter and innerWord == wordsInChain[0]:
                    wordsInChain.append(innerWord)
                    print(wordsInChain)

        if wordsInChainBefore == len(wordsInChain):
            isAChain = False
            break

    print("Number of words in Chain: ", len(wordsInChain))
    print("Starting words size: ", len(words)+1)
    if (len(wordsInChain) != len(words)+1):
        isAChain = False

    return isAChain


answer = chainedWords(['apple', 'snack', 'karat', 'eggs', 'tuna'])
print(answer)
# True
