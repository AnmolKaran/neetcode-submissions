class MyHashMap:

    def __init__(self):
            self.mine = {}

    def put(self, key: int, value: int) -> None:
        self.mine[key] = value

    def get(self, key: int) -> int:
        if key not in self.mine:
            return -1
        else:
            return self.mine[key]

    def remove(self, key: int) -> None:
        if key in self.mine:
            del self.mine[key]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)