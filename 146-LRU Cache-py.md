# 146. LRU Cache

Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: ```get``` and ```put```.

```get(key)``` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

```put(key, value)``` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

**Follow up:** Could you do both operations in **O(1)** time complexity?

## Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

## Thought
Let's look at the requirements and look for data structures we need.
There should be a structure to store our data. Need get and put in O(1).
It seems like: array or hashtable.

We need to track the status of the key. Whether it's recently used. So every time when get is called, the status of that key 
needs to be changed. Moreover, we can't change the status of other data since this should be processed in O(1).

And we also need to know which one is least recently used. To track that in an array, it can only be done in O(1).

So what data structure can we use?

The best way to do put and get is by using DoubleLinkedList, it's easy to add one node to head or tail, or delete any node with only the reference to that node.

But to get the value by key, we need a hashtable.

## Solution
```python
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
        
class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add_node(self, node):
        """
        Always add the new node right after head
        """
        node.prev = self.head
        node.next = self.head.next
        
        node.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        """
        Remove an existing node
        """
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _move_to_head(self, node):
        """
        move a node next to head
        """
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        """
        Pop current tail(prev of tail
        """
        res = self.tail.prev
        self._remove_node(res)
        return res
    
    def put(self, key, value):
        node = self.cache.get(key)
        
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                ans = self._pop_tail()
                del self.cache[ans.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
            
    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
