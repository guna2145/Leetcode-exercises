import pdb


def array_pair_sum(list,target):
    seen = {}
    result = []

    for i, num in enumerate(list):
        complement = target - num
        if complement in seen:
            result.append((seen[complement],i))
        seen[num] = i
    print(''.join((list[x[0]],list[x[1]]) for x in result))

print(array_pair_sum([1,3,4,5,2,4],6))

    
