#Solution 1

def twoNumberSum(array,targetSum):
    for i in  range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
    return []

num = [2,8,3,4,5,7]
result = twoNumberSum(num,8)
print(result)

#Solution 2
def twoNumberSum(array,targetSum):
    nums = {}
    for num  in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []

print(twoNumberSum([2,4,6,8], 10))












