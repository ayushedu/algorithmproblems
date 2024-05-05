"""
Given an array on n, calculate max subarray sum
"""

input = [-1,2,4,-3,5,2,-5,2]

# O(n2)
def brute_force():
    max = input[0]
    count = len(input)
    for i in range(0, count):
        sum = input[i]
        for x in range(i+1, count):
            sum += input[j]
            if(sum > max):
                max = sum


    print("max using brute force is",max)

# O(n)
def efficient_one():
    sum = 0
    best = 0
    n = len(input)

    for x in input:
        if(x < sum + x):
            sum = sum + x
        else:
            sum = x

        if(best < sum):
            best = sum

    print(best)
    
efficient_one()
