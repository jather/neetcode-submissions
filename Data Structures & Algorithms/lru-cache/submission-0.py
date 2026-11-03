class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key, node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def insert(self, node):
        next = self.left.next
        prev = self.left
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev, node.next = None, None

    def get(self, key: int) -> int:
        if key in self.cache:
            val_node = self.cache[key]
            self.remove(val_node)
            self.insert(val_node)
            return val_node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(Node(key, value))
        self.cache[key] = self.left.next
        if len(self.cache) > self.capacity:
            del self.cache[self.right.prev.key]
            self.remove(self.right.prev)

        
        
