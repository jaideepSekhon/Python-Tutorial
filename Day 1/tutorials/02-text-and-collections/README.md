# Lesson 2: Text, lists and dictionaries

## Goal

Transform text and choose a useful way to organise data.

## Prepare text

```python
original = "  Learn Python today  "
cleaned = original.strip()
words = cleaned.lower().split()
print(words)       # ['learn', 'python', 'today']
print(len(words))  # 3
```

strip() removes whitespace at the ends; lower() lowercases text; split() without an argument splits on whitespace. These return new values and do not change original. Strings are immutable: characters cannot be replaced in place.

split() does not remove punctuation. "Hello, world!" becomes ['Hello,', 'world!'].

## Indexing and slicing

```python
word = "coding"
print(word[0])    # c
print(word[-1])   # g
print(word[1:4])  # odi
```

Indexing selects one item. Slicing selects a section, including the start and excluding the stop.

## Lists: a sequence of items

```python
topics = ["strings", "loops"]
topics.append("functions")
print(topics[1])   # loops
print(len(topics)) # 3
```

Lists can change. append() changes this list in place and returns None. Do not write `topics = topics.append("files")`.

## Dictionaries: values identified by keys

```python
student = {"name": "Riya", "age": 20}
print(student["name"])         # Riya
student["age"] = 21
print(student.get("marks", 0)) # 0
```

A mixed list such as ["Riya", 20] is valid, but named keys explain each field. Direct access to a missing key raises KeyError. get() can supply a fallback.

Display values with an f-string:

```python
print(f"{student['name']} is {student['age']} years old.")
```

## Checkpoint

1. Predict `"  AI ai  ".strip().lower().split()`.
2. Write a dictionary for a book's title and page count. Print the title and update the page count. (some methods change an object in place and return None)
3. Explain why assigning append()'s result back to a list variable is a mistake.

References: [Text and indexing](https://docs.python.org/3/tutorial/introduction.html#text), [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods), [Lists and dictionaries](https://docs.python.org/3/tutorial/datastructures.html).
