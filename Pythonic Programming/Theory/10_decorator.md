# Decorators
Decorators in Python are a way to modify the behavior of functions or classes by wrapping them with another function or class. They allow you to add functionality or modify the behavior of the decorated object without directly modifying its code.

Creating and using decorators involves defining a decorator function or class and applying it to the target function or class using the `@` syntax. Here's an example that demonstrates the creation and usage of decorators for both functions and classes:

1. Decorators for Functions:

```python
# Decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

# Applying the decorator to a function
@my_decorator
def my_function():
    print("Inside the function")

# Calling the decorated function
my_function()
```

In this example, `my_decorator` is a decorator function that takes a function as an argument and returns a new wrapper function. The wrapper function is responsible for adding additional functionality before and after the execution of the original function. The `@my_decorator` syntax is used to apply the decorator to the `my_function` function. When `my_function` is called, it is automatically wrapped by the decorator, and the additional functionality is executed.

2. Decorators for Classes:

```python
# Decorator class
class MyDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print("Before class instantiation")
        instance = self.cls(*args, **kwargs)
        print("After class instantiation")
        return instance

# Applying the decorator to a class
@MyDecorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

# Creating an instance of the decorated class
obj = MyClass("John")

# Calling a method on the decorated instance
obj.say_hello()
```

In this example, `MyDecorator` is a decorator class that takes a class as an argument and modifies its instantiation behavior. The `__call__` method is called when an instance of the decorated class is created. It adds additional functionality before and after the instantiation of the original class. The `@MyDecorator` syntax is used to apply the decorator to the `MyClass` class. When an instance of `MyClass` is created, the decorator's `__call__` method is invoked, and the additional functionality is executed.

Decorators can be powerful tools for cross-cutting concerns, such as logging, timing, authentication, and more. They allow you to modularize and reuse such functionalities across multiple functions or classes without duplicating code.

Note: Decorators can also accept arguments, allowing you to customize their behavior further. To implement decorators with arguments, you would need to introduce an extra level of nested functions or classes to handle the argument passing.

It's important to keep in mind that decorators replace the decorated object with the wrapper object. If you want to preserve metadata or attributes of the original object, you may need to use tools like `functools.wraps` for functions or explicitly copy attributes for classes.

Here's a table that provides an overview of decorators in Python, along with their descriptions:

| Decorator   | Description   |
|-------------|---------------|
| `@property` | Defines a method as a property, allowing access and modification of an attribute-like behavior. |
| `@staticmethod` | Defines a method that belongs to a class rather than an instance. It doesn't have access to instance-specific data. |
| `@classmethod` | Defines a method that operates on the class itself rather than an instance. It receives the class as the first argument. |
| `@abstractmethod` | Specifies that a method must be implemented by any subclass. The subclass is forced to provide an implementation. |
| `@staticmethod` | Decorator to create a static method, which is a method that does not receive the implicit first argument (self or cls). |
| `@classmethod` | Decorator to create a class method, which receives the class as the first argument (cls) instead of the instance. |
| `@functools.wraps` | Preserves the original function's metadata (e.g., name, docstring) when creating a wrapper function. |
| `@logging_decorator` | A custom decorator that adds logging functionality to a function or method, allowing you to log information before and after its execution. |
| `@timing_decorator` | A custom decorator that measures the execution time of a function or method and prints the elapsed time. |
| `@retry_decorator` | A custom decorator that retries the execution of a function or method if it encounters an exception, providing resilience to errors. |

These are just a few examples of common decorators and their descriptions. Decorators provide a way to modify or extend the behavior of functions and classes in a flexible and reusable manner. They are a powerful tool for implementing cross-cutting concerns, modifying function behavior, enforcing contracts, and more.

## Decorator Functions
Decorator functions are functions that wrap around other functions or methods to modify their behavior or add additional functionality. They allow you to extend the functionality of existing functions without modifying their code directly.

Here's an example of a decorator function:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Add some code before the original function is called
        print("Before function execution")

        # Call the original function
        result = func(*args, **kwargs)

        # Add some code after the original function is called
        print("After function execution")

        # Return the result of the original function
        return result

    # Return the wrapper function
    return wrapper
