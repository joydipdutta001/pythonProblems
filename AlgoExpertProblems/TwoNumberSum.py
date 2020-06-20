# O(n^2) time || O(1) space

def numbersum(lista, targetsum):
    for i in range(len(lista)-1):
        fnum = lista[i]
        for j in range(i+1, len(lista)):
            snum = lista[j]
            if fnum + snum == targetsum:
                return [fnum, snum]
    return []


# O(n) time || O(n) space
def numberSumArray(array, targetSum):
    nums={}

    for num in array:
        difference = targetSum-num
        if difference in nums:
            return [difference, num]
        else:
            nums[num] = True
    return []

# O(nlog(n)) time || O(1) space
def numbersummore(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left<right:
        currentSum = array[left]+ array[right]
        if currentSum == targetSum:

            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum >targetSum:
            right -= 1
    return []



# Try it YourSelf
array = [23,43,-1,1,-11,-4,4,11,10]
targetSum = 15

print(str(numbersum(array,targetSum))+ " "+
str(numberSumArray(array,targetSum))+" "+
str(numbersummore(array,targetSum)))