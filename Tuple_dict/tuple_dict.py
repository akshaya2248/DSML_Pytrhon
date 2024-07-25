# 3. Write a script to convert a tuple to a dictionary
tuple_1 = ('one', 'two', 'three')
tuple_2 = (1, 2, 3)


print("The key tuple1 = ",tuple_1)


print("The value Tuple_2 = ", tuple_2)

# Checking whether the length of both the tuples are equal or not
if len(tuple_1) == len(tuple_2):

   # converting both the tuples into a dictionary using zip()
   # and dict() functions
   # Here zip function takes elements of input tuple 1 as keys and input tuple 2 elements as values
   # Then we convert this to a dictionary using dict()
     result = dict(zip(tuple_1, tuple_2))

# printing result dictionary from the given two tuples
print("The result dictionary:", result)
