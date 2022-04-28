class MaxHeap:
    
    def __init__(self):
        self.data = [None]
        
    def insert(self, item):
        self.data.append(item)
        i = len(self.data) -1

        while i > 1:
            if self.data[i] > self.data[(i//2)]:
                self.data[i], self.data[(i//2)] = self.data[(i//2)], self.data[i]
                i = i//2
            else: break
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = 2*i
        right = (2*i) + 1
        smallest = i
        if right < len(self.data) and self.data[i] < self.data[right]:
            smallest = right if self.data[left] < self.data[right] else left
        elif left < len(self.data) and self.data[i] < self.data[left]:
            smallest = left
        
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)

maxHeap = MaxHeap()
maxHeap.insert(1)
maxHeap.insert(5)
maxHeap.insert(6)
maxHeap.insert(7)
maxHeap.insert(8)
maxHeap.insert(9)
maxHeap.insert(3)
maxHeap.insert(100)
maxHeap.insert(4)
print(maxHeap.data)
maxHeap.remove()
print(maxHeap.data)
maxHeap.remove()
print(maxHeap.data)