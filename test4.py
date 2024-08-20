# def ArrayChallenge(num):

#     varOcg = [int(digit) for digit in str(num)]
    

#     multiplication_count = 0
    

#     while True:
        
#         multiplier = varOcg[1] 
#         num *= multiplier
#         multiplication_count += 1
        
    
#         new_digits = [int(digit) for digit in str(num)]
#         varOcg.extend(new_digits)
        
    
#         for i in range(1, len(varOcg)):
#             if varOcg[i] == varOcg[i - 1]:
#                 return multiplication_count

# # Example usage:
# print(ArrayChallenge(1234))  # Output should be 1

# def ArrayChallenge(arr):
#     varOcg = []

#     for i in range(len(arr)):
#         nearest_smaller = -1
#         for j in range(i - 1, -1, -1):
#             if arr[j] <= arr[i]:
#                 nearest_smaller = arr[j]
#                 break
#         varOcg.append(nearest_smaller)

#     return ' '.join(map(str, varOcg))

# # Example usage:
# print(ArrayChallenge([5, 3, 1, 9, 7, 3, 4, 1]))  # Output: -1 -1 -1 1 1 1 3 1
# print(ArrayChallenge([2, 4, 5, 1, 7]))           # Output: -1 2 4 -1 1

def ArrayChallenge(num):
    multiplier = 2  # assuming a fixed multiplier of 2
    min_count = float('inf')
    
    for i in num:
        result_list = [i]
        count = 0
        product = i * multiplier
        while product not in result_list:
            result_list.append(product)
            count += 1
            product *= multiplier
        min_count = min(min_count, count)
    
    return min_count
print(ArrayChallenge(input(8)))