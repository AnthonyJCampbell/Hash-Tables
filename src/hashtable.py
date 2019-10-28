# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Get the hashed key for storage
        index = self._hash_mod(key)
        print(f"our index is {index} with key {key}")

        # Check if we've reached capacity
        # If there's already a value at the calculated index, we should resize
        if self.storage[index] is not None:
            # If so, resize first
            self.resize()

        print(key)
        print(value)
        print("")

        # Store the real key and value in the LinkedPair and insert it at the given index
        self.storage[index] = LinkedPair(key, value)
        print(self.storage[index].key)
        print(self.storage[index].value)
        print("")


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # retrieve _hash_mod of key
        index = self._hash_mod(key)

        # Check if self.storage[_hash_mod] has a value
        if self.storage[index] is not None:
            return self.storage[index].value 

        # Else, return None
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # set self.capacity to *= 2
        self.capacity *= 2
        
        # Declare storage with double the capacity
        new_storage = [None] * self.capacity

        for item in self.storage:
            # If nothing's at the given index, we don't have to rehash it.
            if item.key is None:
                pass

            # Rehash the key
            new_hash = self._hash_mod(item.key)

            # Place the LinkedPair at the correct index
            new_storage[new_hash] = item

        self.storage = new_storage

ht = HashTable(5)
ht.retrieve(17)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
