class MyHashSet:

    def __init__(self):
        self.size = 64
        self.hashMap = [None] * self.size

    def getHash(self, key):
        keyHash = key % self.size
        return keyHash

    def add(self, key: int) -> None:
        keyHash = self.getHash(key)

        if self.hashMap[keyHash] is None:
            self.hashMap[keyHash] = [key]
        else:
            for item in self.hashMap[keyHash]:
                if item == key:
                    print("key already in list")
                    return
            self.hashMap[keyHash].append(key)

    def remove(self, key: int) -> None:
        keyHash = self.getHash(key)

        if self.hashMap[keyHash] is None:
            return
        else:
            if key in self.hashMap[keyHash]:
                self.hashMap[keyHash].remove(key)
                return
            return

    def contains(self, key: int) -> bool:
        keyHash = self.getHash(key)

        if self.hashMap[keyHash] is not None and key in self.hashMap[keyHash]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))  # returns true
print(obj.contains(3))  # returns false(not found)
obj.add(2)
print(obj.contains(2))  # returns true
obj.remove(2)
print(obj.contains(2))  # returns false(already removed)
