# assuming there is a solution then there must exist integers a, b in nums such that target = [a,b], so target = a + b
# or a = target - b
# use a dictionary to keep track of past numbers and check if 
# O(n) time, O(n) space
def twoSum(self, nums, target):
        d = {}
        for i, b in enumerate(nums):
            a = target - b
            if a in d:
                return [d[a], i]
            else:
                d[b] = i