```

In this example, `my_decorator` is a decorator function that takes a function `func` as an argument. It defines an inner function `wrapper` that wraps around the original function. The `wrapper` function adds additional code before and after calling the original function. Finally, the `wrapper` function is returned as the decorated version of the original function.

To apply the decorator to a function, you use the `@` syntax:

```python
@my_decorator
def my_function():
    print("Inside the function")
```

In this case, the `@my_decorator` syntax is used to apply the `my_decorator` function to the `my_function` function. Now, whenever `my_function` is called, it will go through the `my_decorator` function first, and the additional code defined in the decorator will be executed before and after the original function.

You can apply multiple decorators to a single function by stacking them with multiple `@` syntax lines:

```python
@decorator1
@decorator2
def my_function():
    print("Inside the function")
```

In this example, both `decorator1` and `decorator2` will be applied to the `my_function` function in the order they are listed.

Decorator functions are a powerful tool in Python that enables you to add cross-cutting functionality, such as logging, authentication, caching, and error handling, to your functions or methods in a clean and modular way.

## Decorator Classes
Decorator classes are classes that act as decorators by implementing the `__call__()` method. They provide an alternative way to decorate functions or methods and offer more flexibility and control compared to decorator functions.

Here's an example of a decorator class:

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Add some code before the original function is called
        print("Before function execution")

        # Call the original function
        result = self.func(*args, **kwargs)

        # Add some code after the original function is called
        print("After function execution")

        # Return the result of the original function
        return result
```

In this example, `MyDecorator` is a decorator class that takes a function `func` as an argument in its constructor (`__init__()` method). The class implements the `__call__()` method, which allows instances of the class to be called as if they were functions.

Inside the `__call__()` method, you can add the desired functionality before and after calling the original function, which is stored as an instance variable `self.func`. The `self.func(*args, **kwargs)` line invokes the original function.

To apply the decorator to a function, you instantiate the decorator class and use it as a callable object:

```python
@MyDecorator
def my_function():
    print("Inside the function")
```

In this case, the `@MyDecorator` syntax is used to create an instance of the `MyDecorator` class and apply it to the `my_function` function. The `MyDecorator` instance acts as a decorator by implementing the `__call__()` method. Whenever `my_function` is called, the `__call__()` method of the decorator instance is executed, and the additional code defined in the decorator is executed before and after the original function.

Similar to decorator functions, you can apply multiple decorator classes to a single function by stacking them with multiple `@` syntax lines.

Decorator classes offer more flexibility than decorator functions because they can maintain state and have additional methods. They can also accept arguments in their constructor to customize their behavior. This makes decorator classes suitable for more complex scenarios where you need to maintain state or perform additional operations during decoration.

## Decorator Parameters
Decorator parameters allow you to customize the behavior of decorators by passing arguments to them. They enable you to modify the decorator's functionality based on specific values or configurations.

To implement decorator parameters, you need to introduce an additional level of nested functions or classes. Here's an example that demonstrates how to create a decorator with parameters using a nested function:

```python
def my_decorator(param1, param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Access and use the decorator parameters
            print(f"Decorator parameters: {param1}, {param2}")

            # Add some code before the original function is called
            print("Before function execution")

            # Call the original function
            result = func(*args, **kwargs)

            # Add some code after the original function is called
            print("After function execution")

            # Return the result of the original function
            return result

        # Return the wrapper function
        return wrapper

    # Return the decorator function
    return decorator
```

In this example, `my_decorator` is a function that takes the decorator parameters `param1` and `param2`. It defines a nested function called `decorator` that acts as the actual decorator. Inside the `decorator` function, you define the wrapper function that wraps around the original function. The decorator parameters can be accessed and used within the `wrapper` function.

To apply the decorator with parameters to a function, you use the `@` syntax along with the decorator parameters:

```python
@my_decorator("value1", "value2")
def my_function():
    print("Inside the function")
```

In this case, the `@my_decorator("value1", "value2")` syntax creates an instance of the `my_decorator` function with the specified parameters and applies it to the `my_function` function. The decorator parameters are passed in as arguments when applying the decorator.

When `my_function` is called, the decorator's functionality is executed, and the decorator parameters are accessible within the wrapper function.

Decorator parameters provide a way to configure and customize decorators, allowing you to make them more flexible and adaptable to different use cases. By accepting parameters, decorators can be reused with different configurations to modify functions or methods in various ways.