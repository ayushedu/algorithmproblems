def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    m = len(arr) // 2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])
    
    return merge(l,r)

def merge(left, right):
    i = j = 0
    output = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    while i < len(left):
        output.append(left[i])
        i += 1

    while j < len(right):
        output.append(right[j])
        j += 1

    return output


if __name__ == "__main__":
    input = [1,5,4,3,2,1]
    print("input", input)
    output = merge_sort(input)
    print('output',output)
