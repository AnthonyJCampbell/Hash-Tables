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

        # If there's nothing at the intended index, we're good to go!
        if self.storage[index] is None:
            # Store the real key and value in the LinkedPair and insert it at the given index
            self.storage[index] = LinkedPair(key, value)

        # If something's there
        else:
            print("Collision detected!")
            # Store item that's currently at the index
            current_item = self.storage[index]
            # Loop over the .next of the item in place until you reach the end
            while item.next is not None:
                # Move over to the right and reloop
                current_item = item.next

            if current_item.key == key:
                current_item.value = value
            else:
                current_item.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # Store item that's currently at the index.
        current_item = self.storage[index]


        if self.storage[index] is None:
            print("There's nothing here.")
            return
        self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # retrieve _hash_mod of key
        index = self._hash_mod(key)
        # Set item to be the Object at the index
        item = self.storage[index]

        # If nothing's there, return None
        if item is None:
            return None
        else:
            return item.value


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
            # if item is not None:
            #     print(item.value)
            # If nothing's at the given index, we don't have to do anything
            if item is None:
                continue
            else:
                # Rehash the key
                new_hash = self._hash_mod(item.key)
                # Place the LinkedPair at the correct index
                new_storage[new_hash] = item

        self.storage = new_storage
        # print(f"After resizing, our storage looks like: {self.storage}")

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
