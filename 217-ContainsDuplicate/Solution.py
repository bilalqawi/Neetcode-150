# PROBLEM
# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.

# THOUGHT PROCESS
# Given integer arrays we want to check if there are any duplicates within them. Brute Forcing would 
# mean we can just loop through manually each time giving us a time complexity of O(N^2) and Space complexity of O(N^2)
# One way of solving this is utilizing the python dictionary (Hashmap) which will check in O(1), so we only loop through the 
# array one time giving us a time complexity of O(N) and a space complexity of O(N)
class Solution:
    def containsDuplicate(self, nums):
        seenDict = {}
        for num in nums:
            if num in seenDict:
                return True
            seenDict[num] = True
        return False
