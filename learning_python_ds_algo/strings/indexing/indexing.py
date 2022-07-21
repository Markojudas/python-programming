# strings are a list of characters and can be indexed

name = "Interstellar"

print(name[0])  # I
print(name[-1])  # reverse index = this is the last index

# name[-1] = 't' -> error, str is immutable


# SLICING

# arr[start:stop] -> inclusive:exclusive
# arr[5:] -> goes from index 5 until the end
# arr[:5] -> starts from the beginning until index 5


# arr[start:stop:step] -> step is 1 by default

nums = "0123456789"

print(nums[::2])  # printing even numbers
print(nums[1::2])  # printing odd numbers
print(nums[::-1])  # reverse
