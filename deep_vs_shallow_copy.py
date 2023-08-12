import copy

#Initilaize the Lists A & B 
A = [1,4,5,7]
#C = [1,2,3]

#Assign A to B
B = copy.copy(A)

#Change or add objects to B
B.append(5)
#B.extend(C)

#Print the Addresses
print("The Memory Address of A is:",hex(id(A[3])), A)
print("The Memory Address of B is:",hex(id(B[4])), B)
