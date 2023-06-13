Class inheritance, also known as subclassing, is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class (called a subclass or derived class) based on an existing class (called a superclass or base class). The subclass inherits the attributes and methods of the superclass, and can also add its own attributes and methods or override the ones inherited.

To create a subclass, you define a new class and specify the superclass within parentheses after the subclass name. The subclass inherits all the attributes and methods from the superclass. Here's an example that demonstrates class inheritance:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Creating objects of the subclass
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the inherited method from the superclass
dog.speak()  # Output: The dog barks.
cat.speak()  # Output: The cat meows.
```

In this example, we have a superclass `Animal` with an `__init__` method and a `speak` method. The `speak` method is defined with a generic message.

We define two subclasses, `Dog` and `Cat`, which inherit from the `Animal` class. The subclasses override the `speak` method to provide their own implementation.

We create objects of the subclasses (`dog` and `cat`) and call the `speak` method on each object. Since the subclasses inherit the `speak` method from the superclass, calling `speak` on `dog` invokes the overridden method in the `Dog` class, and calling `speak` on `cat` invokes the overridden method in the `Cat` class.

In addition to inheriting methods, subclasses can also inherit attributes from the superclass. When creating an instance of a subclass, the subclass's `__init__` method is called. If the subclass doesn't have its own `__init__` method, it will automatically call the superclass's `__init__` method.

Inheritance allows you to create specialized classes that share common attributes and behaviors with a base class. It promotes code reuse, modularity, and extensibility. You can add additional functionality to subclasses, override inherited methods, or define new methods specific to the subclass.