'''
Hash tables consist of key-value pairs like Dictionaries. 
But unlike dictionaries, hash tables use hash method/function.

We give the hash method a key from a key-value pair, called running
the key through the hash, and we'll get an address where the pair
will be stored.

Two things about hash:
One way: You can get value from a key, but not a key from a value.
Deterministic: We'll get the same address upon running the same
key through the hash method multiple times.

-- Collisions --
A collision occurs when we put a key-value pair at an address where 
there already was a key-value pair.

We can handle it by keeping both of the pairs in a list saved at the
assigned address. This is called Separate Chaining.

There is another method called Linear Probing in which in case of Collisions,
the pair won't be saved at the address, but look for another address below the
original address that isn't assigned to a pair yet. 

Linear probing is one of the many methods of Open Addressing.

We'll do Separate Chaining in our implementation.

In Separate Chaining, we can also use a linked list, instead of a list.

-- Note --
Hash Tables can have sizes. Sizes will be the number of addresses in our
hash table. Our size should always be a prime number because it increases 
the amount of randomness, hence the pairs will be distributed in a better
way reducing the amount of collisions.
'''

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key): # Hash method
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None        
    
    def keys(self):
        keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])

        return keys

ht = HashTable(7)
ht.set_item("Charizard", 90)
ht.set_item("Pikachu", 100)
ht.set_item("Noivern", 77)

print(ht.keys())