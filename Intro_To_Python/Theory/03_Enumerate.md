# Enumerate()
The `enumerate()` function in Python is a built-in function that allows you to iterate over an iterable object (such as a list, tuple, or string) while also keeping track of the index of each element. It returns an enumerate object that yields pairs of index and value. Here's the general syntax of `enumerate()`:

```python
enumerate(iterable, start=0)
```

The `iterable` parameter represents the object that you want to iterate over, and the `start` parameter (optional) specifies the starting index value (default is 0).

Here's an example demonstrating the usage of `enumerate()`:

```python
fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:
```
0 apple
1 banana
2 cherry
3 date
```

In the example above, the `enumerate()` function is used to iterate over the `fruits` list. The `index` variable stores the index of each element, and the `fruit` variable stores the corresponding value. The `print()` statement displays the index and value pairs.

By default, `enumerate()` starts counting from 0, but you can specify a different starting index if needed. For example:

```python
fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:
```
1 apple
2 banana
3 cherry
4 date
```

In this case, `enumerate()` starts counting from 1 instead of 0.

The `enumerate()` function is helpful when you need to access both the index and value of elements in an iterable, making it easier to perform tasks like counting, filtering, or mapping elements in a loop.