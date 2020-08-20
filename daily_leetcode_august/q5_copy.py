class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        currentNode = self
        for char in word:
            charIndex = ord(char) - ord('a')
            if currentNode.children[charIndex] is None:
                currentNode.children[charIndex] = WordDictionary()
            currentNode = currentNode.children[charIndex]

        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for child in currentNode.children:
                    if child is not None and child.search(word[i + 1:]):
                        return True
                return False

            charIndex = ord(char) - ord('a')
            if currentNode.children[charIndex] is None:
                return False
            currentNode = currentNode.children[charIndex]

        return currentNode is not None and currentNode.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
