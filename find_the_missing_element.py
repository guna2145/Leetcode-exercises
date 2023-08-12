#find the missing element
from collections import Counter

def find_missing_element(ar1,ar2):
    missing_ele =[]
    for a1 in ar1:
        if a1 not in ar2:
            missing_ele.append(a1)
    return missing_ele

def find_missing_element_counter(ar1,ar2):
    count1 = Counter(ar1)
    count2 = Counter(ar2)
    print(count1,count2)
    missing_ele_count =[]
    for value in ar1:
        print("Checking Value:",value)
        if value not in count2.keys():
            print("Value Not in Array2:",value)
            missing_ele_count.append(value) 
        if value in count2.keys() and count1[value] != count2[value]:
            print("Count Not matching Array2:",value,count1[value],count2[value])
            missing_ele_count.append(value)
    return missing_ele_count

        
#Define the Array 
ar1 = [1,4,5,7,8,4,4,8]
ar2 = [1,4,9,7,8,3]
#Call the function to return the results
#print(find_missing_element(ar1,ar2))
print(find_missing_element_counter(ar1,ar2))