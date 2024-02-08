"""

# (garbage collection)
Python is a high-level language and we don’t have to do the memory management manually.
Python garbage collection algorithm is very useful to open up space in the memory.
Garbage collection is implemented in Python in two ways: reference counting and generational.
When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately.
If you have a cycle, reference count doesn’t reach zero, you wait for the generational garbage collection algorithm to run and
clean the object.

"""