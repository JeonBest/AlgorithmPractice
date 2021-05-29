class Solution(object):
    '''
    # 공간복잡도 O(k), 시간복잡도 O(1)
    def rotate(self, nums, k):

        tmp = nums[0:-k]
        del(nums[0:-k])
        nums.extend(tmp)
    '''
    # 공간복잡도 O(1), 시간복잡도 O(k)
    def rotate(self, nums, k):

        for _ in range(0, k):
            tmp = nums.pop()
            nums.insert(0, tmp)
        
    
sol = Solution()
number = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(number, 3)
print(number)
