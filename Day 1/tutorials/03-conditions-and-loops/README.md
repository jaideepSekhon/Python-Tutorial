# Lesson 3: Conditions and loops

## Goal

Translate an algorithm into valid Python, with deliberate boundaries.

## Blocks use indentation

```python
minutes = 25
if minutes >= 20:
    print("Enough time for practice")
else:
    print("Try a short recall exercise")
```

A colon starts the block; indent its statements consistently. Use four spaces. Python uses and, or and not for boolean logic. `18 <= age <= 60` is a valid chained comparison.

## Iterate directly over values

```python
words = ["learn", "python"]
for word in words:
    print(word.upper())
```

Use `for word in words:`, not `for word in range words:`. range() is useful for a sequence of integers.

```python
for number in range(2, 7, 2):
    print(number)  # 2, then 4, then 6 on separate lines
```

The stop value is excluded. range(4) yields 0, 1, 2, 3.

## Accumulate a result

```python
length_total = 0
for word in ["red", "blue"]:
    length_total += len(word)
print(length_total)  # 7
```

Initialise before the loop. Doing it inside would reset the result each iteration. `total += value` means `total = total + value` here.

## Checkpoint

1. Predict the values from range(1, 6, 2).
2. Write a loop counting words longer than four characters. Use ['cat', 'python', 'notes', 'ai'].
3. What should your counter produce for an empty list? Explain why.

Reference: [Control flow](https://docs.python.org/3/tutorial/controlflow.html).
