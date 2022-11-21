class solution(object):
    def moveZeros(self, nums):
        append_time = nums.count(0)
        for i in range(append_time):
            nums.remove(0)
            nums.append(0)