class MyHashMap:

    def __init__(self):
        self.hashMap = []
        

    def put(self, key: int, value: int) -> None:
        found = False
        for idx in range(len(self.hashMap)):
            if self.hashMap[idx][0] == key:
                found = True
                self.hashMap[idx][1] = value
                break

        if not found:
            self.hashMap.append([key, value])
        

    def get(self, key: int) -> int:
        for idx in range(len(self.hashMap)):
            if self.hashMap[idx][0] == key:
                return self.hashMap[idx][0]
            
        return -1
        

    def remove(self, key: int) -> None:
        for idx in range(len(self.hashMap)):
            if self.hashMap[idx][0] == key:
                self.hashMap.pop(idx)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

'''
myHashMap = MyHashMap()
print(myHashMap.hashMap)
myHashMap.put(1, 1)#The map is now [[1,1]]
print(myHashMap.hashMap)
myHashMap.put(2, 2)#The map is now [[1,1], [2,2]]
print(myHashMap.hashMap)
ret = myHashMap.get(1)#return 1, The map is now [[1,1], [2,2]]
print(ret)
ret = myHashMap.get(3)#return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(ret)
myHashMap.put(2, 1)#The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.hashMap)
ret = myHashMap.get(2)#return 1, The map is now [[1,1], [2,1]]
print(ret)
myHashMap.remove(2)#remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.hashMap)
ret = myHashMap.get(2)#return -1 (i.e., not found), The map is now [[1,1]]
print(ret)
'''

myHashMap = MyHashMap()
print(myHashMap.hashMap)
myHashMap.remove(14)
print(myHashMap.hashMap)
myHashMap.get(4)
print(myHashMap.hashMap)
myHashMap.put(7, 3)
print(myHashMap.hashMap)
myHashMap.put(11, 1)
print(myHashMap.hashMap)
myHashMap.put(12, 1)
print(myHashMap.hashMap)
ret = myHashMap.get(7)
print(ret)
myHashMap.put(1, 19)
print(myHashMap.hashMap)
myHashMap.put(0, 3)
print(myHashMap.hashMap)
myHashMap.put(1, 8)
print(myHashMap.hashMap)
myHashMap.put(2, 6)
print(myHashMap.hashMap)