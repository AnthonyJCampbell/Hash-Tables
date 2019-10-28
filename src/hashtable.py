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
            while current_item.next is not None:
                # Move over to the right and reloop
                current_item = current_item.next

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

        # If passed in a key with no value present, return none
        if current_item is None:
            return None
        
        # If the desired key is the first in our LinkedPairs
        if current_item.key == key:
            # If there is a next, we need to change current to current.next
            if current_item.next:
                self.storage[index] = current_item.next
            # If there's no `next`, we're free to delete it
            else:
                self.storage[index] = None

            # We'll return the value
            return current_item.value

        # If there's a .next and .next.key is not our key, we need to move to current.next
        while current_item.next and current_item.next.key != key:
            current_item = current_item.next

        old_val = current_item.next
        current_item.next = old_val.next
        return old_val.value


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # retrieve _hash_mod of key
        index = self._hash_mod(key)
        # Set item to be the Object at the index
        current_item = self.storage[index]

        # If current_item is None, there's no value at the key and we should return None
        if current_item is None:
            return None

        # Move through all `.next` of current_item until we find the designated key
        while current_item.key is not key:
            # If current_item.next is None, we haven't found it
            if current_item.next is None:
                return None
            # else current_item is item.next
            else:
                current_item = current_item.next

        return current_item.value







        # # If nothing's there, return None
        # if item is None:
        #     return None
        # else:
        #     return item.value


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
