## 380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

- insert(val): Inserts an item val to the set if not already present.
- remove(val): Removes an item val from the set if present.
- getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

### Thinking
Obviously it's a set(hashtable) to support O(1) insert and remove. That is: O(1) access by value.
But O(1) GetRandom needs random access, so there should be a vector. 

Using resizable array, the vector.pushback() is O(1) but remove a random element is O(n) 
since the left elements on the right need to be moved.

And I get a hint online. It only needs getRandom() but not access by index, 
the elements in vector don't need to be "right" order.
