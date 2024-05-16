# Program to sort array

input = [1,3,8,2,9,2,5,6]
n = len(input)

def brute_force():
    print("input", input)
    
    for i in range(n):
        max = input[0]
        for j in range(n-i-1):
            if(j+1 < n and max > input[j+1]):
                input[j] = input[j+1]
                input[j+1] = max
            else:
                max = input[j+1]
                
                
    print('output',input)

brute_force()
