from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen : dict[int, int] = {}

        for i,num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need],i]
            seen[num] = i

        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print(result)  # Output: [0, 1]