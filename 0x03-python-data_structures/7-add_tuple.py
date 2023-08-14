#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    final_tuple = ()
    new_tuple_1 = tuple_a + (0, 0)
    new_tuple_2 = tuple_b + (0, 0)
    final_tuple = new_tuple_1[0] + new_tuple_2[0], new_tuple_1[1] + new_tuple_2[1]
    return final_tuple
