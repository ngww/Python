# Classes at Runtime
In Python, you can dynamically create classes at runtime using the `type()` function. The `type()` function is a built-in function that allows you to create new classes dynamically.

The `type()` function takes three arguments: the name of the class, a tuple of base classes (inheritance), and a dictionary containing the class attributes and methods.

Here's an example that demonstrates how to create a class dynamically at runtime:

```python
# Dynamic class creation
MyClass = type('MyClass', (), {})

# Create an instance of the dynamically created class
obj = MyClass()

# Add an attribute to the instance
obj.name = 'John'

# Access the attribute
print(obj.name)  # Output: John
```

In this example, the `type()` function is used to create a class named `MyClass` with no base classes and an empty dictionary for attributes and methods. The `type()` function returns a new class object, which is assigned to the `MyClass` variable.

You can then create an instance of the dynamically created class using the `MyClass()` syntax, just like any other class.

Since the dynamically created class has an empty dictionary, you can add attributes or methods to it dynamically. In this case, an attribute named `name` is added to the `obj` instance, and its value is set to `'John'`. The added attribute can be accessed like any other attribute of an object.

You can also specify base classes and attributes/methods when creating the class dynamically. Here's an example that demonstrates class inheritance and attribute addition:

```python
# Dynamic class creation with inheritance and attributes
BaseClass = type('BaseClass', (), {'base_attr': 10})

# Create a new class inheriting from BaseClass
DerivedClass = type('DerivedClass', (BaseClass,), {'derived_attr': 'Hello'})

# Create an instance of the derived class
obj = DerivedClass()

# Access attributes from both classes
print(obj.base_attr)     # Output: 10
print(obj.derived_attr)  # Output: Hello
```

In this example, the `BaseClass` is created with an attribute `base_attr`, and the `DerivedClass` is created by inheriting from `BaseClass` and adding an attribute `derived_attr`. The instance of the `DerivedClass` has access to both attributes.

Dynamic class creation using `type()` provides flexibility when you need to create classes dynamically at runtime, allowing you to tailor classes based on specific requirements or conditions.