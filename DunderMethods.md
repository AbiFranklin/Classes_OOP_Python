## Dunder Methods 
Dunder methods, short for "double underscore" methods, are special methods in Python that begin and end with double underscores (`__`). They are also known as magic methods or special methods. These methods are used to define the behavior of objects for built-in operations, such as arithmetic operations, comparisons, and type conversions. Here is a list of some commonly used dunder methods, along with their explanations:

### Initialization and Representation

- **`__init__(self, ...)`**:
  - Called when an instance of a class is created.
  - Used to initialize the instance's attributes.
  - Example: `def __init__(self, name, age):`

- **`__repr__(self)`**:
  - Called by the `repr()` function and by string conversions (e.g., backticks in older versions of Python).
  - Should return a string that ideally could be used to recreate the object.
  - Example: `def __repr__(self):`

- **`__str__(self)`**:
  - Called by the `str()` function and the `print()` function.
  - Should return a readable string representation of the object.
  - Example: `def __str__(self):`

- **`__del__(self)`**:
  - Called when an instance is about to be destroyed.
  - Useful for clean-up activities, but its use is generally discouraged.
  - Example: `def __del__(self):`

### Attribute Access

- **`__getattr__(self, name)`**:
  - Called when an attribute that doesn’t exist is accessed.
  - Example: `def __getattr__(self, name):`

- **`__setattr__(self, name, value)`**:
  - Called when an attribute assignment is attempted.
  - Example: `def __setattr__(self, name, value):`

- **`__delattr__(self, name)`**:
  - Called when an attribute deletion is attempted.
  - Example: `def __delattr__(self, name):`

- **`__getattribute__(self, name)`**:
  - Called unconditionally when any attribute is accessed.
  - Example: `def __getattribute__(self, name):`

### Container Emulation

- **`__len__(self)`**:
  - Called by the `len()` function to determine the length of the object.
  - Example: `def __len__(self):`

- **`__getitem__(self, key)`**:
  - Called to retrieve an item using the indexing operator.
  - Example: `def __getitem__(self, key):`

- **`__setitem__(self, key, value)`**:
  - Called to set the value of an item using the indexing operator.
  - Example: `def __setitem__(self, key, value):`

- **`__delitem__(self, key)`**:
  - Called to delete an item using the indexing operator.
  - Example: `def __delitem__(self, key):`

- **`__iter__(self)`**:
  - Called to return an iterator for the object.
  - Example: `def __iter__(self):`

- **`__next__(self)`**:
  - Called to get the next item from the iterator.
  - Example: `def __next__(self):`

### Operator Overloading

- **`__add__(self, other)`**:
  - Called to implement addition (`+`).
  - Example: `def __add__(self, other):`

- **`__sub__(self, other)`**:
  - Called to implement subtraction (`-`).
  - Example: `def __sub__(self, other):`

- **`__mul__(self, other)`**:
  - Called to implement multiplication (`*`).
  - Example: `def __mul__(self, other):`

- **`__truediv__(self, other)`**:
  - Called to implement true division (`/`).
  - Example: `def __truediv__(self, other):`

- **`__floordiv__(self, other)`**:
  - Called to implement floor division (`//`).
  - Example: `def __floordiv__(self, other):`

- **`__mod__(self, other)`**:
  - Called to implement modulo operation (`%`).
  - Example: `def __mod__(self, other):`

- **`__pow__(self, other)`**:
  - Called to implement exponentiation (`**`).
  - Example: `def __pow__(self, other):`

### Comparison

- **`__eq__(self, other)`**:
  - Called to implement equality (`==`).
  - Example: `def __eq__(self, other):`

- **`__ne__(self, other)`**:
  - Called to implement inequality (`!=`).
  - Example: `def __ne__(self, other):`

- **`__lt__(self, other)`**:
  - Called to implement less-than (`<`).
  - Example: `def __lt__(self, other):`

- **`__le__(self, other)`**:
  - Called to implement less-than-or-equal (`<=`).
  - Example: `def __le__(self, other):`

- **`__gt__(self, other)`**:
  - Called to implement greater-than (`>`).
  - Example: `def __gt__(self, other):`

- **`__ge__(self, other)`**:
  - Called to implement greater-than-or-equal (`>=`).
  - Example: `def __ge__(self, other):`

### Other Special Methods

- **`__call__(self, *args, **kwargs)`**:
  - Called when an instance is called as a function.
  - Example: `def __call__(self, *args, **kwargs):`

- **`__contains__(self, item)`**:
  - Called to implement membership test operators (`in` and `not in`).
  - Example: `def __contains__(self, item):`

- **`__bool__(self)`**:
  - Called to implement the truth value testing.
  - Example: `def __bool__(self):`

- **`__hash__(self)`**:
  - Called to get the hash value of the object.
  - Example: `def __hash__(self):`

### Conclusion

Dunder methods are integral to making classes behave like built-in types and allowing for more readable and Pythonic code. By implementing these methods, you can customize the behavior of your objects and integrate them seamlessly with Python's syntax and built-in functions.