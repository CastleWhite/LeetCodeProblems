class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content = 0
        self.hash = [-1] * 10010
        self.left = [-1] * 10010
        self.right = [-1] * 10010
        # self.head = -3
        # self.tail = -2
        self.left[-3], self.right[-2] = -2, -3

    def delete(self):
        least = self.right[-2]
        lr = self.right[least]
        self.right[-2], self.left[lr] = lr, -2
        self.hash[least] = -1
        self.content -= 1

    def update(self, key):
        l = self.left[key]
        r = self.right[key]
        if r != -3:
            self.left[r], self.right[l] = l, r
            re = self.left[-3]
            self.right[re], self.left[key], self.right[key], self.left[-3] = key, re, -3, key

    def get(self, key: int) -> int:
        if self.hash[key] != -1:
            self.update(key)
        return self.hash[key]

    def put(self, key: int, value: int) -> None:
        if self.hash[key] == -1:
            if self.content == self.capacity:
                self.delete()
            self.content += 1
            re = self.left[-3]
            self.right[re], self.left[-3], self.left[key], self.right[key] = key, key, re, -3
        else:
            self.update(key)
        self.hash[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
