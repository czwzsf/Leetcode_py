'''
class Solution():
    def twosum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''
# 暴力方法，用两个for循环来遍历


# 哈希表
class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping.keys():
                return [mapping[diff], i]
            else:
                mapping[nums[i]] = i


s1 = Solution()
print(s1.twosum([2, 7, 9, 11], 9))
