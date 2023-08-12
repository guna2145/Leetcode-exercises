
import pdb

class Solution:
    num_map = {}
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            complement = target - num
            #pdb.set_trace()
            if complement in Solution.num_map:
                return [Solution.num_map[complement], i]
            Solution.num_map[num] = i
            print(Solution.num_map)
        return []

if __name__ == "__main__":
    nums = [1,4,6,8,9,5,3]
    target = 6  
    
    indices = Solution.twoSum(nums,target)
    if indices:
        print("Indices:", indices)
        print("Numbers:", nums[indices[0]], nums[indices[1]])
    else:
        print("No two numbers add up to the target.")