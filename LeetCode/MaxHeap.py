class MaxHeap:
    def __init__(self, items=[]):

        # we don't use index 0 in a heap for easier indexing
        self.heap = [0]

        for i in items:
            self.heap.append(i)
            self.floatUp(len(self.heap)-1)
    
    # PUBLIC
    # append to the end, then float it up to the top
    def push(self, data):
        self.heap.append(data)
        self.floatUp(len(self.heap)-1)
    
    # PUBLIC
    # check is at least 1 item present, return first item
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    # PUBLIC
    def pop(self):

        # swap max to bottom, pop, it off, bubble root down 
        if len(self.heap) > 2:
            self.swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.bubbleDown(1)
        
        # only 1 value, pop it
        elif len(self.heap) == 2:
            max = self.heap.pop()
        
        # empty heap
        else:
            max = False
        return max
    
    # PRIVATE
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def floatUp(self, index):
        parent = index // 2

        # index is already at root, so no float
        if index <= 1:
            return
        # compare to parent
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)

    # PRIVATE    
    # bubble down to proper position
    def bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        # check if left is not out of range and then check if heap[largest] goes left
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        # check if left is not out of range and then check if heap[largest] goes right
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        # if a new largest was found, swap items and bubble down again
        if largest != index:
            self.swap(index, largest)
            self.bubbleDown(largest)

    # PRIVATE
    def printHeap(self):
        return(str(self.heap[0:len(self.heap)]))


# m = MaxHeap([50, 30, 20])
# m.push(5)
# print(m.printHeap())
# print(str(m.pop()))