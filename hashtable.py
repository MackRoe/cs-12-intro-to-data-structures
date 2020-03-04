# ! python hashtable.py starter code

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        print(self.buckets)
        for bucket in self.buckets:
            print(bucket.items())
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n). Reason: Python must step through each
        key value pair in order to collect node data."""
        hash_values = []

        for bucket in self.buckets:
            # Loop through all buckets √
            for key, value in bucket.items():
                # Collect all values in each bucket √
                hash_values.append(value)
        return hash_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""

        # initialize bucket count variable
        bucket_count = 0
        # TODO: Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            bucket_count += bucket.length()
        return bucket_count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        # check if bucket has key/value pair
        result = bucket.find(lambda item: item[0] == key)

        if result:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        # check if bucket has key/value pair
        result = bucket.find(lambda item: item[0] == key)

        if result:
            # If found, return value associated with given key
            return result[1]
        else:
            # Otherwise, raise error to tell user get failed
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        # check if bucket has key/value pair
        result = bucket.find(lambda item: item[0] == key)

        if result == None:
            bucket.append((key, value))
        else:
            bucket.delete(result)
            bucket.append((key, value))
        # for bucket in self.buckets:
        #     # Check if key-value entry exists in bucket
        #     for bucket_key, bucket_value in bucket.items():
        #         if bucket_key == key:
        #             # If found, update value associated with given key
        #             # and insert given key-value entry into bucket
        #             # TODO:
        #             # -- use LinkedList methods by way of self.buckets --
        #             bucket_value = value
        #             print()
        #             print("> Set Method Action Completed <")
        #             print()

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]

        # check if bucket has key/value pair
        result = bucket.find(lambda item: item[0] == key)
        if result:
            # If found, delete entry associated with given key
            bucket.delete(result)
            print("> Delete Method Action Completed <")
        else:
            # Otherwise, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
