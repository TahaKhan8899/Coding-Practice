class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        currentNode = self
        for node in word:
            if currentNode.children[ord(node) - ord('a')] is None:
                currentNode.children[ord(
                    node) - ord('a')] = WordDictionary()
            currentNode = currentNode.children[ord(node) - ord('a')]

        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self
        for i in range(len(word)):
            node = word[i]
            if node == '.':
                for chars in currentNode.children:
                    if chars is not None and chars.search(word[i + 1:]):
                        return True
                return False

            if currentNode.children[ord(node) - ord('a')] is None:
                return False
            currentNode = currentNode.children[ord(node) - ord('a')]

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
