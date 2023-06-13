# Class Properties
In Python, properties are a way to add getter, setter, and deleter methods to class attributes, allowing you to define computed or controlled access to the attributes. Properties provide a mechanism to encapsulate attribute access and ensure consistency and validation.

To add properties to a class, you can use the `@property`, `@<attribute>.setter`, and `@<attribute>.deleter` decorators. Here's an example that demonstrates how to add properties to a class:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

# Creating an object of the Circle class
circle = Circle(5)

# Accessing the radius property
print(circle.radius)  # Output: 5

# Setting the radius property
circle.radius = 10
print(circle.radius)  # Output: 10

# Trying to set a negative radius
circle.radius = -5  # Raises a ValueError

# Deleting the radius property
del circle.radius
print(circle.radius)  # Raises an AttributeError
```

In this example, we define a class named `Circle` with a private attribute `_radius`. We add a property named `radius` using the `@property` decorator. The `radius` property serves as a getter method, allowing us to access the `_radius` attribute.

We also define a setter method for the `radius` property using the `@radius.setter` decorator. The setter method validates the input and raises a `ValueError` if the radius is negative. If the input is valid, the setter method updates the `_radius` attribute.

Additionally, we add a deleter method for the `radius` property using the `@radius.deleter` decorator. The deleter method deletes the `_radius` attribute.

To access the `radius` property, we can use the dot notation (`object.radius`). This calls the getter method and returns the current value of the `_radius` attribute.

To set the `radius` property, we assign a value to it (`object.radius = value`). This calls the setter method, which validates the input and updates the `_radius` attribute if the value is valid.

To delete the `radius` property, we can use the `del` statement (`del object.radius`). This calls the deleter method, which deletes the `_radius` attribute.

Properties provide a way to define controlled access to attributes while maintaining the simplicity of attribute access syntax. They allow you to define custom behavior for getting, setting, and deleting attributes, enabling you to enforce rules and constraints on attribute values.