# Lesson 4: Functions, return and tracing

## Goal

Write a complete reusable function and distinguish its return value from printed output.

```python
def word_length(word):
    return len(word)

size = word_length("hello")
print(size + 2)  # 7
```

word is a parameter; "hello" is the argument. The call returns 5, assigned to size. Only print() displays output in this script. return exits that function call and sends a value to the caller.

Compare:

```python
def show_length(word):
    print(len(word))

result = show_length("hello")  # displays 5
print(result)                 # displays None
```

A function reaching the end without an explicit return returns None. Printing a value does not return it.

## Trace before guessing

For each line, ask: what runs now, which variable changes, and is anything printed? Defining a function does not run its body. Calling it does.

## Checkpoint

1. Predict exactly what is printed:

```python
def increase(number):
    return number + 3

result = increase(4)
print(result * 2)
```

2. Write sum_positive(numbers), returning the sum of values strictly greater than zero. Include the definition, initialisation, loop, condition and return. Use total rather than sum as a variable name to avoid hiding Python's built-in sum().

3. Check these cases after your attempt:

| Input | Expected return |
| --- | --- |
| [3, -1, 0, 8, -5, 2] | 13 |
| [] | 0 |
| [-4, -2] | 0 |

Explain where return belongs and why. This is a tutorial checkpoint; demo and homework projects come afterward.

Reference: [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
