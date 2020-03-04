# ! python linkedlist.py starter code


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item √
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        # Append node after tail, if it exists √
        else:
            if self.head is not None:
                self.tail.next = new_node

        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item √
        new_node = Node(item)
        # Prepend node before head, if it exists √
        if self.head is None:
            self.head = new_node
        else:
            self.head.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        current = self.head
        while current is not None:
            # check for match with quality() function on first node
            if quality(current.data) is not None:

                current = None
                return current.data
            elif current == self.tail:
                # check for end of linked list
                current = None
                print("Not Found")
            else:
                # otherwise, check for match with quality() on next node
                current = self.next
                if quality(current.data) is not None:

                    current = None
                    return current.data

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item √
        # Reference CREDIT:
        # https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/

        temp = self.head
        prev = None

        print(">> Delete Function Activated <<")
        print("self.head == " + str(self.head))

        if temp.data is None:
            # raise error to tell user that delete has failed √
            raise ValueError('Item not found: {}'.format(item))

        while (temp is not None):
            # Update previous node to skip around node with matching data √
            if (temp.data == item):
                # if item is found at head node
                if temp != self.tail:
                    # if not at the end of the linked list
                    print("at start of while loop, self.head = " + str(self.head))
                    print("and temp.next = " + str(temp.next))

                    # check if item is found in first node of linked list
                    if temp != self.head:
                        # found item not located at first node
                        prev.next = temp.next
                        print("after self.head=temp.next, self.head=" + str(self.head))
                        temp = None
                        print(str(item) + " deleted")
                        return
                    else:
                        # found item IS at first node
                        self.head = temp.next
                        print(str(item) + " deleted")
                        return
                else:
                    # found item is at END of linked list
                    if temp == self.head:
                        # item found at END and HEAD node
                        temp = None
                        print(str(item) + ' deleted')
                        return
                    else:
                        # found item is at END of list but NOT HEAD
                        self.tail = prev
                        prev.next = None
                        temp = None
                        print(str(item) + " deleted")
                        return
            elif temp.data != item:
                if temp == self.tail:
                    temp = None
                    prev = None
                    print(str(item) + "not in linked list.")
                    return

            # return to loop
            prev = temp
            temp = temp.next

            print('Searching.. Node pointer updated')

        print("after while loop, self.head = " + str(self.head))
        # while(temp is not None):
        #     if temp.data == item:
        #         break
        #     prev = temp
        #     temp = temp.next
        #
        # prev.next = temp.next
        #
        # temp = None

    def print_ll(self):
        print("Entering print")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    #test_linked_list()
    ll = LinkedList(['A', 'B', 'C'])

    # ll.delete('A')

    # ll.delete('C')
    ll.print_ll()
    ll.delete('B')
    ll.print_ll()
