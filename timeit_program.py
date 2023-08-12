import timeit 

final_list = []

stmt= """
def add2num(num1,num2):
    for i,j in zip(num1, num2):
        result = i + j
        final_list.append(result)
    return final_list
"""

timeit(stmt, 1000)