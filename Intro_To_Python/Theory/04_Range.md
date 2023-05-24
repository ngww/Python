# Range()
The `range()` function in Python is a built-in function that generates a sequence of numbers. It can be used in various scenarios, such as iterating over a sequence of numbers or creating loops with a specific number of iterations. Here's the general syntax of `range()`:

```python
range(stop)
range(start, stop[, step])
```

The `range()` function takes one, two, or three arguments:

- With one argument, `range(stop)`, it generates a sequence of numbers from 0 to `stop-1`.
- With two arguments, `range(start, stop)`, it generates a sequence of numbers from `start` to `stop-1`.
- With three arguments, `range(start, stop, step)`, it generates a sequence of numbers from `start` to `stop-1`, incrementing by `step` in each iteration.

Here are some examples illustrating the usage of `range()`:

```python
# Example 1: Using range(stop)
for num in range(5):
    print(num)

# Output: 0, 1, 2, 3, 4

# Example 2: Using range(start, stop)
for num in range(2, 8):
    print(num)

# Output: 2, 3, 4, 5, 6, 7

# Example 3: Using range(start, stop, step)
for num in range(1, 10, 2):
    print(num)

# Output: 1, 3, 5, 7, 9
```

In Example 1, `range(5)` generates a sequence of numbers from 0 to 4. The `for` loop iterates over each number in the sequence.

In Example 2, `range(2, 8)` generates a sequence of numbers from 2 to 7 (stop-1). The `for` loop iterates over each number in the sequence.

In Example 3, `range(1, 10, 2)` generates a sequence of odd numbers from 1 to 9 (stop-1), incrementing by 2 in each iteration.

Note that `range()` returns an object of the `range` type, which represents the sequence of numbers. If you need a list of the numbers, you can convert it to a list using the `list()` function:

```python
numbers = list(range(5))
print(numbers)

# Output: [0, 1, 2, 3, 4]
```

The `range()` function is commonly used in `for` loops when you need to iterate over a specific range of numbers or perform a specific number of iterations.