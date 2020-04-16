class Solution:
    def twoSum(self, num, target):
        nums = num.copy()
        nums.sort()
        l, r = 0, len(nums) - 1

        while (l < r):
            tmpsum = nums[l] + nums[r]
            if tmpsum == target:
                l = num.index(nums[l])
                r = num.index(nums[r])
                return [l, r]
            elif tmpsum > target:
                r -= 1
            else:
                l += 1
        return -1
if __name__ == '__main__':
    test = Solution()
    for i in range(int(input())):
        print(test.twoSum(list(map(int, input().split(" "))), int(input())))
