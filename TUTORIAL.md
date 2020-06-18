# Basic Python Example

A test to try Python with CodeRoad

## L1 Add some numbers together

> Test out the basics



This is just a test, so here's the answer:

```py
def add(*args):
    '''Add 1 or more numbers together'''
    total = 0
    for arg in args:
        total += arg
    return total
```

### L1S1 Add

Complete the `add` function. It should be able to add one or more numbers together. 
For example: `add(1) = 1`, `add(1, 2) = 3`, and `add(1, 2, 3) = 6`.
