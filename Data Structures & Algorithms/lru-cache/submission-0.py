class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

        self.cap = capacity
        self.cache = {}


    # the key is the node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]



    def insert(self, node) -> None:
        # leftmost is left
        nxt = self.left.next
        nxt.prev = node
        self.left.next = node

        # sort the nxt node
        node.next = nxt
        node.prev = self.left
        return

    def remove(self, node) -> None:
        prev = node.prev
        nxt = node.next
        # 
        node.prev.next = nxt
        nxt.prev = prev
        # 
        
