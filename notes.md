build frequency() in class_listogram

sample in dictogram.py not working. dictogram has no attribute length

---------------------------------------------------------------------
#linkedlist.py questions
-----------------------
class Node(object) defines an object which is constructed of two parts;
the next and the data. **So, Node.next and Node.data when outside
the Node class?**

**why is the Node class not passed to the LinkedList class?**

class LinkedList(object) creates an object constructed of a .head and .tail

LinkedList.items() is what allegedly creates the linked lists
    in previous method self.head is set to None
    in items(), node is set to self.head making node equal to None
    since the while loop only executes while node is not None, it gets skipped.
    items() returns unmodified empty list
