
from random import randint
'''
    list is a DS which is a mutable ordered sequence of elements
    list can have heterogenous elements
'''
simple_list = [1,2,3,42,5,61]
print("this is a simple list {}".format(simple_list))
print("This is the subscripted access to an element in list :{}".format(simple_list[0]))
print("This is the subscripted access (-ve index) to an element in list :{}".format(simple_list[-1]))
slice_of_list = simple_list[1:3]
print("this is slice of list {}".format(slice_of_list))
num = randint(1, len(simple_list))
if num in simple_list:
    print("random number generated is in the list")
else:
    print("random number generated is not in the list")

