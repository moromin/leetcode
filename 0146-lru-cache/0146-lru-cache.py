class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def moveToHead(self, node):
        self.remove(node)
        self.add(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = dict()
        self.list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        else:
            self.list.moveToHead(self.keyToNode[key])
            return self.keyToNode[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.keyToNode[key].value = value
            self.list.moveToHead(self.keyToNode[key])
            
        else:
            new = Node(key, value)
            self.keyToNode[key] = new
            self.list.add(new)
            
            if len(self.keyToNode) > self.capacity:
                del self.keyToNode[self.list.tail.prev.key]
                self.list.remove(self.list.tail.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)