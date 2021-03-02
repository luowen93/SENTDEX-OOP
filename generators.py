# x = (i for i in range(5))
#
# next(x) # Move the iterator manually
# x.__next__() # __ next method is the same as next(x)
#
# for i in x:
#     print(i)

# class range_example:
#     def __init__(self, end, step=1):
#         self.current = 0
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration() # Must be used for iterators
#         else:
#             return_val = self.current # Return the current value
#             self.current += self.step # Tranverse to next avlue
#             return return_val # Output the value
#
# for i in range_example(5):
#     print(i)

## Completely new generator
def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

x = range_gen(5)
x.__next__()

for i in x:
    print(i)

print(dir(x)) # Is an iterable because of __next__

# range_gen is not an iterable (generator)
# range_gen(5) is an iterable
# range is not an iterable (generator)
# range(5) is NOT an iterable
