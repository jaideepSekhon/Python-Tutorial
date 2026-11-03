# Lesson 1: Types determine what an operation means

## Goal

Distinguish numeric values from numeric-looking text and convert input deliberately.

You already recognise int, str, float and bool. Python does not require a type declaration when assigning a variable. Values have types; inspect them with type().

```python
quantity = 12
label = "12"
print(type(quantity))  # <class 'int'>
print(type(label))     # <class 'str'>
```

The same operator can behave differently for different types:

```python
print(12 + 3)       # 15
print("12" + "3")   # 123
print("12" * 3)     # 121212
```

String multiplication repeats text. This is valid, not an error caused by Python being interpreted. However, `"12" + 3` raises TypeError.

## Input is text

```python
age_text = input("Age: ")
age = int(age_text)
print(age + 1)
```

Entering 20 prints 21. input() returns a string; conversion is necessary for this arithmetic. int("twenty") raises ValueError because that text cannot be interpreted as an integer. Exception handling comes later.

Conversion produces a value; it does not change the original string:

```python
text = "7"
number = int(text)
print(text * 2)    # 77
print(number * 2)  # 14
```

Use float() for decimal input and str() when you deliberately need text.

## Checkpoint — answer before running

1. Predict both outputs and explain the difference:

```python
text = "8"
print(text + "2")
print(int(text) + 2)
```

2. A user enters 2.5. What problem does `int(input("Hours: "))` encounter? Which conversion fits?
3. Write three lines that ask for a price, convert it to a decimal number, and print twice that price.

References: [Built-in functions](https://docs.python.org/3/library/functions.html#input), [Python's introduction](https://docs.python.org/3/tutorial/introduction.html#text).
