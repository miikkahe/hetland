"""
def ss(nums):
    total = 0
    for i in range(len(nums)):
        total = (total + nums[i] ** 2)
    return total

""" # ps. ei toimi

# toinen tapa:

def ss(nums):
    return sum(x**2 for x in nums)

print ss([2, 3, 5])