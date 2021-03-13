class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.reco = [-1] * 10000

    def find(self, key: int) -> int:
        loc = key % 8003
        while self.reco[loc] != key and self.reco[loc] != -1:
            loc += 1
        return loc

    def add(self, key: int) -> None:
        l = self.find(key)
        if self.reco[l] == -1:
            self.reco[l] = key


    def remove(self, key: int) -> None:
        l = self.find(key)
        if self.reco[l] == key:
            self.reco[l] = -2

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        return self.reco[self.find(key)] == key



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
